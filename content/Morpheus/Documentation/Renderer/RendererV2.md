## RendererV2 Documentation

### Path

- `packages\engine\src\ecs_system\RendererV2.ts`

### Related Paths

- `packages\engine\src\animator\IAnimationFrame.ts`
- `packages\engine\src\math\IVector2.ts`
- `packages\engine\src\math\Vector2.ts`
- `packages\engine\src\ecs_system\IRenderer.ts`

---

### Short Description

`RendererV2` is an updated class implementing the `IRenderer` interface. It enhances sprite rendering by supporting scaling alongside the normal and flipped rendering of sprites onto an HTML canvas.

---

### Longer Description

The `RendererV2` class handles rendering sprites on a canvas with the added functionality of scaling. It provides two main methods: `drawNormal`, which draws sprites with scaling, and `drawFlipped`, which flips sprites horizontally while applying the scaling transformation. This version is an extension of `RendererV1` with scaling support for both normal and flipped rendering.

---

### Constructor

Like `RendererV1`, `RendererV2` doesn't require a custom constructor as it only provides static rendering methods.

---

### Methods

#### 1. **drawNormal**

```typescript
drawNormal(
  ctx: CanvasRenderingContext2D,
  image: HTMLImageElement,
  frame: IAnimationFrame,
  position: IVector2,
  scale: IVector2
): void
```

- **Description**:
  - This method draws a sprite on the canvas, scaling it based on the given scale vector.
- **Parameters**:

  - `ctx: CanvasRenderingContext2D`: The 2D rendering context for the canvas.
  - `image: HTMLImageElement`: The image containing the sprite or animation frames.
  - `frame: IAnimationFrame`: The animation frame, specifying the source position and size of the sprite.
  - `position: IVector2`: The position on the canvas where the sprite should be drawn.
  - `scale: IVector2`: The scale factor applied to both the position and size of the sprite.

- **Functionality**:
  - The method draws the sprite at the specified position, scaled by the `scale.x` and `scale.y` values. Both the sprite’s position and size are adjusted according to the scale vector, allowing the sprite to be rendered at varying sizes.

---

#### 2. **drawFlipped**

```typescript
drawFlipped(
  ctx: CanvasRenderingContext2D,
  image: HTMLImageElement,
  frame: IAnimationFrame,
  position: IVector2,
  scale: IVector2
): void
```

- **Description**:

  - This method renders a horizontally flipped version of the sprite, with the scaling transformation applied.

- **Parameters**:

  - `ctx: CanvasRenderingContext2D`: The 2D rendering context for the canvas.
  - `image: HTMLImageElement`: The image containing the sprite or animation frames.
  - `frame: IAnimationFrame`: The animation frame specifying the source position and size of the sprite.
  - `position: IVector2`: The position on the canvas where the flipped sprite should be drawn.
  - `scale: IVector2`: The scaling vector applied to both the position and size of the sprite.

- **Functionality**:
  - The method first saves the canvas state with `ctx.save()`, then translates the canvas to the position where the sprite should be drawn and scales it horizontally by -1 to achieve the flip.
  - The position and size of the sprite are multiplied by the `scale` vector, ensuring the flip and scaling are applied simultaneously.
  - After the sprite is drawn, the canvas state is restored using `ctx.restore()` to remove the transformation effect for the next drawing operations.

---

### Example Usage

#### Drawing a Scaled Normal Sprite:

```typescript
const renderer = new RendererV2()
const scale = { x: 2, y: 2 }
renderer.drawNormal(ctx, playerImage, currentFrame, { x: 100, y: 200 }, scale)
```

- This will draw the sprite at position (100, 200) on the canvas, scaling it to twice its normal size.

#### Drawing a Scaled Flipped Sprite:

```typescript
renderer.drawFlipped(ctx, playerImage, currentFrame, { x: 100, y: 200 }, scale)
```

- This will draw a horizontally flipped version of the sprite at position (100, 200) on the canvas, scaling it to twice its normal size.

---

### Dependencies

- **IAnimationFrame**:
  - Defines the structure of an animation frame, including the position and size within the sprite sheet.
- **IVector2 & Vector2**:
  - Defines the 2D vectors for both position and scaling, and the `Vector2.zero` constant represents a vector with (0, 0) coordinates, used when rendering flipped sprites.

---

### Conclusion

`RendererV2` builds upon the functionality of `RendererV1` by introducing the ability to scale sprites. This allows for more flexible and dynamic rendering in games or graphical applications, where sprites can be resized and flipped based on game logic or user interactions.
