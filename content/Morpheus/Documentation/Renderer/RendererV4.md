## RendererV4 Documentation

### Path

- `packages\engine\src\ecs_system\RendererV4.ts`

### Related Paths

- `packages\engine\src\math\IVector2.ts`
- `packages\engine\src\ecs_component\ITransform.ts`
- `packages\engine\src\animator\IAnimationFrame.ts`
- `packages\engine\src\ecs_system\IRendererV4.ts`

---

### Short Description

`RendererV4` is a class implementing the `IRendererV4` interface, responsible for rendering sprites with scaling, flipping, and positioning transformations using a more structured approach with the `ITransform` component. It also integrates the canvas scaling factor for drawing sprites in games or applications.

---

### Longer Description

`RendererV4` is an upgraded version of previous renderers. It incorporates the `ITransform` component, which includes position and scale, to handle transformations. Additionally, it supports canvas scaling, which allows dynamic scaling of the entire rendering context based on the provided `canvasScale`. This class offers methods to draw sprites both normally and flipped while maintaining central alignment for sprite positioning, using the middle of the sprite as the origin.

---

### Constructor

No constructor is needed for `RendererV4`. The rendering functions are static methods that take in various parameters, including the canvas context, image, animation frame, and transform components.

---

### Methods

#### 1. **drawNormal**

```typescript
drawNormal(
  ctx: CanvasRenderingContext2D,
  canvasScale: IVector2,
  image: HTMLImageElement,
  frame: IAnimationFrame,
  transform: ITransform
): void
```

- **Description**:
  - Draws a sprite in its normal orientation, centered at its position, while applying both the canvas scaling factor and the entity’s own scaling transformation.
- **Parameters**:

  - `ctx: CanvasRenderingContext2D`: The rendering context of the canvas.
  - `canvasScale: IVector2`: Scaling factor to be applied to the entire canvas.
  - `image: HTMLImageElement`: The sprite or animation frame image to be rendered.
  - `frame: IAnimationFrame`: Information about the animation frame, including its position and size on the sprite sheet.
  - `transform: ITransform`: Contains the sprite’s position and scaling transformation.

- **Functionality**:
  - The method first saves the current canvas state. It then scales the canvas using the provided `canvasScale`, translates to the sprite's `position`, and applies the sprite's own scaling factor. The sprite is then drawn at its new position with its center aligned to the specified coordinates. The canvas state is restored at the end to avoid affecting other rendering operations.

---

#### 2. **drawFlipped**

```typescript
drawFlipped(
  ctx: CanvasRenderingContext2D,
  canvasScale: IVector2,
  image: HTMLImageElement,
  frame: IAnimationFrame,
  transform: ITransform
): void
```

- **Description**:
  - Draws a horizontally flipped version of the sprite, centered at its position, with both canvas scaling and entity-specific scaling transformations applied.
- **Parameters**:

  - `ctx: CanvasRenderingContext2D`: The rendering context of the canvas.
  - `canvasScale: IVector2`: Scaling factor to be applied to the entire canvas.
  - `image: HTMLImageElement`: The sprite or animation frame image to be rendered.
  - `frame: IAnimationFrame`: Information about the animation frame, including its position and size on the sprite sheet.
  - `transform: ITransform`: Contains the sprite’s position and scaling transformation.

- **Functionality**:
  - Similar to `drawNormal`, this method saves the canvas state, applies canvas scaling, and translates to the sprite’s position. It then flips the sprite horizontally by applying a negative scale to the x-axis while maintaining the sprite’s vertical scaling. The flipped sprite is drawn with its center aligned to the `position` coordinates, and the canvas state is restored afterward.

---

### Example Usage

#### Drawing a Normal Sprite:

```typescript
const renderer = new RendererV4()
const canvasScale = { x: 1.5, y: 1.5 }
const transform = {
  position: { x: 200, y: 300 },
  scale: { x: 1, y: 1 },
}
renderer.drawNormal(ctx, canvasScale, playerImage, currentFrame, transform)
```

- This will render a sprite centered at position (200, 300) on the canvas, with no additional scaling applied to the sprite itself but scaled by the canvas scale factor.

#### Drawing a Flipped Sprite:

```typescript
renderer.drawFlipped(ctx, canvasScale, playerImage, currentFrame, transform)
```

- This will render a horizontally flipped version of the sprite, centered at position (200, 300), and scaled by the canvas scale factor.

---

### Dependencies

- **IAnimationFrame**:
  - Defines the properties of an animation frame, such as the size and position within a sprite sheet.
- **IVector2**:
  - Represents 2D vectors used for defining positions and scaling factors.
- **ITransform**:
  - Represents the transformation component of the sprite, including position and scaling properties.

---

### Conclusion

`RendererV4` is a versatile rendering system that allows precise control over sprite positioning and scaling. It integrates canvas-wide scaling with entity-specific transformations, making it suitable for games and applications that need dynamic and responsive visual elements. It also supports both normal and flipped sprite rendering, providing flexibility in handling animations.
