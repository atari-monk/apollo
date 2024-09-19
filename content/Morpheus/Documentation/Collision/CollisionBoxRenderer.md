# CollisionBoxRenderer

## Path

- packages\engine\src\ecs_system\CollisionBoxRenderer.ts

## Short Description

- Ecs system extending System class.
- Used in football 2.0.0.
- Caches component CanvasScale in ctor.
- Caches sprite, animator, transform, boxes, spriteOrigin (top left), spriteCenter, boxCenter[], todo: there should be central cache ?
- It's mapped to entity `debugUI`, action `toggleCollider`, key `i` by default.
- Toggles colliders enableRender with "pressOnceOnStart" in entity.json.
- Updates colliders calculation.
- Renders colliders rects.
- Calculates sprite center.
- Calculates collider box center.
- Flag origin.isCenter decides if center or top left is used.
- Renders strokeRect or fillRect, depending on box.style, fill with no style.
- Box center and size is scaled with `CanvalScale`.

## Quirqs

- It switches only colliders with ids: 'body', 'boots', 'kick', 'ball'.
- Box.center is really top left, todo: change names.

## Usage

- Add `style` to collider in entity.json.

```json
"style": {
    "isFill": false,
    "isStroke": true,
    "strokeColor": "black",
    "lineWidth": 2
}
```
