# KeyboardMapping

[Up](index.md)
[Main](../../../../../index.md)

-   C:\atari-monk\code\ts-engine-nx\packages\engine\src\ecs\system\keyboard\KeyboardMapping.ts
-   Ecs system extending System class.
-   Subscribes to input KeyEvents.KeyDown.
-   Stores key list.
-   On key down sends event KeyboardEvent with key and entity id registered in this system

#### Usage

-   Add data to entity.json

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

[Up](index.md)
[Main](../../../../../index.md)
