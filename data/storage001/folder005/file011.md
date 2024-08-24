# Ecs System Builder

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

- 'ISystemFileData.ts'

```typescript
export default interface ISystemFileData {
  system: string
  name: string
  entity: string[]
  cache: string
  version: string
  isOn: boolean
}
```

---

- These data are used to control systems in scene.
- System resides in:

```bash
C:\atari-monk\code\ts-engine-nx\packages\engine\src\ecs_system_builder
```

```bash
packages\engine\src\ecs_system_builder
```

- 