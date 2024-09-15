# collision_detector

```typescript
import Vector2 from '../math/Vector2'
import { ICollision } from './ICollision'
import ICollisionAlgorithm from './ICollisionAlgorithm'
import { IRect } from './IRect'

export default class TopLeftCollision implements ICollisionAlgorithm {
  //prettier-ignore
  draw(): void {;}
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

  isColliding(): boolean {
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
}
```

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

```typescript
import { ICollision } from './ICollision'

export default interface ICollisionCallback {
  (collision: ICollision): void
}
```

```typescript
import { ICollision } from './ICollision'

export default interface ICollisionAlgorithm {
  start(collision: ICollision): void
  isColliding(collision: ICollision): boolean
  draw(collision: ICollision): void
}
```

```typescript
import IVector2 from '../math/IVector2'
import ICollisionEntity from './ICollisionEntity'
import { IRect } from './IRect'

export interface ICollision {
  object1: ICollisionEntity
  object2: ICollisionEntity

  rect1: IRect
  rect2: IRect

  point1: IVector2
  point2: IVector2
}
```

```typescript
import { ICollision } from './ICollision'
import ICollisionAlgorithm from './ICollisionAlgorithm'
import ICollisionCallback from './ICollisionCallback'

export default class CollisionDetector {
  private _collisionCallbacks: Map<string, ICollisionCallback> = new Map()
  private _noCollisionCallbacks: Map<string, ICollisionCallback> = new Map()

  constructor(private readonly _collisionAlgorithm: ICollisionAlgorithm) {}

  start(collision: ICollision): void {
    this._collisionAlgorithm.start(collision)
  }

  private getCollisionKey(collision: ICollision): string {
    const id1 = collision.object1.entityId
    const cid1 = collision.object1.collider.id
    const id2 = collision.object2.entityId

    const key = cid1 ? `${id1}_${cid1}_${id2}` : `${id1}_${id2}`

    return key
  }

  update(collision: ICollision) {
    const isColliding = this._collisionAlgorithm.isColliding(collision)

    const key = this.getCollisionKey(collision)

    if (isColliding) {
      const callback = this._collisionCallbacks.get(key)
      if (callback) {
        callback(collision)
      }
    } else {
      const callback = this._noCollisionCallbacks.get(key)
      if (callback) {
        callback(collision)
      }
    }
  }

  subscribe(
    collision: ICollision,
    collisionCallback: ICollisionCallback,
    noCollisionCallback: ICollisionCallback
  ): void {
    const key = this.getCollisionKey(collision)
    this._collisionCallbacks.set(key, collisionCallback)
    this._noCollisionCallbacks.set(key, noCollisionCallback)
  }

  draw(collision: ICollision) {
    this._collisionAlgorithm.draw(collision)
  }
}
```

```typescript
import IEventSystem from '../event_system/IEventSystem'
import IVector2 from '../math/IVector2'
import Vector2 from '../math/Vector2'
import IRenderer from '../renderer/IRenderer'
import { ICollision } from './ICollision'
import ICollisionAlgorithm from './ICollisionAlgorithm'
import { IRect } from './IRect'

export default class CenterCollisionV1 implements ICollisionAlgorithm {
  private _ctx: CanvasRenderingContext2D

  constructor(
    private readonly _eventSystem: IEventSystem,
    private readonly _renderer: IRenderer,
    private readonly _isDebugMode = false
  ) {
    this._ctx = this._renderer.ctx
  }

  start(collision: ICollision) {
    const updateCallback = () => {
      this.calculateData(collision)
    }

    this._eventSystem.subscribe(
      `${collision.object1.entityId}_updateCenter`,
      updateCallback
    )

    updateCallback()
  }

  private calculateData(collision: ICollision) {
    const { position: position1 } = collision.object1.transform
    const { position: position2 } = collision.object2.transform
    const {
      halfSize: halfSize1,
      center: center1,
      size: size1,
    } = collision.object1.collider
    const {
      halfSize: halfSize2,
      center: center2,
      size: size2,
    } = collision.object2.collider

    const point1 = new Vector2(center1.x - halfSize1.x, center1.y - halfSize1.y)
    const point2 = new Vector2(center2.x - halfSize2.x, center2.y - halfSize2.y)

    const rect1 = this.createRect(position1, point1, size1)
    const rect2 = this.createRect(position2, point2, size2)

    return {
      ...collision,
      rect1,
      rect2,
      point1,
      point2,
    }
  }

  private createRect(
    position: IVector2,
    point: IVector2,
    size: IVector2
  ): IRect {
    const rect: IRect = {} as IRect

    rect.position = new Vector2(position.x + point.x, position.y + point.y)

    rect.size = new Vector2(size.x, size.y)

    return rect
  }

  private updatePoints(collision: ICollision) {
    const p1 = collision.object1.transform.position
    const p2 = collision.object2.transform.position

    this.updatePosition(collision.rect1, p1, collision.point1)
    this.updatePosition(collision.rect2, p2, collision.point2)
  }

  private updatePosition(rect: IRect, pos: IVector2, point: IVector2) {
    rect.position.x = pos.x + point.x
    rect.position.y = pos.y + point.y
  }

  isColliding(collision: ICollision) {
    const updColl = this.calculateData(collision)
    this.updatePoints(updColl)
    collision.rect1 = updColl.rect1
    collision.rect2 = updColl.rect2
    return (
      updColl.rect1.position.x <
        updColl.rect2.position.x + updColl.rect2.size.x &&
      updColl.rect1.position.x + updColl.rect1.size.x >
        updColl.rect2.position.x &&
      updColl.rect1.position.y <
        updColl.rect2.position.y + updColl.rect2.size.y &&
      updColl.rect1.position.y + updColl.rect1.size.y > updColl.rect2.position.y
    )
  }

  draw(collision: ICollision) {
    if (!this._isDebugMode) return
    const { rect1, rect2 } = collision
    this._ctx.fillStyle = 'white'
    if (!rect1.position) return
    this._ctx.fillRect(
      rect1.position.x,
      rect1.position.y,
      rect1.size.x,
      rect1.size.y
    )
    this._ctx.fillStyle = 'yellow'
    this._ctx.fillRect(
      rect2.position.x,
      rect2.position.y,
      rect2.size.x,
      rect2.size.y
    )
  }
}
```

```typescript
import IEntityCache from '../ecs_cache/IEntityCache'
import CanvasScale from '../ecs_component/CanvasScale'
import IEventSystem from '../event_system/IEventSystem'
import IVector2 from '../math/IVector2'
import Vector2 from '../math/Vector2'
import IRenderer from '../renderer/IRenderer'
import { ICollision } from './ICollision'
import ICollisionAlgorithm from './ICollisionAlgorithm'
import { IRect } from './IRect'

export default class CenterCollisionV2 implements ICollisionAlgorithm {
  private _ctx: CanvasRenderingContext2D
  private _canvasScale: CanvasScale

  constructor(
    private readonly _eventSystem: IEventSystem,
    private readonly _entityCache: IEntityCache,
    private readonly _renderer: IRenderer,
    private readonly _isDebugMode = false
  ) {
    this._ctx = this._renderer.ctx
    this._canvasScale = this.getCanvasScale()
  }

  private getCanvasScale() {
    const canvasEntity = this._entityCache.getStrict('canvas')
    const canvasScale = canvasEntity.getComponentStrict(CanvasScale)
    return canvasScale
  }

  start(collision: ICollision) {
    const updateCallback = () => {
      this.calculateData(collision)
    }

    this._eventSystem.subscribe(
      `${collision.object1.entityId}_updateCenter`,
      updateCallback
    )

    updateCallback()
  }

  private calculateData(collision: ICollision) {
    const { scaleFactor: scale } = this._canvasScale
    const { position: position1 } = collision.object1.transform
    const { position: position2 } = collision.object2.transform
    const {
      halfSize: collisionBoxHalfSize1,
      center: collisionBoxTopLeft1,
      size: collisionBoxSize1,
    } = collision.object1.collider
    const {
      halfSize: collisionBoxHalfSize2,
      center: collisionBoxTopLeft2,
      size: collisionBoxSize2,
    } = collision.object2.collider

    //const boxCenterX = spriteCenterX + (box.center.x - box.size.x / 2) * scale.x

    const collisionBoxCenter1 = new Vector2(
      collisionBoxTopLeft1.x - collisionBoxHalfSize1.x,
      collisionBoxTopLeft1.y - collisionBoxHalfSize1.y
    )
    const collisionBoxCenter2 = new Vector2(
      collisionBoxTopLeft2.x - collisionBoxHalfSize2.x,
      collisionBoxTopLeft2.y - collisionBoxHalfSize2.y
    )

    const spriteCenter1 = new Vector2()
    spriteCenter1.x = position1.x + 40
    spriteCenter1.y = position1.y + 80

    const spriteCenter2 = new Vector2()
    spriteCenter2.x = position2.x + 40
    spriteCenter2.y = position2.y + 20

    const rect1 = this.createRect(
      spriteCenter1,
      collisionBoxCenter1,
      collisionBoxSize1
    )
    const rect2 = this.createRect(
      spriteCenter2,
      collisionBoxCenter2,
      collisionBoxSize2
    )

    return {
      ...collision,
      rect1,
      rect2,
      point1: collisionBoxTopLeft1,
      point2: collisionBoxTopLeft2,
    }
  }

  private createRect(
    position: IVector2,
    point: IVector2,
    size: IVector2
  ): IRect {
    const rect: IRect = {} as IRect
    const { scaleFactor: scale } = this._canvasScale

    rect.position = new Vector2(
      (position.x + point.x) * scale.x,
      (position.y + point.y) * scale.y
    )

    rect.size = new Vector2(size.x * scale.x, size.y * scale.y)

    return rect
  }

  private updatePoints(collision: ICollision) {
    const p1 = collision.object1.transform.position.add(new Vector2(40, 80))
    const p2 = collision.object2.transform.position.add(new Vector2(40, 20))

    this.updatePosition(
      collision.rect1,
      p1,
      collision.point1,
      collision.object1.collider.halfSize
    )
    this.updatePosition(
      collision.rect2,
      p2,
      collision.point2,
      collision.object2.collider.halfSize
    )
  }

  private updatePosition(
    rect: IRect,
    spriteCenter: IVector2,
    boxCenter: IVector2,
    boxHalfSize: IVector2
  ) {
    const { scaleFactor: scale } = this._canvasScale
    rect.position.x = (spriteCenter.x + boxCenter.x - boxHalfSize.x) * scale.x
    rect.position.y = (spriteCenter.y + boxCenter.y - boxHalfSize.y) * scale.y
  }

  isColliding(collision: ICollision) {
    const updColl = this.calculateData(collision)
    this.updatePoints(updColl)
    collision.rect1 = updColl.rect1
    collision.rect2 = updColl.rect2
    return (
      updColl.rect1.position.x <
        updColl.rect2.position.x + updColl.rect2.size.x &&
      updColl.rect1.position.x + updColl.rect1.size.x >
        updColl.rect2.position.x &&
      updColl.rect1.position.y <
        updColl.rect2.position.y + updColl.rect2.size.y &&
      updColl.rect1.position.y + updColl.rect1.size.y > updColl.rect2.position.y
    )
  }

  draw(collision: ICollision) {
    if (!this._isDebugMode) return
    const { rect1, rect2 } = collision
    this._ctx.fillStyle = 'white'
    if (!rect1.position) return
    this._ctx.fillRect(
      rect1.position.x,
      rect1.position.y,
      rect1.size.x,
      rect1.size.y
    )
    this._ctx.fillStyle = 'white'
    this._ctx.fillRect(
      rect2.position.x,
      rect2.position.y,
      rect2.size.x,
      rect2.size.y
    )

    // this.drawSpriteTopLeftUnscaled(collision)
    // this.drawSpriteTopLeftScaled(collision)
    // this.drawSpriteCenterScaled(collision)
    // this.drawCollisionBoxCenter(collision)
  }

  private drawSpriteTopLeftUnscaled(collision: ICollision) {
    const { position: position1 } = collision.object1.transform
    const { position: position2 } = collision.object2.transform

    this._ctx.fillStyle = 'green'
    this._ctx.beginPath()
    this._ctx.arc(position1.x, position1.y, 5, 0, 2 * Math.PI)
    this._ctx.fill()

    this._ctx.fillStyle = 'green'
    this._ctx.beginPath()
    this._ctx.arc(position2.x, position2.y, 5, 0, 2 * Math.PI)
    this._ctx.fill()
  }

  private drawSpriteTopLeftScaled(collision: ICollision) {
    const { scaleFactor: scale } = this._canvasScale
    const { position: position1 } = collision.object1.transform
    const { position: position2 } = collision.object2.transform

    this._ctx.fillStyle = 'red'
    this._ctx.beginPath()
    this._ctx.arc(
      position1.x * scale.x,
      position1.y * scale.y,
      2,
      0,
      2 * Math.PI
    )
    this._ctx.fill()

    this._ctx.fillStyle = 'red'
    this._ctx.beginPath()
    this._ctx.arc(
      position2.x * scale.x,
      position2.y * scale.y,
      2,
      0,
      2 * Math.PI
    )
    this._ctx.fill()
  }

  private drawSpriteCenterScaled(collision: ICollision) {
    const { scaleFactor: scale } = this._canvasScale
    const { position: position1 } = collision.object1.transform
    const { position: position2 } = collision.object2.transform
    const { halfSize: halfSize1 } = collision.object1.collider
    const { halfSize: halfSize2 } = collision.object2.collider

    const center1 = new Vector2(
      (position1.x + 40) * scale.x,
      (position1.y + 80) * scale.y
    )
    const center2 = new Vector2(
      (position2.x + 40) * scale.x,
      (position2.y + 20) * scale.y
    )

    this._ctx.fillStyle = 'red'
    this._ctx.beginPath()
    this._ctx.arc(center1.x, center1.y, 2, 0, 2 * Math.PI)
    this._ctx.fill()

    this._ctx.fillStyle = 'red'
    this._ctx.beginPath()
    this._ctx.arc(center2.x, center2.y, 2, 0, 2 * Math.PI)
    this._ctx.fill()
  }

  private drawCollisionBoxCenter(collision: ICollision) {
    const { scaleFactor: scale } = this._canvasScale
    const { position: position1 } = collision.object1.transform
    const { position: position2 } = collision.object2.transform
    const { halfSize: halfSize1, center: topLeft1 } = collision.object1.collider
    const { halfSize: halfSize2, center: topLeft2 } = collision.object2.collider

    //const boxCenterX = spriteCenterX + (box.center.x - box.size.x / 2) * scale.x
    const center1 = new Vector2(
      (position1.x + 40 + topLeft1.x - halfSize1.x) * scale.x,
      (position1.y + 80 + topLeft1.y - halfSize1.y) * scale.y
    )
    const center2 = new Vector2(
      (position2.x + 40 + topLeft2.x - halfSize2.x) * scale.x,
      (position2.y + 20 + topLeft2.y - halfSize2.y) * scale.y
    )

    this._ctx.fillStyle = 'red'
    this._ctx.beginPath()
    this._ctx.arc(center1.x, center1.y, 5, 0, 2 * Math.PI)
    this._ctx.fill()

    this._ctx.fillStyle = 'blue'
    this._ctx.beginPath()
    this._ctx.arc(center2.x, center2.y, 5, 0, 2 * Math.PI)
    this._ctx.fill()
  }
}
```

```typescript
import IEntityCache from '../ecs_cache/IEntityCache'
import CanvasScale from '../ecs_component/CanvasScale'
import IEventSystem from '../event_system/IEventSystem'
import IVector2 from '../math/IVector2'
import Vector2 from '../math/Vector2'
import IRenderer from '../renderer/IRenderer'
import { ICollision } from './ICollision'
import ICollisionAlgorithm from './ICollisionAlgorithm'
import { IRect } from './IRect'

export default class CenterCollisionV3 implements ICollisionAlgorithm {
  private _ctx: CanvasRenderingContext2D
  private _canvasScale: CanvasScale

  constructor(
    private readonly _eventSystem: IEventSystem,
    private readonly _entityCache: IEntityCache,
    private readonly _renderer: IRenderer,
    private readonly _isDebugMode = false
  ) {
    this._ctx = this._renderer.ctx
    this._canvasScale = this.getCanvasScale()
  }

  private getCanvasScale() {
    const canvasEntity = this._entityCache.getStrict('canvas')
    const canvasScale = canvasEntity.getComponentStrict(CanvasScale)
    return canvasScale
  }

  start(collision: ICollision) {
    const updateCallback = () => {
      this.calculateData(collision)
    }

    this._eventSystem.subscribe(
      `${collision.object1.entityId}_updateCenter`,
      updateCallback
    )

    updateCallback()
  }

  private calculateData(collision: ICollision) {
    const { scaleFactor: scale } = this._canvasScale
    const { position: position1 } = collision.object1.transform
    const { position: position2 } = collision.object2.transform
    const {
      halfSize: collisionBoxHalfSize1,
      center: collisionBoxTopLeft1,
      size: collisionBoxSize1,
    } = collision.object1.collider
    const {
      halfSize: collisionBoxHalfSize2,
      center: collisionBoxTopLeft2,
      size: collisionBoxSize2,
    } = collision.object2.collider

    //const boxCenterX = spriteCenterX + (box.center.x - box.size.x / 2) * scale.x

    const collisionBoxCenter1 = new Vector2(
      collisionBoxTopLeft1.x - collisionBoxHalfSize1.x,
      collisionBoxTopLeft1.y - collisionBoxHalfSize1.y
    )
    const collisionBoxCenter2 = new Vector2(
      collisionBoxTopLeft2.x - collisionBoxHalfSize2.x,
      collisionBoxTopLeft2.y - collisionBoxHalfSize2.y
    )

    const spriteCenter1 = new Vector2()
    spriteCenter1.x = position1.x //+ 40
    spriteCenter1.y = position1.y //+ 80

    const spriteCenter2 = new Vector2()
    spriteCenter2.x = position2.x //+ 40
    spriteCenter2.y = position2.y //+ 20

    const rect1 = this.createRect(
      spriteCenter1,
      collisionBoxCenter1,
      collisionBoxSize1
    )
    const rect2 = this.createRect(
      spriteCenter2,
      collisionBoxCenter2,
      collisionBoxSize2
    )

    return {
      ...collision,
      rect1,
      rect2,
      point1: collisionBoxTopLeft1,
      point2: collisionBoxTopLeft2,
    }
  }

  private createRect(
    position: IVector2,
    point: IVector2,
    size: IVector2
  ): IRect {
    const rect: IRect = {} as IRect
    const { scaleFactor: scale } = this._canvasScale

    rect.position = new Vector2(
      (position.x + point.x) * scale.x,
      (position.y + point.y) * scale.y
    )

    rect.size = new Vector2(size.x * scale.x, size.y * scale.y)

    return rect
  }

  private updatePoints(collision: ICollision) {
    const p1 = collision.object1.transform.position //.add(new Vector2(40, 80))
    const p2 = collision.object2.transform.position //.add(new Vector2(40, 20))

    this.updatePosition(
      collision.rect1,
      p1,
      collision.point1,
      collision.object1.collider.halfSize
    )
    this.updatePosition(
      collision.rect2,
      p2,
      collision.point2,
      collision.object2.collider.halfSize
    )
  }

  private updatePosition(
    rect: IRect,
    spriteCenter: IVector2,
    boxCenter: IVector2,
    boxHalfSize: IVector2
  ) {
    const { scaleFactor: scale } = this._canvasScale
    rect.position.x = (spriteCenter.x + boxCenter.x - boxHalfSize.x) * scale.x
    rect.position.y = (spriteCenter.y + boxCenter.y - boxHalfSize.y) * scale.y
  }

  isColliding(collision: ICollision) {
    const updColl = this.calculateData(collision)
    this.updatePoints(updColl)
    collision.rect1 = updColl.rect1
    collision.rect2 = updColl.rect2
    return (
      updColl.rect1.position.x <
        updColl.rect2.position.x + updColl.rect2.size.x &&
      updColl.rect1.position.x + updColl.rect1.size.x >
        updColl.rect2.position.x &&
      updColl.rect1.position.y <
        updColl.rect2.position.y + updColl.rect2.size.y &&
      updColl.rect1.position.y + updColl.rect1.size.y > updColl.rect2.position.y
    )
  }

  draw(collision: ICollision) {
    if (!this._isDebugMode) return
    const { rect1, rect2 } = collision
    this._ctx.fillStyle = 'white'
    if (!rect1.position) return
    this._ctx.fillRect(
      rect1.position.x,
      rect1.position.y,
      rect1.size.x,
      rect1.size.y
    )
    this._ctx.fillStyle = 'white'
    this._ctx.fillRect(
      rect2.position.x,
      rect2.position.y,
      rect2.size.x,
      rect2.size.y
    )

    // this.drawSpriteTopLeftUnscaled(collision)
    // this.drawSpriteTopLeftScaled(collision)
    // this.drawSpriteCenterScaled(collision)
    // this.drawCollisionBoxCenter(collision)
  }

  private drawSpriteTopLeftUnscaled(collision: ICollision) {
    const { position: position1 } = collision.object1.transform
    const { position: position2 } = collision.object2.transform

    this._ctx.fillStyle = 'green'
    this._ctx.beginPath()
    this._ctx.arc(position1.x, position1.y, 5, 0, 2 * Math.PI)
    this._ctx.fill()

    this._ctx.fillStyle = 'green'
    this._ctx.beginPath()
    this._ctx.arc(position2.x, position2.y, 5, 0, 2 * Math.PI)
    this._ctx.fill()
  }

  private drawSpriteTopLeftScaled(collision: ICollision) {
    const { scaleFactor: scale } = this._canvasScale
    const { position: position1 } = collision.object1.transform
    const { position: position2 } = collision.object2.transform

    this._ctx.fillStyle = 'red'
    this._ctx.beginPath()
    this._ctx.arc(
      position1.x * scale.x,
      position1.y * scale.y,
      2,
      0,
      2 * Math.PI
    )
    this._ctx.fill()

    this._ctx.fillStyle = 'red'
    this._ctx.beginPath()
    this._ctx.arc(
      position2.x * scale.x,
      position2.y * scale.y,
      2,
      0,
      2 * Math.PI
    )
    this._ctx.fill()
  }

  private drawSpriteCenterScaled(collision: ICollision) {
    const { scaleFactor: scale } = this._canvasScale
    const { position: position1 } = collision.object1.transform
    const { position: position2 } = collision.object2.transform
    const { halfSize: halfSize1 } = collision.object1.collider
    const { halfSize: halfSize2 } = collision.object2.collider

    const center1 = new Vector2(
      (position1.x + 40) * scale.x,
      (position1.y + 80) * scale.y
    )
    const center2 = new Vector2(
      (position2.x + 40) * scale.x,
      (position2.y + 20) * scale.y
    )

    this._ctx.fillStyle = 'red'
    this._ctx.beginPath()
    this._ctx.arc(center1.x, center1.y, 2, 0, 2 * Math.PI)
    this._ctx.fill()

    this._ctx.fillStyle = 'red'
    this._ctx.beginPath()
    this._ctx.arc(center2.x, center2.y, 2, 0, 2 * Math.PI)
    this._ctx.fill()
  }

  private drawCollisionBoxCenter(collision: ICollision) {
    const { scaleFactor: scale } = this._canvasScale
    const { position: position1 } = collision.object1.transform
    const { position: position2 } = collision.object2.transform
    const { halfSize: halfSize1, center: topLeft1 } = collision.object1.collider
    const { halfSize: halfSize2, center: topLeft2 } = collision.object2.collider

    //const boxCenterX = spriteCenterX + (box.center.x - box.size.x / 2) * scale.x
    const center1 = new Vector2(
      (position1.x + 40 + topLeft1.x - halfSize1.x) * scale.x,
      (position1.y + 80 + topLeft1.y - halfSize1.y) * scale.y
    )
    const center2 = new Vector2(
      (position2.x + 40 + topLeft2.x - halfSize2.x) * scale.x,
      (position2.y + 20 + topLeft2.y - halfSize2.y) * scale.y
    )

    this._ctx.fillStyle = 'red'
    this._ctx.beginPath()
    this._ctx.arc(center1.x, center1.y, 5, 0, 2 * Math.PI)
    this._ctx.fill()

    this._ctx.fillStyle = 'blue'
    this._ctx.beginPath()
    this._ctx.arc(center2.x, center2.y, 5, 0, 2 * Math.PI)
    this._ctx.fill()
  }
}
```

```typescript
import IEntityCache from '../ecs_cache/IEntityCache'
import CanvasScale from '../ecs_component/CanvasScale'
import Vector2 from '../math/Vector2'
import { IRectOptions } from '../renderer/IPointOptions'
import IRenderer from '../renderer/IRenderer'
import { ICollision } from './ICollision'
import ICollisionAlgorithm from './ICollisionAlgorithm'
import { IRect } from './IRect'

//position is in center of collision box
export default class CollisionDetectionV4 implements ICollisionAlgorithm {
  private _rect1!: IRect
  private _rect2!: IRect
  private _ctx: CanvasRenderingContext2D
  private _canvasScale: CanvasScale

  constructor(
    private readonly _entityCache: IEntityCache,
    private readonly _renderer: IRenderer,
    private readonly _isDebugMode = false
  ) {
    this._ctx = this._renderer.ctx
    this._canvasScale = this.getCanvasScale()
  }

  private getCanvasScale() {
    const canvasEntity = this._entityCache.getStrict('canvas')
    const canvasScale = canvasEntity.getComponentStrict(CanvasScale)
    return canvasScale
  }

  start(collision: ICollision) {
    const {
      transform: { position: pos1 },
      collider: { size: size1, halfSize: halfSize1, center: center1 },
    } = collision.object1
    const {
      transform: { position: pos2 },
      collider: { size: size2, halfSize: halfSize2, center: center2 },
    } = collision.object2

    this._rect1 = {
      position: pos1.add(center1),
      size: size1,
      halfSize: halfSize1,
    }

    this._rect2 = {
      position: pos2.add(center2),
      size: size2,
      halfSize: halfSize2,
    }
  }

  isColliding(): boolean {
    const p1 = this._rect1.position
    const p2 = this._rect2.position
    const s1 = this._rect1.halfSize
    const s2 = this._rect2.halfSize
    return (
      p1.x - s1.x < p2.x + s2.x &&
      p1.x + s1.x > p2.x - s2.x &&
      p1.y - s1.y < p2.y + s2.y &&
      p1.y + s1.y > p2.y - s2.y
    )
  }

  draw(collision: ICollision) {
    if (!this._isDebugMode) return
    this.start(collision)
    if (!this._rect1.position) return
    this._renderer.fillCenteredRectScaling(
      this._rect1.position,
      this._rect1.size,
      this._rect1.halfSize,
      this._canvasScale.scaleFactor,
      Vector2.one,
      { fillColor: 'red' } as IRectOptions
    )
    this._renderer.fillCenteredRectScaling(
      this._rect2.position,
      this._rect2.size,
      this._rect2.halfSize,
      this._canvasScale.scaleFactor,
      Vector2.one,
      { fillColor: 'blue' } as IRectOptions
    )
  }
}
```
