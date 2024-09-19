# Ecs System Builder

- These data are used to control systems in scene.
- 'system.json'

```json
[
  {
    "system": "canvasScaler",
    "name": "Canvas Scaler",
    "entity": ["canvas"],
    "cache": "startSystemCache",
    "version": "3.0.0",
    "isOn": "true"
  },
  {
    "system": "sceneRendererV3",
    "name": "Scene Renderer",
    "entity": ["field"],
    "cache": "rendererCache",
    "version": "3.0.0",
    "isOn": "true"
  }
]
```
