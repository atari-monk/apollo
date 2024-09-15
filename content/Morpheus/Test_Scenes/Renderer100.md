# Renderer100

1. This scene point is to test spriteRenderer system.  
2. It also uses canvasScaler, witch is in each scene.  
3. Also drawTransformPosition. All in version 1.0.0.  
4. It has two players.  
5. Player1 is at transfrom.position 430,540.  
This point is rendered to show that it is top left of the sprite.  
System spriteRenderer 1.0.0 does that.  
6. Player2 is rendered to show use of component sprite.spriteOffset property.  
It is used to translate sprite so point form transform.position is in center of sprite.  
7. This behavior is just stupid in retrospect, but i didnt know better at 1.0.0.  
I dint delete this version becouse a lot of features worked on it and wanted to transfer them.  
Even as transfer is done it remains a point to show of what 'not to do'.  
Also to show that, at the beggining and always, one makes weird assumptions/decisions.

---

1. To select this scene pass to config:

```json
 "select": {
      "folder": "engine",
      "subFolder": "",
      "scene": "renderer100"
    }
```