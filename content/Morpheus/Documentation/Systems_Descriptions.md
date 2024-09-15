# Systems Descriptions

## SpriteRenderer

### Version 1.0.0

- Caches components.
- Creates animator.
- Event 'AnimationSwitch'.
- Updates animation frames switching with animator.
- Renders animation sprites on canvas.
- Position uses formula:

```plaintext
  transform.position.x + sprite.spriteOffset.x
```

- This is first, old version where sprite origin was in top left.  
  Offset was used to ajust sprite. Didnt know better.
- Canvas draw methods in 'DefaultRenderer'.
