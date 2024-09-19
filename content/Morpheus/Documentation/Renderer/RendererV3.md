## RendererV3 Documentation

### Path

- `packages\engine\src\ecs_system\RendererV3.ts`

### Related Paths

- `packages\engine\src\animator\IAnimationFrame.ts`
- `packages\engine\src\math\IVector2.ts`
- `packages\engine\src\math\Vector2.ts`
- `packages\engine\src\ecs_system\IRenderer.ts`

---

### Short Description

`RendererV3` is a class implementing the `IRenderer` interface, which enhances sprite rendering by centering sprites at their position and supporting scaling transformations. This version builds on the functionality of `RendererV2` but ensures that the sprites are drawn with their centers aligned to the specified position.

---

### Longer Description

`RendererV3` extends the sprite rendering functionality by adjusting the position calculations to center the sprite based on its size, rather than drawing it from the top-left corner. This change ensures that the `position` represents the center of the sprite, which is useful in games and graphical applications that rely on centered sprite positioning. As in `RendererV2`, both normal and flipped sprites can be scaled during rendering.

---

### Constructor

`RendererV3` does not require a custom constructor as it provides static rendering methods for handling sprite drawing operations.

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
  - This method draws a sprite on the canvas with its center aligned to the specified position and scaled based on the provided scale vector.
- **Parameters**:

  - `ctx: CanvasRenderingContext2D`: The 2D rendering context for the canvas.
  - `image: HTMLImageElement`: The image containing the sprite or animation frames.
  - `frame: IAnimationFrame`: The animation frame specifying the source position and size of the sprite.
  - `position: IVector2`: The position on the canvas where the center of the sprite should be drawn.
  - `scale: IVector2`: The scaling factor applied to both the position and size of the sprite.

- **Functionality**:
  - The method first adjusts the position to place the sprite's center at the `position` coordinates by subtracting half of the sprite's width and height. The sprite is then drawn at this adjusted position, with both its size and position scaled based on the `scale` vector.

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

  - This method draws a horizontally flipped version of the sprite, with its center aligned to the specified position and scaling applied.

- **Parameters**:

  - `ctx: CanvasRenderingContext2D`: The 2D rendering context for the canvas.
  - `image: HTMLImageElement`: The image containing the sprite or animation frames.
  - `frame: IAnimationFrame`: The animation frame specifying the source position and size of the sprite.
  - `position: IVector2`: The position on the canvas where the center of the flipped sprite should be drawn.
  - `scale: IVector2`: The scaling factor applied to both the position and size of the sprite.

- **Functionality**:
  - The method first saves the current canvas state, then translates the canvas to the sprite's center position and scales it horizontally by -1 to achieve the flip. The flipped sprite is drawn at the adjusted position with scaling applied, and the canvas state is restored after drawing to ensure that the transformation doesn't affect future rendering operations.

---

### Example Usage

#### Drawing a Centered, Scaled Normal Sprite:

```typescript
const renderer = new RendererV3()
const scale = { x: 1.5, y: 1.5 }
renderer.drawNormal(ctx, playerImage, currentFrame, { x: 300, y: 200 }, scale)
```

- This will draw the sprite centered at position (300, 200) on the canvas, scaled to 1.5 times its original size.

#### Drawing a Centered, Scaled Flipped Sprite:

```typescript
renderer.drawFlipped(ctx, playerImage, currentFrame, { x: 300, y: 200 }, scale)
```

- This will draw a horizontally flipped version of the sprite, centered at position (300, 200), and scaled to 1.5 times its original size.

---

### Dependencies

- **IAnimationFrame**:
  - Defines the structure of an animation frame, including the position and size of the frame in the sprite sheet.
- **IVector2 & Vector2**:
  - Represents 2D vectors for position and scaling. The `Vector2.zero` constant is used for rendering flipped sprites without a position shift.

---

### Conclusion

`RendererV3` refines the rendering process by aligning sprites to the center of their position, offering greater flexibility and control when managing sprite animations in games or graphical applications. The scaling and flipping capabilities from `RendererV2` are preserved, while the centering adjustment enhances the accuracy and utility of sprite positioning.
