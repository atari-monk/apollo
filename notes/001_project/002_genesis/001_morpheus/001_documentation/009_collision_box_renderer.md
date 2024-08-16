# CollisionBoxRenderer

[Up](index.md)
[Main](../../../../../index.md)

## Responsibility

- Ecs system extending System class.
- Used in football 2.0.0.
- Caches component CanvasScale in ctor.
- Caches sprite, animator, transform, boxes, spriteOrigin (top left), spriteCenter, boxCenter[], todo: there should be central cache ?
- It's mapped to entity `debugUI`, action `toggleCollider`, key `i` by default.
- Toggles colliders enableRender with "pressOnceOnStart" in entity.json.
- Updates colliders calculation.
- Renders colliders rects.
- Calculates sprite center.

```typescript
const spriteCenterX = (transform.position.x + halfFrameSizeX) * scale.x
```

- Calculates collider box center.

```typescript
const boxCenterX = spriteCenterX + (box.center.x - box.size.x / 2) * scale.x
```

- Flag origin.isCenter decides if center or top left is used.
- Renders strokeRect or fillRect, depending on box.style, fill with no style.
- Box center and size is scaled with `CanvalScale`.

## Quirqs

- It switches only colliders with ids: 'body', 'boots', 'kick', 'ball'.
- Box.center is really top left, todo: change names.

## Path

```plaintext
C:\atari-monk\code\ts-engine-nx\packages\engine\src\animation_system\ecs\system\sprite_renderer\CollisionBoxRenderer.ts
```

## Usage

- Add `origin` and `style` to collider in entity.json.

```json
"origin": {
        "isTopLeft": false,
        "isCenter": true
    },
"style": {
    "isFill": false,
    "isStroke": true,
    "strokeColor": "black",
    "lineWidth": 2
}
```

[Up](index.md)
[Main](../../../../../index.md)
