# MarkersRendererWithScaling

[Up](index.md)
[Main](../../../../../index.md)

# Responsibility

-   Ecs system extending System class.
-   Used in football 2.0.0
-   For each entity regisered in system:
    -   Renders points: sprite center, collider box center and it's mirror along sprite center.
    -   All points are scaled with `CanvasScale` in canvas resize events.
    -   Caches components Transform, Sprite, BoxCollider, Direction, MarkerPoints.
    -   It's mapped to entity `debugUI`, action `toggleMarkers`, key `u`.
    -   Toggles markerPoints enableRender with "pressOnceOnStart" in entity.json
    -   Updates markers calculation.
    -   Renders markers points.

# Path

```bash
   C:\atari-monk\code\ts-engine-nx\packages\engine\src\ecs\system\renderer\MarkersRenderer.ts
```

# Usage

-   Add data to entity.json.  
    Also add listed components data to render them.

```json
  "debugUI": {
    "id": "debugUI",
    "name": "debugUI",
    "keyMap": {
      "actions": [
        {
          "action": "toggleMarkers",
          "key": "u",
          "pressOnceOnStart": true
        },
      ]
    }
  }
```

-Add system to system.json

```json
{
    "system": "markersV2",
    "entity": ["player1"],
    "cache": "rendererCache",
    "name": "Markers Renderer V2"
}
```

[Up](index.md)
[Main](../../../../../index.md)
