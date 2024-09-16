# RendererV1

```typescript
import { IRenderer } from './IRenderer'
import { IAnimationFrame } from './IAnimationFrame'
import IVector2 from '../math/IVector2'
import Vector2 from '../math/Vector2'

export default class RendererV1 implements IRenderer {
  drawNormal(
    ctx: CanvasRenderingContext2D,
    image: HTMLImageElement,
    frame: IAnimationFrame,
    position: IVector2,
    _scale: IVector2
  ): void {
    ctx.drawImage(
      image,
      frame.framePosition.x,
      frame.framePosition.y,
      frame.frameSize.x,
      frame.frameSize.y,
      position.x,
      position.y,
      frame.frameSize.x,
      frame.frameSize.y
    )
  }

  drawFlipped(
    ctx: CanvasRenderingContext2D,
    image: HTMLImageElement,
    frame: IAnimationFrame,
    position: IVector2,
    scale: IVector2
  ): void {
    ctx.save()
    ctx.translate(position.x + frame.frameSize.x, position.y)
    ctx.scale(-1, 1)
    this.drawNormal(ctx, image, frame, Vector2.zero, scale)
    ctx.restore()
  }
}
```

This `RendererV1` class implements the `IRenderer` interface and provides two main methods for drawing images on a canvas: `drawNormal` and `drawFlipped`. Here's a breakdown of how each method works:

1. **drawNormal**:

   - This method is responsible for drawing an image on the canvas as it is, without any transformations.
   - It takes in the following parameters:
     - `ctx`: The canvas rendering context (`CanvasRenderingContext2D`) used for drawing.
     - `image`: The image (`HTMLImageElement`) that will be drawn.
     - `frame`: An object of type `IAnimationFrame`, which contains information about the specific frame to draw from a sprite sheet, such as the position and size of the frame within the image.
     - `position`: An `IVector2` object representing the (x, y) coordinates on the canvas where the image should be drawn.
     - `_scale`: A scaling factor (`IVector2`), though it isn't used directly in this function.
   - The method uses `ctx.drawImage` to draw a part of the image (the specific frame) onto the canvas at the given position. It extracts the frame's position and size from `frame.framePosition` and `frame.frameSize`.

2. **drawFlipped**:
   - This method draws the image flipped horizontally (mirrored along the vertical axis).
   - It uses `ctx.save()` to save the current canvas state and `ctx.restore()` to restore it at the end of the drawing operation, ensuring that any transformations applied during drawing (e.g., translation or scaling) do not affect other drawings.
   - The method first translates the canvas context so that the image's position is moved by the width of the frame and then scales the canvas horizontally by -1 to flip the image.
   - It calls `drawNormal` to draw the flipped image at the translated position, using `Vector2.zero` for the position, as the transformation has already handled the placement.

In summary, `RendererV1` provides basic functionality for drawing both normal and horizontally flipped images from sprite sheets onto an HTML5 canvas.

---

Yes but dont u think it is not well designed ?  
Position is not the center, dosent have canvasScaling, scaling, rotation, with canvas transforms.

You're right—the design of the `RendererV1` class has some limitations, particularly in terms of flexibility and how it handles transformations like scaling, rotation, and positioning. The current implementation:

1. **Uses the top-left corner as the reference point** instead of the center, which makes positioning less intuitive, especially for complex transformations or game objects.
2. **Lacks handling for scaling** beyond just flipping the image. It doesn't account for scaling factors that would resize the drawn image dynamically based on the desired size.

3. **Has no rotation support**, which is a common requirement in rendering engines, especially for game development.

4. **Transformations are limited**—currently, only flipping (mirroring) is supported, but scaling and rotation are equally important and should be applied via canvas transforms.

### Redesign Proposal

Here's how we could improve the design:

1. **Position the image based on its center** (or give the option to specify how the image should be aligned, whether centered or top-left).
2. **Introduce scaling and rotation transforms** by using the `ctx.scale()` and `ctx.rotate()` methods.
3. **Account for canvas scaling** in both normal and flipped drawing modes.
4. **Allow custom transform order** for more flexibility (e.g., applying rotation, then scaling, etc.).

Here's a refined version of `RendererV1`:

```typescript
export default class RendererV2 implements IRenderer {
  drawNormal(
    ctx: CanvasRenderingContext2D,
    image: HTMLImageElement,
    frame: IAnimationFrame,
    position: IVector2,
    scale: IVector2,
    rotation: number = 0
  ): void {
    ctx.save() // Save the current canvas state

    // Translate to the image's center, considering scaling
    const centerX = position.x + (frame.frameSize.x * scale.x) / 2
    const centerY = position.y + (frame.frameSize.y * scale.y) / 2

    ctx.translate(centerX, centerY) // Move to the center
    ctx.rotate(rotation) // Apply rotation if any
    ctx.scale(scale.x, scale.y) // Apply scaling if any

    // Draw the image, adjusting for its center after transforms
    ctx.drawImage(
      image,
      frame.framePosition.x,
      frame.framePosition.y,
      frame.frameSize.x,
      frame.frameSize.y,
      -frame.frameSize.x / 2, // Since we've translated to the center
      -frame.frameSize.y / 2, // Move image back by half its size
      frame.frameSize.x,
      frame.frameSize.y
    )

    ctx.restore() // Restore the canvas state to prevent affecting future drawings
  }

  drawFlipped(
    ctx: CanvasRenderingContext2D,
    image: HTMLImageElement,
    frame: IAnimationFrame,
    position: IVector2,
    scale: IVector2,
    rotation: number = 0
  ): void {
    ctx.save() // Save the current canvas state

    // Translate to the image's center, considering scaling
    const centerX = position.x + (frame.frameSize.x * scale.x) / 2
    const centerY = position.y + (frame.frameSize.y * scale.y) / 2

    ctx.translate(centerX, centerY) // Move to the center
    ctx.rotate(rotation) // Apply rotation if any
    ctx.scale(-scale.x, scale.y) // Flip horizontally and apply scaling

    // Draw the flipped image, adjusting for its center after transforms
    ctx.drawImage(
      image,
      frame.framePosition.x,
      frame.framePosition.y,
      frame.frameSize.x,
      frame.frameSize.y,
      -frame.frameSize.x / 2, // Since we've translated to the center
      -frame.frameSize.y / 2, // Move image back by half its size
      frame.frameSize.x,
      frame.frameSize.y
    )

    ctx.restore() // Restore the canvas state
  }
}
```

### Key Changes:

1. **Central positioning**: The `position` now refers to the center of the image, making it easier to manage placement and transformations like rotation.
2. **Scaling**: Added `ctx.scale(scale.x, scale.y)` to allow dynamic resizing of the image.

3. **Rotation**: `ctx.rotate(rotation)` allows for easy rotation of the image around its center.

4. **Flipping**: In `drawFlipped`, `ctx.scale(-scale.x, scale.y)` flips the image horizontally while still respecting scaling.

### Flexibility:

This design gives you more control over how the image is rendered, whether you want to flip, scale, or rotate it. It also keeps the canvas state intact between drawing operations by using `ctx.save()` and `ctx.restore()`.

Let me know if this aligns better with what you were aiming for!

---

Is there usecase for V1 ?

Yes, despite its limitations, **`RendererV1`** still has some valid use cases, especially when simplicity and performance are more critical than flexibility. Here are a few scenarios where `RendererV1` could be useful:

### 1. **Simple 2D Sprite Rendering (No Advanced Transforms)**

- **Use Case**: If you're rendering static sprites or sprites that only need basic frame animation (without scaling, rotation, or complex transformations), `RendererV1` is more than sufficient. It focuses on a minimal set of operations, ensuring quick rendering with minimal overhead.
- **Example**: In 2D games or applications where you have animated characters or UI elements that don’t need complex visual effects, this simple renderer would be ideal.

### 2. **Performance-Critical Scenarios**

- **Use Case**: If performance is a key concern (e.g., mobile games or highly optimized 2D applications), the simpler `RendererV1` would likely perform better than more complex renderers. Since it avoids unnecessary transforms and calculations, it can be faster, especially when drawing many objects in rapid succession.
- **Example**: Rendering large numbers of background objects, tiles, or other simple elements where transforms aren't needed would be faster using this straightforward approach.

### 3. **Rendering with Pre-Transformed Assets**

- **Use Case**: If your assets (images) are already pre-scaled, pre-flipped, or pre-rotated, and you don’t need to perform any real-time transformations, the simpler `RendererV1` can still be effective. This might apply if you're using sprite sheets that are designed with different transformations baked into them.
- **Example**: An application where you have different versions of an image (like flipped or rotated sprites) already available in a sprite sheet, so you don't need the renderer to handle these transformations.

### 4. **Fixed UI Elements or Static Graphics**

- **Use Case**: For applications that involve fixed or static elements, like a non-interactive UI (menu, HUD, etc.), where no dynamic transformations are required, `RendererV1` would work well. There's no need for the extra complexity of scaling or rotating when elements are always drawn in the same way.
- **Example**: A heads-up display (HUD) in a game where you always want to display icons or static elements at the same position, size, and orientation.

### 5. **Initial Prototyping or Simplicity**

- **Use Case**: If you’re just prototyping a project and don’t need complex rendering yet, `RendererV1` offers a simpler, less distracting API. Once the prototype requires more functionality, you can move to a more advanced renderer like `RendererV2`.
- **Example**: Early stages of game or UI development when you're focusing more on logic and flow rather than visual details or dynamic transformations.

### 6. **Limited Platform or Browser Capabilities**

- **Use Case**: In cases where the platform might not support complex transformations efficiently (e.g., older devices or browsers), using `RendererV1` ensures compatibility without overloading the system with complex transforms.
- **Example**: Rendering 2D sprites on very low-end hardware or in environments like older browsers or embedded systems where performance is constrained.

---

### Conclusion:

While `RendererV1` lacks advanced features like scaling, rotation, and center-based positioning, it's still useful when:

- You don't need those features.
- Performance is a priority.
- Your assets already incorporate transformations.
- The project is at an early stage or very simple.

For more dynamic or visually rich applications, however, moving to a more robust renderer like `RendererV2` would be necessary.

---

What about its top left position, would that be usefull in some case ?

Yes, the top-left positioning in **`RendererV1`** can still be useful in several scenarios, particularly in 2D rendering contexts where aligning objects by their top-left corner makes sense. Here are some cases where top-left positioning is beneficial:

### 1. **Grid-Based Layouts**

- **Use Case**: In games or applications with grid-based layouts (like tile maps, board games, or pixel art), aligning elements by the top-left corner simplifies positioning. Each tile or element can be placed directly in a cell of the grid without additional calculations for centering.
- **Example**: A **tile map editor** or a **puzzle game** where tiles need to be positioned in a strict grid system can benefit from the top-left origin. For instance, each tile might be 32x32 pixels, and the position of a tile at (3, 5) would simply be `(3 * 32, 5 * 32)`.

### 2. **UI Layouts (Top-Left Aligned)**

- **Use Case**: Many user interfaces (UI) elements like buttons, icons, or panels are naturally aligned by their top-left corner. This is often how UI frameworks position and render elements, making top-left positioning a natural fit.
- **Example**: **Buttons** or **menus** in an application where you want each element to be placed in a fixed position relative to the top-left of its container (e.g., a window or a panel). For instance, you might position a button at `(10, 10)` without needing to adjust for its size.

### 3. **Canvas or Image Cropping**

- **Use Case**: When drawing sprites or parts of images (like from a sprite sheet), the top-left corner is often the reference point. Using the top-left position simplifies the calculation when you need to crop images or draw them at exact pixel coordinates.
- **Example**: **Rendering sprite sheets** where each frame of the sprite is laid out in a grid, and you want to extract and draw a specific portion of the image. In this case, positioning based on the top-left is intuitive, as it matches the coordinate system of the sprite sheet itself.

### 4. **Static Backgrounds or Large Elements**

- **Use Case**: For large static background images, top-left positioning makes sense because such elements usually cover a significant part of the screen, starting from the top-left corner.
- **Example**: A **parallax scrolling background** where each layer starts at the top-left of the canvas. This approach is efficient for rendering backgrounds in games or apps where the entire canvas is filled from the top-left.

### 5. **Browser Rendering and CSS Alignment**

- **Use Case**: HTML and CSS layout models, including the canvas element, use top-left as the default positioning anchor. By using the same convention in your rendering, you align more naturally with the rest of the web technologies.
- **Example**: Drawing elements that mirror **DOM layouts**, where top-left alignment is the default for CSS elements (e.g., a canvas overlay positioned at the same top-left corner as a corresponding HTML element).

### 6. **Pixel-Perfect Rendering**

- **Use Case**: In cases where **pixel-perfect rendering** is crucial (such as retro or pixel-art games), top-left positioning makes calculations straightforward and avoids sub-pixel rendering issues that can occur when positioning elements based on their center.
- **Example**: A **pixel-art game** where sprites need to align perfectly with a pixel grid can benefit from top-left positioning. Placing elements based on whole numbers (e.g., `(32, 64)`) prevents anti-aliasing or blurring caused by sub-pixel adjustments.

### 7. **Fixed-Size UI Components**

- **Use Case**: If you're dealing with UI components that have a fixed, non-resizable size (like toolbars, headers, or footers), top-left positioning allows you to precisely place these elements without needing to calculate their center points.
- **Example**: A **header or toolbar** in a web application that spans the top of the screen and is aligned starting from `(0, 0)` in the top-left corner.

---

### Conclusion:

Top-left positioning can be useful in contexts where elements are naturally placed in a grid, pixel-perfect layout, or UI scenario. It simplifies calculations when aligning objects to edges or when interacting with fixed-size components. While centering is more intuitive for dynamic objects and transformations, the top-left positioning can provide simplicity and precision in more static or structured use cases.

---

Well than maybe i should keep the class.

That makes sense! Keeping the `RendererV1` class as a simpler, more performance-oriented option can be a good idea, especially for cases where you don't need the extra complexity of more advanced rendering. You can always have both `RendererV1` for straightforward use cases and a more flexible version for when you need more features like scaling, rotation, or center-based positioning.

---

Tests

They act as a safeguard against accidental changes in method logic.

```typescript
import { IAnimationFrame } from '../animator/IAnimationFrame'
import RendererV1 from '../animator/RendererV1'
import IVector2 from '../math/IVector2'
import Vector2 from '../math/Vector2'

describe('RendererV1', () => {
  let ctx: CanvasRenderingContext2D
  let renderer: RendererV1
  let image: HTMLImageElement
  let frame: IAnimationFrame
  let position: IVector2
  let scale: IVector2

  beforeEach(() => {
    // Mock the canvas context
    ctx = {
      drawImage: jest.fn(),
      save: jest.fn(),
      restore: jest.fn(),
      translate: jest.fn(),
      scale: jest.fn(),
      rotate: jest.fn(),
    } as unknown as CanvasRenderingContext2D

    renderer = new RendererV1()

    // Mock image and frame data
    image = new Image()
    frame = {
      framePosition: new Vector2(),
      frameSize: new Vector2(32, 32),
    }

    position = new Vector2(100, 50)
    scale = new Vector2(1, 1)
  })

  // Test Cases

  // Test for normal drawing
  it('should draw the image normally at the correct position', () => {
    renderer.drawNormal(ctx, image, frame, position, scale)

    // Verify the drawImage method was called with the correct arguments
    expect(ctx.drawImage).toHaveBeenCalledWith(
      image,
      0,
      0,
      32,
      32, // Frame's position and size
      100,
      50, // Corrected y-coordinate here
      32,
      32 // Image drawn with this size (frame size)
    )
  })

  // Test for flipped drawing
  it('should correctly flip the image horizontally', () => {
    renderer.drawFlipped(ctx, image, frame, position, scale)

    // Ensure that save and restore are called to avoid affecting other drawings
    expect(ctx.save).toHaveBeenCalled()
    expect(ctx.restore).toHaveBeenCalled()

    // Check if the canvas is translated and scaled for flipping
    expect(ctx.translate).toHaveBeenCalledWith(100 + 32, 50) // Corrected y-coordinate here
    expect(ctx.scale).toHaveBeenCalledWith(-1, 1)

    // Verify the drawImage method was called on the flipped coordinates
    expect(ctx.drawImage).toHaveBeenCalledWith(
      image,
      0,
      0,
      32,
      32, // Frame's position and size
      0,
      0, // Image should be drawn at position (0,0) due to translate
      32,
      32 // Image drawn with this size (frame size)
    )
  })
})
```
