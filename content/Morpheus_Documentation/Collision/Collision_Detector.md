# Collision Detector

## IRect

Interface describes a rectangle with:

1. **position**: Coordinates of the rectangle's location.
2. **size**: Width and height of the rectangle.
3. **halfSize**: Half of the rectangle’s width and height.

It provides a structure for handling 2D rectangles, including their position, dimensions, and bounds.

## ICollisionEntity

Interface defines an entity involved in collision detection and physics. It includes:

1. **entityId**: A unique identifier for the entity.
2. **transform**: Defines the entity’s position, rotation, and scale.
3. **collider**: Represents the entity's collision shape as a box.
4. **rigidBody**: Simulates physical properties like mass and velocity for interaction with the physics system.

This interface integrates components for positioning, collision detection, and physics simulation in a game or simulation system.

## ICollision

Interface represents a collision between two entities, `object1` and `object2`, both of type `ICollisionEntity`.

It also includes two corresponding rectangular bounds, `rect1` and `rect2`, of type `IRect`, which define the areas where the collision occurs.

## ICollisionCallback

Interface defines a function that takes an `ICollision` object as a parameter and returns `void`.  
It is used as a callback to handle collision events between two entities.

## ICollisionAlgorithm

Interface defines the structure for a collision detection algorithm. It includes three methods:

- `start`: Initializes or processes the start of a collision.
- `isColliding`: Returns a boolean indicating if a collision is occurring.
- `draw`: Visualizes the collision.

This interface provides a framework for managing and evaluating collisions between entities.

## CollisionDetector

The class is responsible for managing collision detection and handling in a system. Here's a brief overview of its functionality:

- **Constructor**: Takes an `ICollisionAlgorithm` instance to handle the specifics of collision detection and visualization.
- **`start`**: Initializes the collision process using the provided collision algorithm.
- **`update`**: Checks if a collision is occurring and triggers the appropriate callback based on whether a collision is detected.
- **`subscribe`**: Registers callbacks to be called when a collision occurs or stops occurring.
- **`draw`**: Uses the collision algorithm to visualize the collision.

The class maintains two maps of callbacks: one for when a collision is detected and one for when no collision is detected, identified by a unique key generated from the involved entities.
