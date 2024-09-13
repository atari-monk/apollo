# TopLeftCollision Algorithm

```typescript
import Vector2 from '../math/Vector2'
import { ICollision } from '../collision_detector/ICollision'
import ICollisionAlgorithm from '../collision_detector/ICollisionAlgorithm'
import { IRect } from '../collision_detector/IRect'

export default class TopLeftCollision implements ICollisionAlgorithm {
  private _rect1!: IRect
  private _rect2!: IRect

  start(collision: ICollision) {
    const {
      transform: { position: pos1 },
      collider: { size: size1 },
    } = collision.object1
    const {
      transform: { position: pos2 },
      collider: { size: size2 },
    } = collision.object2

    this._rect1 = {
      position: pos1,
      size: size1,
      halfSize: Vector2.zero,
    }

    this._rect2 = {
      position: pos2,
      size: size2,
      halfSize: Vector2.zero,
    }
  }

  isColliding(_collision: ICollision): boolean {
    const p1 = this._rect1.position
    const p2 = this._rect2.position
    const s1 = this._rect1.size
    const s2 = this._rect2.size
    return (
      p1.x < p2.x + s2.x &&
      p1.x + s1.x > p2.x &&
      p1.y < p2.y + s2.y &&
      p1.y + s1.y > p2.y
    )
  }

  //prettier-ignore
  draw(_collision: ICollision): void {;}
}
```

<audio controls>
  <source src="./audio_en/TopLeftCollision.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>
The `TopLeftCollision` class implements the `ICollisionAlgorithm` interface, which is used for detecting collisions between rectangular objects. Here's a breakdown of its components:

### Components

1. **Properties:**

   - `_rect1` and `_rect2` are private properties that represent the rectangles involved in the collision detection. They are of type `IRect`.

2. **Methods:**

   - **`start(collision: ICollision)`**: Initializes the `_rect1` and `_rect2` properties based on the `collision` object passed as a parameter. It extracts the positions and sizes of the two colliding objects and sets them to `_rect1` and `_rect2`. Note that the `halfSize` property of `IRect` is set to `Vector2.zero` and is not used in the collision logic.

   - **`isColliding(_collision: ICollision): boolean`**: Determines if the two rectangles are colliding. This method uses the axis-aligned bounding box (AABB) collision detection algorithm. It checks if the rectangles overlap by comparing their positions and sizes.

   - **`draw(_collision: ICollision): void`**: This method is a placeholder for drawing the collision or debug information. In this implementation, it does nothing (`;`).

### Usage

- **Initialization**: The `start` method is called to set up the rectangles with their respective positions and sizes. This method must be called before performing collision checks.

- **Collision Check**: The `isColliding` method is used to check if the two rectangles intersect. It returns `true` if there is a collision and `false` otherwise.

- **Drawing**: The `draw` method is currently a no-op but can be used to visualize or debug the collision if needed.

This class is useful in scenarios where you need to check for collisions between rectangular objects in a 2D space, and it assumes that the rectangles are axis-aligned.
