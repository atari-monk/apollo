# BallDribble

## Path

- packages\engine\src\ecs_system\BallDribble.ts

## Short Description

- Ecs system extending System class.
- Used in football 1.0.0.
- Caches Transform, Kick, BoxCollider, todo: there should be central cache ?
- Also caches Transform for ball entity.
- Kick.enableKick is set by collision detection of ball and player collider box with id: `kick`.
- If `Kick.enableKick` springForce is calculated and added to ball Transform.position.
- Stiffness is hardcoded to 0.1, todo: move to component data.

## Usage

- Add to player entity.json

```json
"kick":
{
  "enableKick": false
}
```

- Add to system.json

```json
{
  "system": "ballDribble",
  "entity": ["player1"],
  "cache": "rendererCache",
  "name": "Ball Dribble"
}
```
