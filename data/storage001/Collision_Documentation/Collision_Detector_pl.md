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

<iframe src="https://1drv.ms/u/c/37f44e52f80d7972/IQRZHSi7xMw8TaFcDUCj33rWATEbYX7mqjzMiKqrlaA66D4" width="300" height="120" frameborder="0" scrolling="no"></iframe>
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

<iframe src="https://1drv.ms/u/c/37f44e52f80d7972/IQRqygCAPZ3nQ75raB5yAvfhAZodjLzD1-q_XTeJvdlVqxw" width="300" height="120" frameborder="0" scrolling="no"></iframe>
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

<iframe src="https://1drv.ms/u/c/37f44e52f80d7972/IQTX4YTF1Ef3S5QVPF9wPK53AW0x30mMp_XhfMr5ksT812E" width="300" height="120" frameborder="0" scrolling="no"></iframe>
Interfejs `ICollision` reprezentuje kolizję między dwoma obiektami, `object1` i `object2`, które są typu `ICollisionEntity`.  
Zawiera również dwa odpowiadające prostokątne obszary, `rect1` i `rect2`, typu `IRect`, które definiują miejsca, gdzie dochodzi do kolizji.

## ICollisionCallback

```typescript
import { ICollision } from './ICollision'

export default interface ICollisionCallback {
  (collision: ICollision): void
}
```

<iframe src="https://1drv.ms/u/c/37f44e52f80d7972/IQRUHHC6AKsVSaVhtkmRrnJ_AZS8jt6upBuOn9riIMS5JDU" width="300" height="120" frameborder="0" scrolling="no"></iframe>
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

<iframe src="https://1drv.ms/u/c/37f44e52f80d7972/IQSYLJHco841TaK22tO3g4TGARyL0w1iPtnq8pr9_d1TUS4" width="300" height="120" frameborder="0" scrolling="no"></iframe>
Interfejs `ICollisionAlgorithm` definiuje strukturę algorytmu wykrywania kolizji. Zawiera trzy metody:
- `start(collision: ICollision)`: Inicjuje lub przetwarza początek kolizji.
- `isColliding(collision: ICollision)`: Zwraca wartość logiczną, która wskazuje, czy kolizja ma miejsce.
- `draw(collision: ICollision)`: Wizualizuje kolizję.

Ten interfejs zapewnia ramy do zarządzania i oceny kolizji między obiektami.