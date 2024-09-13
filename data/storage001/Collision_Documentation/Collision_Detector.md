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

<iframe src="https://1drv.ms/u/c/37f44e52f80d7972/IQTLqMF1XK1GRqImvPbh4D4yAXd2RUO6lpSNw7EgIdI4oyI" width="300" height="120" frameborder="0" scrolling="no"></iframe>
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
