### **Class Name:** `RendererV2`

---

### **1. Class Purpose**
- **Description:**
  The `RendererV2` class is responsible for rendering images (frames) onto an HTML5 canvas, providing functionality for both normal and horizontally flipped drawings. It integrates with the canvas' `2D` context to draw frames at specific positions and scales.

---

### **2. Key Methods and Properties**
- **Primary Methods:**
  - `drawNormal(ctx: CanvasRenderingContext2D, image: HTMLImageElement, frame: IAnimationFrame, position: IVector2, scale: IVector2)`
    - **Description:** Renders an image frame onto the canvas in its normal orientation.
    - **Behavior:** Draws a specific portion of the image (`frame`) at a defined position and scale on the canvas. The position is multiplied by the scaling factor to ensure proper sizing.
    - **Returns:** `void` (no return value).
    - **Exceptions:** No explicit exceptions, but incorrect input values (e.g., invalid canvas context or image) may result in rendering errors.
  
  - `drawFlipped(ctx: CanvasRenderingContext2D, image: HTMLImageElement, frame: IAnimationFrame, position: IVector2, scale: IVector2)`
    - **Description:** Renders an image frame onto the canvas with a horizontal flip.
    - **Behavior:** Transforms the canvas context by translating and scaling it to flip the image horizontally. After drawing, it restores the canvas' original state. Uses `drawNormal` internally for the actual rendering.
    - **Returns:** `void` (no return value).
    - **Exceptions:** As with `drawNormal`, improper input values could cause rendering issues.

- **Key Properties:**
  This class does not define any instance properties.

---

### **3. Usage Examples**
- **Example 1:**
  Rendering a normal image frame on the canvas.

    ```typescript
    const renderer = new RendererV2();
    renderer.drawNormal(ctx, image, frame, position, scale);
    ```

- **Example 2:**
  Rendering a flipped image frame on the canvas.

    ```typescript
    const renderer = new RendererV2();
    renderer.drawFlipped(ctx, image, frame, position, scale);
    ```

---

### **4. Dependencies and Interactions**
- **Dependencies:**
  - `IRenderer`: An interface that `RendererV2` implements.
  - `IAnimationFrame`: Defines the structure of the animation frame containing the frame's position and size.
  - `IVector2`: A vector interface for representing two-dimensional positions and sizes.
  - `Vector2`: A vector utility class that provides helper functions like `zero`.

- **Interactions with Other Classes:**
  - This class interacts with the `CanvasRenderingContext2D` to manipulate the canvas for drawing and transformations.
  - Uses `Vector2.zero` to manage coordinate transformations when flipping images.

---

### **5. Limitations and Assumptions**
- **Known Limitations:**
  - This class does not support rotation or other advanced transformations beyond flipping.
  - Designed to work with 2D contexts only (e.g., `CanvasRenderingContext2D`).

- **Assumptions:**
  - It is assumed that the `image`, `frame`, and other parameters are correctly defined and validated before being passed to the methods.
  - Assumes that the `scale` values are positive and properly defined to avoid rendering issues.

---

### **6. Additional Notes (Optional)**
- Future versions of this class could include more advanced rendering features such as rotation or color manipulation.
- Compatible with most modern browsers that support the HTML5 canvas API.

---