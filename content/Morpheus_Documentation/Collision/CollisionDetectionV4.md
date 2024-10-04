### **Class Name:** `CollisionDetectionV4`

---

### **1. Class Purpose**
- **Description:**
  `CollisionDetectionV4` is responsible for detecting collisions between two rectangular objects. It can use either the center or the corner of each object as the reference point for collision detection, and it supports debugging visualization by drawing the collision rectangles.

---

### **2. Constructor**
- `__init__(_entityCache, _renderer, options = {})`
    - **Description:** Initializes the `CollisionDetectionV4` class by setting up the entity cache and renderer, and configuring options for collision detection.
    - **Parameters:**
        - `_entityCache`: An instance of `IEntityCache` used to retrieve entities, such as the canvas, for scaling purposes.
        - `_renderer`: An instance of `IRenderer` used to render debug visuals (if enabled).
        - `options`: An optional object to configure the behavior of the collision detection algorithm.
            - `useCenter`: (Optional) Boolean flag to determine if the center of the objects should be used for collision detection. Defaults to `false`.
            - `isDebugMode`: (Optional) Boolean flag to enable or disable drawing the collision rectangles for debugging purposes. Defaults to `false`.

---

### **3. Key Methods and Properties**

- **Primary Methods:**

  - `start(collision)`
    - **Description:** Initializes the collision detection process by retrieving the position, size, half-size, and optional center of both objects involved in the collision.
    - **Behavior:** Sets up the rectangles (`_rect1` and `_rect2`) used for collision detection, with the option to use the center of the objects for their position.
    - **Returns:** None.
    - **Exceptions:** Throws an error if the necessary components (e.g., `CanvasScale`) are not found in the entity cache.

  - `isColliding()`
    - **Description:** Performs the collision detection logic, comparing the positions and sizes of the two rectangles.
    - **Behavior:** Determines if the two rectangles overlap by comparing their positions and half-sizes. The method checks if their edges are crossing each other, indicating a collision.
    - **Returns:** A boolean value indicating whether the two objects are colliding (`true` if they are colliding, `false` otherwise).
    - **Exceptions:** None.

  - `draw(collision)`
    - **Description:** Draws the two rectangles involved in the collision on the canvas for debugging purposes.
    - **Behavior:** If debug mode is enabled, it calls the renderer to draw filled rectangles representing the collision objects on the canvas. The rectangles are scaled based on the canvas scale factor.
    - **Returns:** None.
    - **Exceptions:** None.

- **Key Properties:**

  - `_rect1` and `_rect2`
    - **Description:** Represent the rectangular boundaries of the two objects involved in the collision.
    - **Behavior:** These properties are dynamically set during the `start()` method and used in collision detection and drawing. They store the position, size, and half-size of each object.

  - `_canvasScale`
    - **Description:** Stores the scale factor of the canvas, which is retrieved from the `CanvasScale` component of the canvas entity.
    - **Behavior:** Used in the `draw()` method to ensure the rectangles are drawn at the correct scale.

  - `_useCenter`
    - **Description:** A boolean flag indicating whether to use the center of objects for collision detection.
    - **Behavior:** If `true`, the center of the objects is added to their position when setting up the rectangles.

  - `_isDebugMode`
    - **Description:** A boolean flag to enable or disable debug drawing.
    - **Behavior:** When `true`, the `draw()` method renders the rectangles to the canvas. Otherwise, no drawing occurs.

---

### **4. Usage Examples**

- **Example 1:**
  Demonstrates how to initialize the collision detection class and check for collisions between two objects.

    ```typescript
    const collisionDetection = new CollisionDetectionV4(entityCache, renderer, { useCenter: true, isDebugMode: true })
    collisionDetection.start(collision)
    const isColliding = collisionDetection.isColliding()
    console.log(`Are the objects colliding? ${isColliding}`)
    ```

- **Example 2 (Optional):**
  Demonstrates using the class with debug mode enabled to visually represent collisions.

    ```typescript
    const collisionDetection = new CollisionDetectionV4(entityCache, renderer, { isDebugMode: true })
    collisionDetection.start(collision)
    collisionDetection.draw(collision)
    ```

---

### **5. Dependencies and Interactions**

- **Dependencies:**
  - `IEntityCache`: Used to retrieve the canvas entity for determining the canvas scale.
  - `IRenderer`: Responsible for rendering the rectangles to the canvas in debug mode.
  - `CanvasScale`: A component required to determine the scaling factor for the canvas.
  - `ICollision`: Provides the data structure for collision information, including object positions and sizes.

- **Interactions with Other Classes:**
  - Interacts with the `ICollision` interface to retrieve collision data.
  - Uses `IRect`, `IRectOptions`, and `Vector2` for handling rectangle geometry and rendering.

---

### **6. Limitations and Assumptions**
- **Known Limitations:**
  - Assumes that both objects have rectangular colliders (`IRect`), which limits the algorithm's applicability to other shapes.
  - The class is designed for use in a single-threaded environment.
  - No support for detecting collisions between more than two objects at once.

- **Assumptions:**
  - It assumes that the positions and sizes of the objects are provided in a valid format.
  - Assumes that the `CanvasScale` component exists on the canvas entity, and if not, an error will be thrown.

---

### **7. Additional Notes (Optional)**
- Future improvements could include support for additional shapes and concurrent collision detection.
- Debug mode adds overhead to the rendering process, so it should be disabled in production.

---

### **8. Version**
- **Version Number:** 1.0.0
- **Last Modified:** 2024-10-05

---