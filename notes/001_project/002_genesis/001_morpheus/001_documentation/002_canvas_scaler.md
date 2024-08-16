# CanvasScaler

[Up](index.md)
[Main](../../../../../index.md)

-   C:\atari-monk\code\ts-engine-nx\packages\engine\src\ecs\system\CanvasScaler.ts
-   Ecs system extending System class.
-   Required by scene to give canvas size.
-   Requires canvas entity that holds CanvasScale component.
-   Assumes resolution 1920x1080.
-   Every resize of window:
    -   Resizes canvas to size of window.
    -   Updates component CanvasScale.scaleFactor data.
    -   CanvasScale.scaleFactor is window/1920x1080 size ratio.
    -   Sends event 'resizeCanvas'

#### Usage

-   Add data to entity.json

```json
"canvas": {
    "canvasScale": {
      "scaleFactor": {
        "x": 1,
        "y": 1
      }
    }
  }
```

-Add system to system.json

```json
{
    "system": "canvasScaler",
    "entity": ["canvas"],
    "cache": "startSystemCache",
    "name": "Canvas Scaler"
}
```

[Up](index.md)
[Main](../../../../../index.md)
