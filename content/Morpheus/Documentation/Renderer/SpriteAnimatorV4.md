## SpriteAnimatorV4 Documentation

### Path

- `packages\engine\src\ecs_system\SpriteAnimatorV4.ts`

### Related Paths

- `packages\engine\src\animator\IAnimationConfig.ts`
- `packages\engine\src\animator\IAnimationFrame.ts`
- `packages\engine\src\ecs_system\IRendererV4.ts`
- `packages\engine\src\math\IVector2.ts`
- `packages\engine\src\ecs_component\ITransform.ts`
- `packages\engine\src\animator\AnimationState.ts`
- `packages\engine\src\animator\IAnimationStrategy.ts`

---

### Short Description

`SpriteAnimatorV4` is a class responsible for handling sprite animations in a 2D environment. It manages various animation strategies and controls how frames are updated and rendered using a provided `IRendererV4` instance.

---

### Longer Description

The `SpriteAnimatorV4` class is designed to animate 2D sprites by cycling through frames based on a provided animation configuration. It supports both cyclic and sequential animation strategies. The class handles frame switching based on elapsed time and the animation type, and it provides functionality for drawing the current frame, either normally or flipped, on an HTML canvas.

The `SpriteAnimatorV4` integrates multiple components such as `IAnimationConfig` to define animations, `IAnimationStrategy` for updating frame states, and `IRendererV4` for rendering the animation onto a canvas.

---

### Constructor

```typescript
constructor(
  animationConfigs: IAnimationConfig[],
  renderer: IRendererV4,
  cyclicAnimation: IAnimationStrategy,
  sequentialAnimation: IAnimationStrategy
)
```

- **Parameters**:
  - `animationConfigs: IAnimationConfig[]`: A list of configurations for different animations. Each config includes the image path, frame size, and other related properties.
  - `renderer: IRendererV4`: A renderer instance responsible for drawing the sprite frames on the canvas.
  - `cyclicAnimation: IAnimationStrategy`: The strategy used for cyclic animations, where frames loop continuously.
  - `sequentialAnimation: IAnimationStrategy`: The strategy used for sequential animations, where frames progress linearly without looping by default.

---

### Methods

#### 1. **createAnimationFrames**

```typescript
private createAnimationFrames(
  config: IAnimationConfig,
  animIndex: number
): IAnimationFrame[]
```

- **Description**:
  - This method generates an array of animation frames based on the provided configuration. It calculates the position and size of each frame within the sprite sheet.
- **Parameters**:
  - `config: IAnimationConfig`: The configuration containing frame size, count, and image data for the animation.
  - `animIndex: number`: The index of the animation in the list of animations.
- **Returns**:
  - An array of `IAnimationFrame` instances representing the frames of the animation.

---

#### 2. **setAnimationStrategy**

```typescript
private setAnimationStrategy(animationType: AnimationType): void
```

- **Description**:
  - Sets the animation strategy based on the `AnimationType`. If the animation is cyclic, the cyclic strategy is used; otherwise, the sequential strategy is applied.
- **Parameters**:
  - `animationType: AnimationType`: The type of animation, either `Cyclic` or `Sequential`.
- **Throws**:
  - An error if the provided animation type is not supported.

---

#### 3. **update**

```typescript
update(deltaTime: number): void
```

- **Description**:
  - Updates the current frame of the animation based on the elapsed time (`deltaTime`) and the selected animation strategy.
- **Parameters**:
  - `deltaTime: number`: The time in milliseconds since the last update.

---

#### 4. **switchAnimation**

```typescript
switchAnimation(animationIndex: number): void
```

- **Description**:
  - Switches to a different animation by updating the sprite's image source and animation strategy. It resets the frame index and timing to start the new animation from the beginning.
- **Parameters**:
  - `animationIndex: number`: The index of the animation to switch to. Should be a valid index within the `animations` array.

---

#### 5. **draw**

```typescript
draw(
  ctx: CanvasRenderingContext2D,
  canvasScale: IVector2,
  transform: ITransform,
  isFlipped = false
): void
```

- **Description**:
  - Renders the current animation frame on the canvas, either in its normal orientation or flipped horizontally. It delegates the drawing to the `IRendererV4` instance.
- **Parameters**:
  - `ctx: CanvasRenderingContext2D`: The 2D rendering context for the canvas.
  - `canvasScale: IVector2`: The scaling factor to apply to the rendered sprite on the canvas.
  - `transform: ITransform`: The transform (position, scale, rotation) applied to the sprite.
  - `isFlipped: boolean`: Whether or not to flip the sprite horizontally when drawing. Defaults to `false`.

---

### Example Usage

#### Updating and Drawing a Sprite:

```typescript
const animator = new SpriteAnimatorV4(
  animationConfigs,
  renderer,
  cyclicAnimation,
  sequentialAnimation
)
animator.update(deltaTime)
animator.draw(ctx, { x: 1, y: 1 }, transform, false)
```

- This will update the current animation frame based on `deltaTime` and draw the sprite on the canvas using the specified scale and transform.

#### Switching Animations:

```typescript
animator.switchAnimation(1)
```

- This will switch to the second animation (at index 1) in the `animations` array, resetting the animation state.

---

### Dependencies

- **IAnimationConfig**:
  - Describes the structure of an animation configuration, including the path to the image file and frame details.
- **IAnimationFrame**:
  - Defines a single animation frame, with properties like frame size and position.
- **IRendererV4**:
  - Interface for rendering the sprite on the canvas, providing methods for drawing normal and flipped frames.
- **ITransform**:
  - Defines the transformation (position, scale, rotation) of the sprite on the canvas.
- **IAnimationStrategy**:
  - Controls the update logic for different types of animations, such as cyclic and sequential.
- **AnimationState**:
  - Manages the current state of the animation, including the active animation index and frame timing.

---

### Conclusion

`SpriteAnimatorV4` is a versatile class designed for animating sprites in 2D environments. It simplifies the management of multiple animation types, allowing easy switching between animations and supporting both normal and flipped rendering. The class is particularly useful for games and graphical applications that rely on smooth, flexible sprite animations.
