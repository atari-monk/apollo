# Collision Detector

```typescript
import IVector2 from '../math/IVector2'

export interface IRect {
  position: IVector2
  size: IVector2
  halfSize: IVector2
}
```

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

[ICollisionEntity]('https://1drv.ms/u/c/37f44e52f80d7972/IQQUvEfTMO2QT7qucF4uMCyXAbkhsAJuKD0bRiVY1vp8New')
