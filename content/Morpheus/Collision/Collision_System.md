# Collision System

---

```typescript
import BoxCollider from '../ecs_component/BoxCollider'
import RigidBody from '../ecs_component/RigidBody'
import Transform from '../ecs_component/Transform'
import CollisionObject from '../ecs_component/CollisionObject'
import IVector2 from '../math/IVector2'
import IEntityCache from '../ecs_cache/IEntityCache'
import IEntity from '../ecs_entity/IEntity'
import System from '../ecs_system_core/System'
import ICollisionHandler from './ICollisionHandler'
import CollisionDetector from '../collision_detector/CollisionDetector'
import { ICollision } from '../collision_detector/ICollision'
import ICollisionEntity from '../collision_detector/ICollisionEntity'
import { IRect } from '../collision_detector/IRect'

export default class Collision extends System {
  private _cache = new Map<string, ICollision[]>()

  constructor(
    entityCache: IEntityCache,
    private readonly _collisionDetector: CollisionDetector,
    private readonly _collisionHandlers: Map<string, ICollisionHandler[]>
  ) {
    super(entityCache)
  }

  protected override startEntity(entity: IEntity) {
    const colliders = entity.getComponents(BoxCollider)
    if (!colliders) throw new Error(`No colliders in ${entity.id}`)

    const collisions: ICollision[] = []

    for (const collider of colliders) {
      const handlers = this._collisionHandlers.get(collider.id)
      if (!handlers) continue

      const collision = {
        object1: {} as ICollisionEntity,
        object2: {} as ICollisionEntity,

        rect1: {} as IRect,
        rect2: {} as IRect,

        point1: {} as IVector2,
        point2: {} as IVector2,
      }
      this.setCollision(collision, entity, collider)

      this._collisionDetector.start(collision)

      for (const handler of handlers) {
        this._collisionDetector.subscribe(
          collision,
          handler.onCollisionHandler.bind(handler),
          handler.offCollisionHandler.bind(handler)
        )
      }

      collisions.push(collision)
    }

    this._cache.set(entity.id, collisions)
  }

  private setCollision(
    collision: ICollision,
    entity: IEntity,
    collider: BoxCollider
  ) {
    this.setObject1(collision, entity, collider)
    this.setObject2(collision, entity)
  }

  private setObject1(
    collision: ICollision,
    entity: IEntity,
    collider: BoxCollider
  ) {
    collision.object1 = {
      entityId: entity.id,
      collider,
      rigidBody: entity.getComponentStrict(RigidBody),
      transform: entity.getComponentStrict(Transform),
    }
  }

  private setObject2(collision: ICollision, entity: IEntity) {
    const entity2 = this.getEntity2(entity)
    collision.object2 = {
      entityId: entity2.id,
      collider: entity2.getComponentStrict(BoxCollider),
      rigidBody: entity2.getComponentStrict(RigidBody),
      transform: entity2.getComponentStrict(Transform),
    }
  }

  private getEntity2(entity: IEntity) {
    return this._entityCache.getStrict(
      entity.getComponentStrict(CollisionObject).objectIdToCollideWith
    )
  }

  protected override updateEntity(entity: IEntity, _deltaTime: number): void {
    const collisions = this._cache.get(entity.id)
    if (collisions) {
      for (const collision of collisions) {
        this._collisionDetector.update(collision)
      }
    }
  }

  protected override renderEntity(entity: IEntity, _deltaTime: number): void {
    const collisions = this._cache.get(entity.id)
    if (collisions) {
      for (const collision of collisions) {
        this._collisionDetector.draw(collision)
      }
    }
  }
}
```

<audio controls>
  <source src="./audio_en/Collision_System.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>
This `Collision` class is a system that manages collision detection and handling within an entity-component-system (ECS) architecture. It utilizes various components like `BoxCollider`, `RigidBody`, and `Transform` to detect and process collisions between entities. Below is a breakdown of the class:

### Class Overview:

- **Inheritance**: The `Collision` class extends a `System` class, which is a core part of an ECS framework, indicating that it's responsible for handling the behavior of entities related to collisions.
- **Dependencies**: It requires an `IEntityCache` (to store and manage entities), a `CollisionDetector` (for detecting collisions), and a map of collision handlers (`_collisionHandlers`) that define specific collision response behaviors for various objects.

### Key Fields:

1. **\_cache (Map<string, ICollision[]>)**:

   - Caches a list of collision objects for each entity by storing the entity ID as the key and a list of `ICollision` objects as the value.
   - This cache allows the system to manage ongoing collisions and avoid redundant collision computations.

2. **\_collisionDetector (CollisionDetector)**:
   - The object responsible for performing actual collision detection and determining if two entities have collided.
3. **\_collisionHandlers (Map<string, ICollisionHandler[]>)**:
   - Maps entity IDs to collision handlers (functions that determine what to do when a collision occurs).
   - Each collider has an associated set of handlers that are invoked when the collision detector detects an overlap.

### Key Methods:

1. **startEntity(entity: IEntity)**:

   - Called when the system is initialized for a specific entity.
   - Retrieves all `BoxCollider` components of the entity, generates collision objects, and subscribes collision handlers to those objects.
   - Each collision object is added to the `_cache` for future use.
   - This method sets up all necessary objects (`ICollisionEntity`, `IRect`, `IVector2`) to represent collision data for two entities.

2. **setCollision(collision: ICollision, entity: IEntity, collider: BoxCollider)**:

   - Responsible for setting up the `ICollision` object, which contains two main parts:
     - `object1`: The entity initiating the collision.
     - `object2`: The other entity involved in the collision.
   - Calls helper methods (`setObject1`, `setObject2`) to configure these objects.

3. **setObject1 / setObject2**:

   - These methods set the collision data for the two entities involved in the collision, including their colliders, rigid bodies, and transforms.

4. **getEntity2(entity: IEntity)**:

   - Retrieves the second entity involved in the collision based on a reference stored in the `CollisionObject` component of the first entity.
   - This lookup happens through the `IEntityCache`, ensuring the system has access to all necessary entities.

5. **updateEntity(entity: IEntity, \_deltaTime: number)**:

   - Updates the state of collisions for an entity, based on time progression or game state changes.
   - This is called every game update cycle and ensures that the collision detector updates the collision's state.

6. **renderEntity(entity: IEntity, \_deltaTime: number)**:
   - Used to visualize or process rendering of the collision (if needed).
   - The method draws the collision-related data through the `CollisionDetector`, which might visualize collision boundaries or related information.

### General Flow:

- When an entity is started, the system checks if it has a `BoxCollider`, sets up collision data (`ICollision`), and subscribes the relevant handlers.
- During each update and render cycle, the system updates the state of the collisions using the collision detector and triggers visual feedback or processing if necessary.

### Example Use:

1. **Entity Setup**: An entity with a `BoxCollider` and `RigidBody` is added to the ECS. The system prepares it for collision detection with other entities.
2. **Collision Detection**: The `CollisionDetector` checks if this entity collides with another entity.
3. **Collision Handlers**: If a collision occurs, the system triggers the appropriate handlers (like bouncing, damage, or sound effects).
4. **Rendering**: If required, it draws collision boundaries for debugging or visualization purposes.

This design is typical in physics or game engines where entities with colliders interact, and different handlers are invoked based on collisions between objects.
