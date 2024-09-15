# Renderer100

This scene point is to test spriteRenderer system.  
It also uses canvasScaler, witch is in each scene.  
Also drawTransformPosition. All in version 1.0.0.  
It has two players.  
Player1 is at transfrom.position 430,540.  
This point is rendered to show that it is top left of the sprite.  
System spriteRenderer 1.0.0 does that.  
Player2 is rendered to show use of component sprite.spriteOffset property.  
It is used to translate sprite so point form transform.position is in center of sprite.  
This behavior is just stupid in retrospect, but i didnt know better at 1.0.0.  
I dint delete this version becouse a lot of features worked on it and wanted to transfer them.  
Even as transfer is done it remains a point of not to do.  
Also to show at the beggining and always, one makes weird assumptions/decisions.

To select this scene pass to config:

```json
 "select": {
      "folder": "engine",
      "subFolder": "",
      "scene": "renderer100"
    },
```