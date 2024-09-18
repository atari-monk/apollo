# SpriteRendererV1

## Path
- packages\engine\src\ecs_system\SpriteRendererV1.ts

## Related Path
- packages\engine\src\animator
- packages\engine\src\animatorV1
- packages\engine\src\ecs_system_factory\spriteRendererFactory.ts

## Short Description
- Ecs system extending System class.
- Used in football 1.0.0.
- For each entity regisered in system:
  - Caches sprite animation components Sprite, Transform.
  - Caches animator object.
  - Subscribes to AnimationSwitch event.
  - Updates animator frame.
  - Renders animator.
  - Renders in position transform.position + sprite.spriteOffset.

## Longer Description

The `SpriteRendererV1` class extends the `System` class and is responsible for managing the rendering and animation of sprites in a game or graphical application. Here’s a breakdown of its functionality:

1. **Constructor**: Initializes the `SpriteRendererV1` with dependencies such as `entityCache`, `renderer`, `eventSystem`, `spriteAnimatorFactory`, and `logger`.

2. **startEntity**: Sets up a new entity by creating a cache for it and subscribing to relevant events.

3. **createCache**: Constructs a cache object for an entity, including components like `transform`, `sprite`, and an `animator` created using the `spriteAnimatorFactory`.

4. **subscribeEvent**: Subscribes to the `AnimationSwitch` event, which triggers the `switchAnimation` method when the event occurs.

5. **switchAnimation**: Changes the animation of the sprite if the event data corresponds to the entity.

6. **updateEntity**: Updates the entity by setting its position and updating its animation based on the `deltaTime`. If the cache for the entity is missing, logs an error.

7. **logError**: Logs an error message when the cache for an entity is not found.

8. **setPosition**: Updates the sprite's position by adding its offset to its current position.

9. **renderEntity**: Renders the entity by drawing the sprite using the animator, its position, and flip state. If the cache for the entity is missing, logs an error.

In summary, `SpriteRendererV1` manages the lifecycle of sprites, including caching their state, handling animation changes, updating their positions, and rendering them.

## Test Scene

1. This scene point is to test spriteRenderer system.  
2. It also uses canvasScaler, witch is in each scene.  
3. Also drawTransformPosition. All in version 1.0.0.  
4. It has four players.  
5. Player1 is at transfrom.position 430,540.  
This point is rendered to show that it is top left of the sprite.  
**System spriteRenderer 1.0.0 renders transfrom.position as top left point of sprite.**  
6. Player2 is rendered to show use of component sprite.spriteOffset property.  
**Component property sprite.spriteOffset is used to translate sprite so point form transform.position is in center of sprite.**  
7. This behavior is just stupid in retrospect, but i didnt know better at 1.0.0.  
I dint delete this version becouse a lot of features worked on it and wanted to transfer them.  
Even as transfer is done it remains a point to show of what 'not to do'.  
Also to show that, at the beggining and always, one makes weird assumptions/decisions.
8. Also player 3 and 4 was added to test flipping of sprite.  
They are 1,2 but flipped and moved by x+100.
9. To select this scene pass to config:

```json
 "select": {
      "folder": "engine",
      "subFolder": "",
      "scene": "renderer100"
    }
```

## Usage

- Add data to entity.json

```json
"canvas": {
    "canvasScale": {
      "scaleFactor": {
        "x": 1,
        "y": 1
      }
    }
  },
  "player1": {
    "id": "player1",
    "name": "player1",
    "transform": {
      "position": {
        "x": 430,
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
    "nr": 1,
    "system": "canvasScaler",
    "name": "Canvas Scaler",
    "entity": ["canvas"],
    "cache": "startSystemCache",
    "version": "1.0.0",
    "isOn": true
  },
  {
    "nr": 2,
    "system": "spriteRenderer",
    "name": "Sprite Renderer",
    "entity": ["player1"],
    "cache": "rendererCache",
    "version": "1.0.0",
    "isOn": true
  },
  {
    "nr": 2,
    "system": "drawTransformPosition",
    "name": "Sprite Renderer",
    "entity": ["player1"],
    "cache": "rendererCache",
    "version": "1.0.0",
    "isOn": true
  }
```
