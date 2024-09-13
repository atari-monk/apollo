# Collision Detector

## IRect

```typescript
import IVector2 from '../math/IVector2'

export interface IRect {
  position: IVector2
  size: IVector2
  halfSize: IVector2
}
```

<audio controls>
  <source src="./audio_en/IRect.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>
The `IRect` interface describes a rectangle with:

1. **position**: Coordinates of the rectangle's location.
2. **size**: Width and height of the rectangle.
3. **halfSize**: Half of the rectangle’s width and height.

It provides a structure for handling 2D rectangles, including their position, dimensions, and bounds.

## ICollisionEntity

```typescript
import IBoxCollider from '../ecs_component/IBoxCollider'
import IRigidBody from '../ecs_component/IRigidBody'
import ITransform from '../ecs_component/ITransform'

export default interface ICollisionEntity {
  entityId: string
  transform: ITransform
  collider: IBoxCollider
  rigidBody: IRigidBody
}
```

<audio controls>
  <source src="./audio_en/ICollisionEntity.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>
The `ICollisionEntity` interface defines an entity involved in collision detection and physics. It includes:

1. **entityId**: A unique identifier for the entity.
2. **transform**: Defines the entity’s position, rotation, and scale.
3. **collider**: Represents the entity's collision shape as a box.
4. **rigidBody**: Simulates physical properties like mass and velocity for interaction with the physics system.

This interface integrates components for positioning, collision detection, and physics simulation in a game or simulation system.

## ICollision

```typescript
import IVector2 from '../math/IVector2'
import ICollisionEntity from './ICollisionEntity'
import { IRect } from './IRect'

export interface ICollision {
  object1: ICollisionEntity
  object2: ICollisionEntity

  rect1: IRect
  rect2: IRect
}
```

<audio controls>
  <source src="./audio_en/ICollision.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>
The `ICollision` interface represents a collision between two entities, `object1` and `object2`, both of type `ICollisionEntity`.  
It also includes two corresponding rectangular bounds, `rect1` and `rect2`, of type `IRect`, which define the areas where the collision occurs.

## ICollisionCallback

```typescript
import { ICollision } from './ICollision'

export default interface ICollisionCallback {
  (collision: ICollision): void
}
```

<audio controls>
  <source src="./audio_en/ICollisionCallback.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>
The `ICollisionCallback` interface defines a function that takes an `ICollision` object as a parameter and returns `void`.  
It is used as a callback to handle collision events between two entities.

## ICollisionAlgorithm

```typescript
import { ICollision } from './ICollision'

export default interface ICollisionAlgorithm {
  start(collision: ICollision): void
  isColliding(collision: ICollision): boolean
  draw(collision: ICollision): void
}
```

<audio controls>
  <source src="./audio_en/ICollisionAlgorithm.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>
The `ICollisionAlgorithm` interface defines the structure for a collision detection algorithm. It includes three methods:
- `start(collision: ICollision)`: Initializes or processes the start of a collision.
- `isColliding(collision: ICollision)`: Returns a boolean indicating if a collision is occurring.
- `draw(collision: ICollision)`: Visualizes the collision.

This interface provides a framework for managing and evaluating collisions between entities.

## CollisionDetector

```typescript
import { ICollision } from './ICollision'
import ICollisionAlgorithm from './ICollisionAlgorithm'
import ICollisionCallback from './ICollisionCallback'

export default class CollisionDetector {
  private _collisionCallbacks: Map<string, ICollisionCallback> = new Map()
  private _noCollisionCallbacks: Map<string, ICollisionCallback> = new Map()

  constructor(private readonly _collisionAlgorithm: ICollisionAlgorithm) {}

  start(collision: ICollision): void {
    this._collisionAlgorithm.start(collision)
  }

  private getCollisionKey(collision: ICollision): string {
    const id1 = collision.object1.entityId
    const cid1 = collision.object1.collider.id
    const id2 = collision.object2.entityId

    const key = cid1 ? `${id1}_${cid1}_${id2}` : `${id1}_${id2}`

    return key
  }

  update(collision: ICollision) {
    const isColliding = this._collisionAlgorithm.isColliding(collision)

    const key = this.getCollisionKey(collision)

    if (isColliding) {
      const callback = this._collisionCallbacks.get(key)
      if (callback) {
        callback(collision)
      }
    } else {
      const callback = this._noCollisionCallbacks.get(key)
      if (callback) {
        callback(collision)
      }
    }
  }

  subscribe(
    collision: ICollision,
    collisionCallback: ICollisionCallback,
    noCollisionCallback: ICollisionCallback
  ): void {
    const key = this.getCollisionKey(collision)
    this._collisionCallbacks.set(key, collisionCallback)
    this._noCollisionCallbacks.set(key, noCollisionCallback)
  }

  draw(collision: ICollision) {
    this._collisionAlgorithm.draw(collision)
  }
}
```

<audio controls>
  <source src="./audio_en/CollisionDetector.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>
The `CollisionDetector` class is responsible for managing collision detection and handling in a system. Here's a brief overview of its functionality:

- **Constructor**: Takes an `ICollisionAlgorithm` instance to handle the specifics of collision detection and visualization.
- **`start(collision: ICollision): void`**: Initializes the collision process using the provided collision algorithm.
- **`update(collision: ICollision): void`**: Checks if a collision is occurring and triggers the appropriate callback based on whether a collision is detected.
- **`subscribe(collision: ICollision, collisionCallback: ICollisionCallback, noCollisionCallback: ICollisionCallback): void`**: Registers callbacks to be called when a collision occurs or stops occurring.
- **`draw(collision: ICollision): void`**: Uses the collision algorithm to visualize the collision.

The class maintains two maps of callbacks: one for when a collision is detected and one for when no collision is detected, identified by a unique key generated from the involved entities.
