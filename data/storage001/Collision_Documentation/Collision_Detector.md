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

<iframe src="https://1drv.ms/u/c/37f44e52f80d7972/IQRHChuioIr3QJG3hDB5PM85AeFt3vIUwTNh-vYDHWrlG74" width="300" height="120" frameborder="0" scrolling="no"></iframe>
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

<iframe src="https://1drv.ms/u/c/37f44e52f80d7972/IQQUvEfTMO2QT7qucF4uMCyXAabp4nc9h6h7EEn2pIdPnBA" width="300" height="120" frameborder="0" scrolling="no"></iframe>
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

<iframe src="https://1drv.ms/u/c/37f44e52f80d7972/IQQ9hXiIE7s7SaDMKkI_C44FAcFgnezr36MWD835LrOH_s4" width="300" height="120" frameborder="0" scrolling="no"></iframe>
The `ICollision` interface represents a collision between two entities, `object1` and `object2`, both of type `ICollisionEntity`.  
It also includes two corresponding rectangular bounds, `rect1` and `rect2`, of type `IRect`, which define the areas where the collision occurs.

## ICollisionCallback

```typescript
import { ICollision } from './ICollision'

export default interface ICollisionCallback {
  (collision: ICollision): void
}
```

<iframe src="https://1drv.ms/u/c/37f44e52f80d7972/IQQrpMzmghxwQqpsN8_cB79yAT-g5JbacyMDf59g5T6PQCc" width="300" height="120" frameborder="0" scrolling="no"></iframe>
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

<iframe src="https://1drv.ms/u/c/37f44e52f80d7972/IQQVB155XGEZQpns79x6_mwRARWfYBPCBhdSIW58KZ_9Tzc" width="300" height="120" frameborder="0" scrolling="no"></iframe>
The `ICollisionAlgorithm` interface defines the structure for a collision detection algorithm. It includes three methods:
- `start(collision: ICollision)`: Initializes or processes the start of a collision.
- `isColliding(collision: ICollision)`: Returns a boolean indicating if a collision is occurring.
- `draw(collision: ICollision)`: Visualizes the collision.

This interface provides a framework for managing and evaluating collisions between entities.