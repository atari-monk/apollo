### **Class Name:** `DrawSpritePoints`

---

### **1. Class Purpose**
- **Description:**  
  `DrawSpritePoints` is responsible for rendering specific points of a sprite, such as its top-left corner and center.  
  It provides functionality to display these points based on keyboard input, leveraging an entity-component-system (ECS) framework.  
  The points are drawn at specific positions scaled according to the canvas and entity's transformation.  
  **Acctually there allready is DrawTransformPositionV1, DrawTransformPositionV2.**  
  This class may be to upgrade or remove.

---

### **2. Key Methods and Properties**

- **Primary Methods:**
  - `constructor(entityCache: IEntityCache, _renderer: IRenderer, _keyboardActionHandler?: KeyboardActionHandler)`
      - **Description:** Initializes the `DrawSpritePoints` system with an entity cache, renderer, and an optional keyboard action handler.
      - **Behavior:** Retrieves the canvas scale and sets up the keyboard handler to toggle the visibility of sprite points on initialization.
      - **Exceptions:** Throws errors if the canvas entity or scale is not found.

  - `start(): void`
      - **Description:** Overrides the base `System`'s `start` method to execute the initial toggle of sprite point visibility if the keyboard handler is activated.
      - **Behavior:** Automatically switches the visibility of the points if the `switchIt` method is triggered by the keyboard.

  - `startEntity(entity: IEntity): void`
      - **Description:** Initializes the sprite point cache for each entity, storing its transform, sprite, and calculated positions.
      - **Behavior:** Retrieves and caches the entity's `Sprite`, `Transform`, and initializes the vectors for top-left and center positions.
      - **Returns:** None.

  - `updateEntity(entity: IEntity, _deltaTime: number): void`
      - **Description:** Updates the position of the sprite's top-left and center points based on the entity's transformation and canvas scale.
      - **Behavior:** Calculates the updated positions for the top-left and center points of the sprite and stores them in the cache.
      - **Returns:** None.

  - `renderEntity(entity: IEntity, _deltaTime: number): void`
      - **Description:** Renders the sprite's top-left and center points on the canvas, depending on the sprite's flags.
      - **Behavior:** Draws points at the top-left and center positions if their visibility flags (`PointFlag.ShowTopLeft`, `PointFlag.ShowCenter`) are enabled.
      - **Returns:** None.

  - `switchIt(): void`
      - **Description:** Toggles the visibility of the sprite's top-left and center points by flipping their corresponding flags.
      - **Behavior:** Switches the visibility flags for the top-left and center points in all cached sprites.
      - **Returns:** None.

  - `getCanvasScale(): CanvasScale`
      - **Description:** Retrieves the canvas scale from the `canvas` entity.
      - **Behavior:** Looks up the `CanvasScale` component from the canvas entity in the entity cache.
      - **Returns:** The `CanvasScale` component used to adjust the scaling of points during rendering.

- **Key Properties:**
  - `_canvasScale`
      - **Description:** Represents the scaling factor applied to rendering on the canvas.
      - **Behavior:** Fetched from the `canvas` entity and used to scale the position of points during rendering.

  - `_cache`
      - **Description:** A map storing each entity's sprite, transformation, and positions of key points (top-left and center).
      - **Behavior:** Used to store and retrieve sprite-related data for rendering and updating each entity.

  - `_pressOnceOnStart`
      - **Description:** A flag that determines whether the visibility of points should be toggled immediately upon start.
      - **Behavior:** Controlled by the `KeyboardActionHandler` and used to toggle the sprite point visibility once at the start of the system.

---

### **3. Usage Examples**

- **Example 1:**
```typescript
const drawSpritePoints = new DrawSpritePoints(entityCache, renderer, keyboardActionHandler);

// Adding an entity
const entity = ... // Some entity setup
drawSpritePoints.startEntity(entity);

// In the update loop
drawSpritePoints.updateEntity(entity, deltaTime);

// In the render loop
drawSpritePoints.renderEntity(entity, deltaTime);
```

- **Example 2 (Keyboard interaction):**
```typescript
// Automatically toggle sprite point visibility on keyboard press
keyboardActionHandler.initKeyboardKey(() => drawSpritePoints.switchIt());

// In the game loop
drawSpritePoints.updateEntity(entity, deltaTime);
drawSpritePoints.renderEntity(entity, deltaTime);
```

---

### **4. Dependencies and Interactions**
- **Dependencies:**
  - `Sprite`: Represents the visual sprite component, including animation frames and custom flags.
  - `IEntityCache`: Manages entity lookups.
  - `CanvasScale`: Handles scaling of canvas rendering.
  - `Transform`: Represents the position, rotation, and scaling of entities.
  - `KeyboardActionHandler`: Manages keyboard input interactions.
  - `Vector2`: Utility for 2D vector math.
  - `IRenderer`: Provides rendering functionality, including methods to draw points on the canvas.
  - `IPointOptions`: Interface that defines options for rendering points, such as color and size.
  
- **Interactions with Other Classes:**
  - Interacts with `Sprite`, `Transform`, and `CanvasScale` components of entities to calculate and render the key points (top-left and center).
  - Listens to keyboard inputs via `KeyboardActionHandler` to toggle point visibility.

---

### **5. Limitations and Assumptions**
- **Known Limitations:**
  - This class assumes that the entities have valid `Sprite` and `Transform` components. Missing components may cause errors.
  - It assumes that sprites have defined flags for controlling the visibility of points (`ShowTopLeft`, `ShowCenter`).
  - This system does not support complex multi-threaded environments or concurrent rendering loops.

- **Assumptions:**
  - It assumes that the `KeyboardActionHandler` is correctly initialized if keyboard input is used.
  - The canvas entity and its `CanvasScale` component are assumed to be present in the entity cache.

---

### **6. Additional Notes (Optional)**
- Future improvements could include customizable keyboard controls for toggling specific points, or support for more complex sprite point calculations (e.g., bottom-right corner).
- This system might also benefit from enhanced validation to handle missing components more gracefully.

---