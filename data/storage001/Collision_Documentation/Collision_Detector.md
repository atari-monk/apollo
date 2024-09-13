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

[🔊 En](https://1drv.ms/u/c/37f44e52f80d7972/IQQUvEfTMO2QT7qucF4uMCyXAabp4nc9h6h7EEn2pIdPnBA)  
The `ICollisionEntity` interface defines an entity involved in collision detection and physics. It includes:

1. **entityId**: A unique identifier for the entity.
2. **transform**: Defines the entity’s position, rotation, and scale.
3. **collider**: Represents the entity's collision shape as a box.
4. **rigidBody**: Simulates physical properties like mass and velocity for interaction with the physics system.

This interface integrates components for positioning, collision detection, and physics simulation in a game or simulation system.

[🔊 Pl](https://1drv.ms/u/c/37f44e52f80d7972/IQQ1YOAXBx_TS7RYKORW3_IuAadD943cM_25apf0S2yZvek)  
Interfejs `ICollisionEntity` definiuje jednostkę zaangażowaną w wykrywanie kolizji i fizykę. Zawiera:

1. **entityId**: Unikalny identyfikator jednostki.
2. **transform**: Definiuje pozycję, rotację i skalę jednostki.
3. **collider**: Reprezentuje kształt kolizji jednostki jako pudełko.
4. **rigidBody**: Symuluje właściwości fizyczne, takie jak masa i prędkość, do interakcji z systemem fizyki.

Ten interfejs integruje komponenty do pozycjonowania, wykrywania kolizji i symulacji fizyki w systemie gry lub symulacji.
