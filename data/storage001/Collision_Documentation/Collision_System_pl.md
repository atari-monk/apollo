# System Kolizji

```typescript
import BoxCollider from '../ecs_component/BoxCollider'
import RigidBody from '../ecs_component/RigidBody'
import Transform from '../ecs_component/Transform'
import CollisionObject from '../ecs_component/CollisionObject'
import IVector2 from '../math/IVector2'
import IEntityCache from '../ecs_cache/IEntityCache'
import IEntity from '../ecs_entity/IEntity'
import System from '../ecs_system_core/System'
import ICollisionHandler from './ICollisionHandler'
import CollisionDetector from '../collision_detector/CollisionDetector'
import { ICollision } from '../collision_detector/ICollision'
import ICollisionEntity from '../collision_detector/ICollisionEntity'
import { IRect } from '../collision_detector/IRect'

export default class Collision extends System {
  private _cache = new Map<string, ICollision[]>()

  constructor(
    entityCache: IEntityCache,
    private readonly _collisionDetector: CollisionDetector,
    private readonly _collisionHandlers: Map<string, ICollisionHandler[]>
  ) {
    super(entityCache)
  }

  protected override startEntity(entity: IEntity) {
    const colliders = entity.getComponents(BoxCollider)
    if (!colliders) throw new Error(`No colliders in ${entity.id}`)

    const collisions: ICollision[] = []

    for (const collider of colliders) {
      const handlers = this._collisionHandlers.get(collider.id)
      if (!handlers) continue

      const collision = {
        object1: {} as ICollisionEntity,
        object2: {} as ICollisionEntity,

        rect1: {} as IRect,
        rect2: {} as IRect,

        point1: {} as IVector2,
        point2: {} as IVector2,
      }
      this.setCollision(collision, entity, collider)

      this._collisionDetector.start(collision)

      for (const handler of handlers) {
        this._collisionDetector.subscribe(
          collision,
          handler.onCollisionHandler.bind(handler),
          handler.offCollisionHandler.bind(handler)
        )
      }

      collisions.push(collision)
    }

    this._cache.set(entity.id, collisions)
  }

  private setCollision(
    collision: ICollision,
    entity: IEntity,
    collider: BoxCollider
  ) {
    this.setObject1(collision, entity, collider)
    this.setObject2(collision, entity)
  }

  private setObject1(
    collision: ICollision,
    entity: IEntity,
    collider: BoxCollider
  ) {
    collision.object1 = {
      entityId: entity.id,
      collider,
      rigidBody: entity.getComponentStrict(RigidBody),
      transform: entity.getComponentStrict(Transform),
    }
  }

  private setObject2(collision: ICollision, entity: IEntity) {
    const entity2 = this.getEntity2(entity)
    collision.object2 = {
      entityId: entity2.id,
      collider: entity2.getComponentStrict(BoxCollider),
      rigidBody: entity2.getComponentStrict(RigidBody),
      transform: entity2.getComponentStrict(Transform),
    }
  }

  private getEntity2(entity: IEntity) {
    return this._entityCache.getStrict(
      entity.getComponentStrict(CollisionObject).objectIdToCollideWith
    )
  }

  protected override updateEntity(entity: IEntity, _deltaTime: number): void {
    const collisions = this._cache.get(entity.id)
    if (collisions) {
      for (const collision of collisions) {
        this._collisionDetector.update(collision)
      }
    }
  }

  protected override renderEntity(entity: IEntity, _deltaTime: number): void {
    const collisions = this._cache.get(entity.id)
    if (collisions) {
      for (const collision of collisions) {
        this._collisionDetector.draw(collision)
      }
    }
  }
}
```

<audio controls>
  <source src="./audio_pl/Collision_System.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>
Oto tłumaczenie opisu klasy `Collision` na język polski:

---

### Klasa `Collision`

Klasa `Collision` jest systemem zarządzającym detekcją i obsługą kolizji w architekturze entity-component-system (ECS). Wykorzystuje różne komponenty, takie jak `BoxCollider`, `RigidBody` i `Transform`, do wykrywania i przetwarzania kolizji między obiektami. Poniżej znajduje się szczegółowy opis klasy:

### Przegląd Klasy:

- **Dziedziczenie**: Klasa `Collision` dziedziczy po klasie `System`, która jest kluczową częścią frameworka ECS, co oznacza, że jest odpowiedzialna za zarządzanie zachowaniem obiektów związanych z kolizjami.
- **Zależności**: Wymaga `IEntityCache` (do przechowywania i zarządzania obiektami), `CollisionDetector` (do wykrywania kolizji) oraz mapy obsługiwaczy kolizji (`_collisionHandlers`), które definiują specyficzne reakcje na kolizje dla różnych obiektów.

### Kluczowe Pola:

1. **\_cache (Map<string, ICollision[]>)**:

   - Przechowuje listę obiektów kolizji dla każdego obiektu, używając identyfikatora obiektu jako klucza i listy obiektów `ICollision` jako wartości.
   - Ten cache pozwala na zarządzanie trwającymi kolizjami i unikanie redundantnych obliczeń kolizji.

2. **\_collisionDetector (CollisionDetector)**:

   - Obiekt odpowiedzialny za rzeczywiste wykrywanie kolizji i określanie, czy dwa obiekty mają kolizję.

3. **\_collisionHandlers (Map<string, ICollisionHandler[]>)**:
   - Mapuje identyfikatory obiektów na obsługiwacze kolizji (funkcje określające, co zrobić w przypadku kolizji).
   - Każdy collider ma przypisany zestaw obsługiwaczy, które są wywoływane, gdy detektor kolizji wykryje nakładanie się obiektów.

### Kluczowe Metody:

1. **startEntity(entity: IEntity)**:

   - Wywoływana, gdy system jest inicjowany dla konkretnego obiektu.
   - Pobiera wszystkie komponenty `BoxCollider` obiektu, generuje obiekty kolizji i subskrybuje odpowiednie obsługiwacze kolizji.
   - Każdy obiekt kolizji jest dodawany do `_cache` w celu późniejszego użycia.
   - Ta metoda ustawia wszystkie niezbędne obiekty (`ICollisionEntity`, `IRect`, `IVector2`) do reprezentowania danych kolizji dla dwóch obiektów.

2. **setCollision(collision: ICollision, entity: IEntity, collider: BoxCollider)**:

   - Odpowiada za ustawienie obiektu `ICollision`, który zawiera dwie główne części:
     - `object1`: Obiekt inicjujący kolizję.
     - `object2`: Inny obiekt zaangażowany w kolizję.
   - Wywołuje metody pomocnicze (`setObject1`, `setObject2`), aby skonfigurować te obiekty.

3. **setObject1 / setObject2**:

   - Te metody ustalają dane kolizji dla dwóch obiektów zaangażowanych w kolizję, w tym ich collidery, ciała sztywne i transformacje.

4. **getEntity2(entity: IEntity)**:

   - Pobiera drugi obiekt zaangażowany w kolizję na podstawie referencji przechowywanej w komponencie `CollisionObject` pierwszego obiektu.
   - To wyszukiwanie odbywa się za pośrednictwem `IEntityCache`, co zapewnia dostęp do wszystkich niezbędnych obiektów.

5. **updateEntity(entity: IEntity, \_deltaTime: number)**:

   - Aktualizuje stan kolizji dla obiektu, w zależności od postępu czasu lub zmian w stanie gry.
   - Jest wywoływana w każdym cyklu aktualizacji gry i zapewnia, że detektor kolizji aktualizuje stan kolizji.

6. **renderEntity(entity: IEntity, \_deltaTime: number)**:
   - Używana do wizualizacji lub przetwarzania renderowania kolizji (jeśli jest to potrzebne).
   - Metoda ta rysuje dane dotyczące kolizji za pomocą `CollisionDetector`, co może wizualizować granice kolizji lub związane z nimi informacje.

### Ogólny Przebieg:

- Gdy obiekt zostaje dodany do ECS, system sprawdza, czy ma on `BoxCollider`, ustawia dane kolizji (`ICollision`) i subskrybuje odpowiednie obsługiwacze.
- W trakcie każdej aktualizacji i renderowania, system aktualizuje stan kolizji za pomocą detektora kolizji i wywołuje wizualne informacje zwrotne lub przetwarzanie, jeśli jest to konieczne.

### Przykładowe Użycie:

1. **Konfiguracja Obiektu**: Obiekt z `BoxCollider` i `RigidBody` jest dodawany do ECS. System przygotowuje go do wykrywania kolizji z innymi obiektami.
2. **Wykrywanie Kolizji**: `CollisionDetector` sprawdza, czy ten obiekt koliduje z innym obiektem.
3. **Obsługiwacze Kolizji**: Jeśli wystąpi kolizja, system wywołuje odpowiednie obsługiwacze (np. odbicie, uszkodzenia lub efekty dźwiękowe).
4. **Renderowanie**: Jeśli jest to wymagane, system rysuje granice kolizji do debugowania lub wizualizacji.

Ten projekt jest typowy dla silników fizyki lub gier, gdzie obiekty z colliderami wchodzą w interakcje, a różne obsługiwacze są wywoływane w zależności od kolizji między obiektami.
