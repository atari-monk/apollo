# TopLeftCollision Algorithm

The `TopLeftCollision` class implements the `ICollisionAlgorithm` interface, which is used for detecting collisions between rectangular objects. Here's a breakdown of its components:

### Components

1. **Properties:**

   - `rect1` and `rect2` are private properties that represent the rectangles involved in the collision detection. They are of type `IRect`.

2. **Methods:**

   - **`start`**: Initializes the `rect1` and `rect2` properties based on the `collision` object passed as a parameter. It extracts the positions and sizes of the two colliding objects and sets them to `rect1` and `rect2`. Note that the `halfSize` property of `IRect` is set to `Vector2.zero` and is not used in the collision logic.

   - **`isColliding`**: Determines if the two rectangles are colliding. This method uses the axis-aligned bounding box (AABB) collision detection algorithm. It checks if the rectangles overlap by comparing their positions and sizes.

   - **`draw`**: This method is a placeholder for drawing the collision or debug information. In this implementation, it does nothing (`;`).

### Usage

- **Initialization**: The `start` method is called to set up the rectangles with their respective positions and sizes. This method must be called before performing collision checks.

- **Collision Check**: The `isColliding` method is used to check if the two rectangles intersect. It returns `true` if there is a collision and `false` otherwise.

- **Drawing**: The `draw` method is currently a no-op but can be used to visualize or debug the collision if needed.

This class is useful in scenarios where you need to check for collisions between rectangular objects in a 2D space, and it assumes that the rectangles are axis-aligned.
