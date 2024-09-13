# Detektor Kolizji

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
Interfejs `IRect` opisuje prostokąt z:

1. **position**: Współrzędne lokalizacji prostokąta.
2. **size**: Szerokość i wysokość prostokąta.
3. **halfSize**: Połowa szerokości i wysokości prostokąta.

Zapewnia strukturę do obsługi prostokątów 2D, w tym ich położenia, wymiarów i granic.

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
Interfejs `ICollisionEntity` definiuje jednostkę zaangażowaną w wykrywanie kolizji i fizykę. Zawiera:

1. **entityId**: Unikalny identyfikator jednostki.
2. **transform**: Definiuje pozycję, rotację i skalę jednostki.
3. **collider**: Reprezentuje kształt kolizji jednostki jako pudełko.
4. **rigidBody**: Symuluje właściwości fizyczne, takie jak masa i prędkość, do interakcji z systemem fizyki.

Ten interfejs integruje komponenty do pozycjonowania, wykrywania kolizji i symulacji fizyki w systemie gry lub symulacji.

## ICollision

```
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
Interfejs `ICollision` reprezentuje kolizję między dwoma obiektami, `object1` i `object2`, które są typu `ICollisionEntity`.  
Zawiera również dwa odpowiadające prostokątne obszary, `rect1` i `rect2`, typu `IRect`, które definiują miejsca, gdzie dochodzi do kolizji.

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
Interfejs `ICollisionCallback` definiuje funkcję, która przyjmuje obiekt typu `ICollision` jako parametr i zwraca `void`.  
Służy jako callback do obsługi zdarzeń kolizji między dwoma obiektami.

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
Interfejs `ICollisionAlgorithm` definiuje strukturę algorytmu wykrywania kolizji. Zawiera trzy metody:
- `start(collision: ICollision)`: Inicjuje lub przetwarza początek kolizji.
- `isColliding(collision: ICollision)`: Zwraca wartość logiczną, która wskazuje, czy kolizja ma miejsce.
- `draw(collision: ICollision)`: Wizualizuje kolizję.

Ten interfejs zapewnia ramy do zarządzania i oceny kolizji między obiektami.
