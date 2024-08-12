# MarkersRenderer

[Up](index.md)
[Main](../../../../../index.md)

-   C:\atari-monk\code\ts-engine-nx\packages\engine\src\ecs\system\renderer\MarkersRenderer.ts
-   Ecs system extending System class.
-   Used in football 1.0.0
-   For each entity regisered in system:
    -   Caches components Transform, BoxCollider, Direction, MarkerPoints.
    -   It's mapped to entity `debugUI`, action `toggleMarkers`, key `u`.
    -   Toggles markerPoints enableRender with "pressOnceOnStart" in entity.json
    -   Updates markers calculation.
    -   Renders markers points.

#### Usage

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
    "system": "markers",
    "entity": ["player1"],
    "cache": "rendererCache",
    "name": "Markers Renderer"
}
```

[Up](index.md)
[Main](../../../../../index.md)
