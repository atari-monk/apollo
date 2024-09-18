# Collision System

This `Collision` class is a system that manages collision detection and handling within an entity-component-system (ECS) architecture. It utilizes various components like `BoxCollider`, `RigidBody`, and `Transform` to detect and process collisions between entities. Below is a breakdown of the class:

### Class Overview:

- **Inheritance**: The `Collision` class extends a `System` class, which is a core part of an ECS framework, indicating that it's responsible for handling the behavior of entities related to collisions.
- **Dependencies**: It requires an `IEntityCache` (to store and manage entities), a `CollisionDetector` (for detecting collisions), and a map of collision handlers (`_collisionHandlers`) that define specific collision response behaviors for various objects.

### Key Fields:

1. **Cache**:

   - Caches a list of collision objects for each entity by storing the entity ID as the key and a list of `ICollision` objects as the value.
   - This cache allows the system to manage ongoing collisions and avoid redundant collision computations.

2. **CollisionDetector**:
   - The object responsible for performing actual collision detection and determining if two entities have collided.
3. **CollisionHandlers**:
   - Maps entity IDs to collision handlers (functions that determine what to do when a collision occurs).
   - Each collider has an associated set of handlers that are invoked when the collision detector detects an overlap.

### Key Methods:

1. **startEntity**:

   - Called when the system is initialized for a specific entity.
   - Retrieves all `BoxCollider` components of the entity, generates collision objects, and subscribes collision handlers to those objects.
   - Each collision object is added to the `_cache` for future use.
   - This method sets up all necessary objects (`ICollisionEntity`, `IRect`, `IVector2`) to represent collision data for two entities.

2. **setCollision**:

   - Responsible for setting up the `ICollision` object, which contains two main parts:
     - `object1`: The entity initiating the collision.
     - `object2`: The other entity involved in the collision.
   - Calls helper methods (`setObject1`, `setObject2`) to configure these objects.

3. **setObject1 / setObject2**:

   - These methods set the collision data for the two entities involved in the collision, including their colliders, rigid bodies, and transforms.

4. **getEntity2**:

   - Retrieves the second entity involved in the collision based on a reference stored in the `CollisionObject` component of the first entity.
   - This lookup happens through the `IEntityCache`, ensuring the system has access to all necessary entities.

5. **updateEntity**:

   - Updates the state of collisions for an entity, based on time progression or game state changes.
   - This is called every game update cycle and ensures that the collision detector updates the collision's state.

6. **renderEntity**:
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
