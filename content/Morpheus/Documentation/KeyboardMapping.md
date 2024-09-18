# KeyboardMapping

## Path

- packages\engine\src\ecs_system\KeyboardMapping.ts

## Short Description

- Ecs system extending System class.
- Subscribes to input KeyEvents.KeyDown.
- Stores key list.
- On key down sends event KeyboardEvent with key and entity id registered in this system

#### Usage

- Add data to entity.json

```json
 "debugUI": {
    "id": "debugUI",
    "name": "debugUI",
    "keyMap": {
      "actions": [
        {
          "action": "toggleOrigin",
          "key": "u",
          "pressOnceOnStart": false
        },
        {
          "action": "toggleCollider",
          "key": "i",
          "pressOnceOnStart": true
        },
        {
          "action": "toggleAnimation",
          "key": "o",
          "pressOnceOnStart": false
        }
      ]
    }
  }
```

-Add system to system.json

```json
{
  "system": "keyboardMapping",
  "entity": ["debugUI"],
  "cache": "startSystemCache",
  "name": "Keyboard Mapping"
}
```
