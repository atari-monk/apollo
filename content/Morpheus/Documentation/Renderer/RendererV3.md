### **Class Name:** `RendererV3`

---

### **1. Class Purpose**
- **Description:**
  This class is responsible for rendering images to a canvas, providing methods to draw images normally and flipped horizontally.  
  **It centers sprite around transform.position. Scales sprite. It does this by calculations.  It is deprecated as new versions donot use mannual calculations, but canvas transforms, to get same effects.**

---

### **2. Key Methods and Properties**
- **Primary Methods:**
  - `drawNormal(ctx: CanvasRenderingContext2D, image: HTMLImageElement, frame: IAnimationFrame, position: IVector2, scale: IVector2): void`
    - **Description:** Renders an image on the canvas at a specified position and scale, using a specific frame from an animation.
    - **Behavior:** The image is drawn centered on the specified position, adjusted for the frame size and scale.
    - **Returns:** `void`
  
  - `drawFlipped(ctx: CanvasRenderingContext2D, image: HTMLImageElement, frame: IAnimationFrame, position: IVector2, scale: IVector2): void`
    - **Description:** Renders an image flipped horizontally on the canvas.
    - **Behavior:** The method saves the current canvas state, applies a horizontal flip transformation, and then calls `drawNormal` to render the image. The canvas state is restored afterward.
    - **Returns:** `void`

- **Key Properties:**
  - None explicitly defined in this class.

---

### **3. Usage Examples**
- **Example 1:**
  Here’s how to use the `RendererV3` class to draw an image normally.

  ```typescript
  const renderer = new RendererV3();
  const canvas = document.getElementById('myCanvas') as HTMLCanvasElement;
  const ctx = canvas.getContext('2d');
  const image = new Image();
  image.src = 'path/to/image.png';
  
  const frame = {
      framePosition: new Vector2(0, 0),
      frameSize: new Vector2(100, 100),
  };
  
  const position = new Vector2(150, 150);
  const scale = new Vector2(1, 1);
  
  image.onload = () => {
      renderer.drawNormal(ctx, image, frame, position, scale);
  };
  ```

- **Example 2:**
  Here’s how to use the `RendererV3` class to draw an image flipped.

  ```typescript
  const renderer = new RendererV3();
  const canvas = document.getElementById('myCanvas') as HTMLCanvasElement;
  const ctx = canvas.getContext('2d');
  const image = new Image();
  image.src = 'path/to/image.png';
  
  const frame = {
      framePosition: new Vector2(0, 0),
      frameSize: new Vector2(100, 100),
  };
  
  const position = new Vector2(150, 150);
  const scale = new Vector2(1, 1);
  
  image.onload = () => {
      renderer.drawFlipped(ctx, image, frame, position, scale);
  };
  ```

---

### **4. Dependencies and Interactions**
- **Dependencies:**
  - `IRenderer` - This class implements the `IRenderer` interface.
  - `IAnimationFrame` - Required for defining frame properties used in rendering.
  - `IVector2` and `Vector2` - Used for managing vector positions and dimensions.

- **Interactions with Other Classes:**
  - Interacts with `CanvasRenderingContext2D` to perform drawing operations.
  - Uses `IAnimationFrame` to determine how to render frames from a sprite sheet.

---

### **5. Limitations and Assumptions**
- **Known Limitations:**
  - This class does not handle image loading errors; it assumes images are available before rendering.
  
- **Assumptions:**
  - It assumes that `frame` and `position` parameters are valid and properly defined.
  - It assumes that the context (`ctx`) is correctly set up before invoking the drawing methods.

---

### **6. Additional Notes (Optional)**
- Consider adding error handling for image loading and rendering.
- Future improvements may include supporting additional transformations or rotation capabilities.

---