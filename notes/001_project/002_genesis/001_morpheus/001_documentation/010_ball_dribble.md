# BallDribble

[Up](index.md)
[Main](../../../../../index.md)

## Responsibility

- Ecs system extending System class.
- Used in football 1.0.0.
- Caches Transform, Kick, BoxCollider, todo: there should be central cache ?
- Also caches Transform for ball entity.
- Kick.enableKick is set by collision detection of ball and player collider box with id: `kick`.
- If `Kick.enableKick` springForce is calculated and added to ball Transform.position.
- Stiffness is hardcoded to 0.1, todo: move to component data.
- Spring is calculated with formula:

```typescript
const displacement = playerTransform.position
  .add(playerCollider.center)
  .subtract(ballTransform.position)
```

## Path

```plaintext
C:\atari-monk\code\ts-engine-nx\packages\engine\src\football\ecs\system\BallDribble.ts
```

## Usage

- Add to system.json

```json
{
  "system": "ballDribble",
  "entity": ["player1"],
  "cache": "rendererCache",
  "name": "Ball Dribble"
}
```

- Add to player entity.json

```json
"kick":
{
  "enableKick": false
}
```

[Up](index.md)
[Main](../../../../../index.md)
