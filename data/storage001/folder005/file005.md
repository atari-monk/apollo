# SpriteRendererV1

- C:\atari-monk\code\ts-engine-nx\packages\engine\src\animation_system\ecs\system\sprite_renderer\SpriteRendererV1.ts
- Ecs system extending System class.
- Used in football 1.0.0
- For each entity regisered in system:
  - Caches sprite animation components Sprite, Transform.
  - Caches animator object.
  - Subscribes to AnimationSwitch event.
  - Updates animator frame.
  - Renders animator.
  - Renders in position transform.position + sprite.spriteOffset.

#### Usage

- Add data to entity.json

```json
  "player1": {
    "id": "player1",
    "name": "player1",
    "transform": {
      "position": {
        "x": 830,
        "y": 540
      },
      "scale": {
        "x": 1,
        "y": 1
      },
      "rotation": 0
    },
    "sprite": {
      "spriteOffset": {
        "x": -36,
        "y": -75
      },
      "isFlipped": false,
      "spriteAnimation": [
        {
          "imagePath": "./assets/images/football/red-player.png",
          "frameCount": 20,
          "frameDuration": 0.05,
          "frameSize": {
            "x": 80,
            "y": 160
          },
          "animationType": 1
        }
      ],
      "state": "idle"
    }
  }
```

-Add system to system.json

```json
{
  "system": "spriteRendererV1Tester",
  "entity": ["player1"],
  "cache": "rendererCache",
  "name": "Sprite Renderer"
}
```
