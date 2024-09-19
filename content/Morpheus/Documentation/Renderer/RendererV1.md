## RendererV1 Documentation

### Path

- `packages\engine\src\ecs_system\RendererV1.ts`

### Related Paths

- `packages\engine\src\animator\IAnimationFrame.ts`
- `packages\engine\src\math\IVector2.ts`
- `packages\engine\src\math\Vector2.ts`
- `packages\engine\src\ecs_system\IRendererV1.ts`

---

### Short Description

`RendererV1` is a class that implements the `IRendererV1` interface to handle drawing 2D images (sprites) onto an HTML canvas. It provides methods for rendering sprites both in their normal orientation and flipped horizontally.

---

### Longer Description

The `RendererV1` class is responsible for rendering sprites onto a canvas using two primary methods: `drawNormal`, for drawing sprites in their default orientation, and `drawFlipped`, for drawing sprites flipped horizontally. These methods work with animation frames and the canvas' 2D rendering context to ensure that the sprites are rendered accurately in the desired position and orientation.

---

### Constructor

The class does not have a custom constructor, as it only provides static functionality through its drawing methods.

---

### Methods

#### 1. **drawNormal**

```typescript
drawNormal(
  ctx: CanvasRenderingContext2D,
  image: HTMLImageElement,
  frame: IAnimationFrame,
  position: IVector2
): void
```

- **Description**:
  - This method is used to draw a sprite (or a portion of it) onto the canvas at a specified position without any transformations.
- **Parameters**:
  - `ctx: CanvasRenderingContext2D`: The 2D rendering context for the canvas where the image will be drawn.
  - `image: HTMLImageElement`: The image containing the sprite or animation frames.
  - `frame: IAnimationFrame`: The specific animation frame to be rendered. Contains details such as the position and size of the frame within the image.
  - `position: IVector2`: The position on the canvas where the sprite should be drawn.
- **Functionality**:
  - The method uses the `drawImage` function from the Canvas API to render the image at the provided position with no additional transformations or effects.
  - The frame's source position and size (within the sprite sheet) are defined by `frame.framePosition` and `frame.frameSize`, and these values determine which part of the image to render.

---

#### 2. **drawFlipped**

```typescript
drawFlipped(
  ctx: CanvasRenderingContext2D,
  image: HTMLImageElement,
  frame: IAnimationFrame,
  position: IVector2
): void
```

- **Description**:
  - This method is used to render a horizontally flipped version of the sprite. The flip is achieved by manipulating the canvas' transformation matrix before drawing the sprite and then resetting the matrix afterward.
- **Parameters**:

  - `ctx: CanvasRenderingContext2D`: The 2D rendering context for the canvas.
  - `image: HTMLImageElement`: The image containing the sprite or animation frames.
  - `frame: IAnimationFrame`: The animation frame to be rendered.
  - `position: IVector2`: The position on the canvas where the flipped sprite should be drawn.

- **Functionality**:
  - The method first saves the current canvas state using `ctx.save()`.
  - Then it performs a transformation by translating the canvas to the sprite's position and scaling it negatively along the X-axis to achieve a horizontal flip.
  - After the transformation, it calls the `drawNormal` method to draw the image.
  - Finally, the method restores the canvas state with `ctx.restore()` to revert the transformations.

---

### Example Usage

#### Drawing a Normal Sprite:

```typescript
const renderer = new RendererV1()
renderer.drawNormal(ctx, playerImage, currentFrame, { x: 100, y: 200 })
```

- This will draw the sprite at position (100, 200) on the canvas using the provided `playerImage` and `currentFrame`.

#### Drawing a Flipped Sprite:

```typescript
renderer.drawFlipped(ctx, playerImage, currentFrame, { x: 100, y: 200 })
```

- This will draw a horizontally flipped version of the sprite at position (100, 200) on the canvas.

---

### Dependencies

- **IAnimationFrame**:
  - Used to define the structure of an animation frame, including its position and size within the image.
- **IVector2 & Vector2**:
  - Defines the position on the canvas where the image is drawn. The `Vector2.zero` constant is used to indicate a position of (0, 0) when rendering flipped sprites.

---

### Conclusion

`RendererV1` simplifies rendering sprites onto an HTML canvas, offering basic functionality for both normal and horizontally flipped rendering. It is a lightweight, essential component for games or graphical applications that need to render animated sprites with minimal overhead.
