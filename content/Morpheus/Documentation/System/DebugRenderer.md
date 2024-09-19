# DebugRenderer

## Path

- packages\engine\src\ecs_system\DebugRenderer.ts

## Short Description

- Ecs system extending System class.
- Used in football 1.0.0
- For each entity regisered in system:
  - Caches components Transform, Direction, RigidBody, BoxCollider[].
  - It's mapped to entity `debugUI`, action `toggleCollider`, key `i`.
  - Toggles collider enableRender with "pressOnceOnStart" in entity.json
  - Renders box colliders.
  - Renders velocity vector.
  - Renders direction vector.
  - Renders transform.position point.

## Usage

- Add data to entity.json.  
  Also add listed components data to render them.

```json
  "debugUI": {
    "id": "debugUI",
    "name": "debugUI",
    "keyMap": {
      "actions": [
        {
          "action": "toggleCollider",
          "key": "i",
          "pressOnceOnStart": true
        }
      ]
    }
  }
```

-Add system to system.json

```json
{
  "system": "debugRenderer",
  "entity": ["player1"],
  "cache": "rendererCache",
  "name": "Debug Renderer"
}
```
