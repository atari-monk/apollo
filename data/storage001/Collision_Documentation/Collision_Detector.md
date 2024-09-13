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

<audio controls>
  <source src="https://1drv.ms/u/c/37f44e52f80d7972/ERS8R9Mw7ZBPuq5wXi4wLJcB8fTnMe6xeZrFEkA8NnzhSA?e=og0h1T" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>
