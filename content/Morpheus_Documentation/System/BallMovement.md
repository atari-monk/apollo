### **Class Name:** `BallMovement`

---

### **1. Class Purpose**
- **Description:**
  This class manages the movement of an entity in a 2D space based on keyboard input. It updates the entity's velocity while preserving the direction based on the input keys (arrows).

---

### **2. Constructor**
- `constructor(entityCache: IEntityCache, logger: ILogger, input: IInputManager, eventSystem: IEventSystem)`
    - **Description:** Initializes a new instance of the `BallMovement` class, setting up the necessary dependencies.
    - **Parameters:**
        - `entityCache`: The cache of entities managed in the system.
        - `logger`: An instance of a logger for logging events and actions.
        - `input`: An input manager to handle keyboard interactions.
        - `eventSystem`: An event system for handling movement events.

---

### **3. Key Methods and Properties**
- **Primary Methods:**
- `OnLeft(id: string)`
    - **Description:** Sets the horizontal direction to left.
    - **Behavior:** Calls `sendMoveEvent` to notify movement.
- `OnRight(id: string)`
    - **Description:** Sets the horizontal direction to right.
    - **Behavior:** Calls `sendMoveEvent` to notify movement.
- `OnUp(id: string)`
    - **Description:** Sets the vertical direction to up.
    - **Behavior:** Calls `sendMoveEvent` to notify movement.
- `OnDown(id: string)`
    - **Description:** Sets the vertical direction to down.
    - **Behavior:** Calls `sendMoveEvent` to notify movement.
- `handleKeyDown(key: string, id: string, rigidBody: RigidBody, keyActions: KeyActionWithParamMap<string>)`
    - **Description:** Handles the key down event for movement.
    - **Behavior:** Invokes `handleKey` method to process key actions.
- `handleKeyUp(key: string, id: string, rigidBody: RigidBody, keyActions: KeyActionWithParamMap<string>)`
    - **Description:** Handles the key up event to reset directions.
    - **Behavior:** Resets `_directionX` and `_directionY` to 0.
- `handleKey(id: string, rigidBody: RigidBody, keyActions: KeyActionWithParamMap<string>)`
    - **Description:** Processes the currently pressed keys and updates the rigid body velocity.
    - **Behavior:** Applies directional velocity to the entity.

- **Key Properties:**
- `_directionX`
    - **Description:** Represents the current horizontal direction of movement.
    - **Behavior:** Value is set based on arrow key inputs (left/right).
- `_directionY`
    - **Description:** Represents the current vertical direction of movement.
    - **Behavior:** Value is set based on arrow key inputs (up/down).

---

### **4. Usage Examples**
- **Example 1:**
  Demonstrating the creation and usage of the `BallMovement` class.

    ```typescript
    const movement = new BallMovement(entityCache, logger, input, eventSystem);
    movement.OnLeft('entityId'); // Sets movement direction to left
    ```

- **Example 2 (Optional):**
  Showing the response to key events.

    ```typescript
    movement.handleKeyDown('ArrowUp', 'entityId', rigidBody, keyActions);
    movement.handleKeyUp('ArrowUp', 'entityId', rigidBody, keyActions);
    ```

---

### **5. Dependencies and Interactions**
- **Dependencies:**
  - `IEntityCache`: For managing entity data.
  - `ILogger`: For logging actions.
  - `IInputManager`: To handle input events.
  - `IEventSystem`: For sending movement events.
  - `RigidBody`: For applying physical properties to the entity.
  - `Vector2`: For handling 2D vectors.

- **Interactions with Other Classes:**
  - Interacts with `RigidBody` to update the velocity based on user input and movement events.

---

### **6. Limitations and Assumptions**
- **Known Limitations:**
  - Assumes that the keyboard input is the only method of movement control. Other input methods are not handled.
  
- **Assumptions:**
  - Assumes that the `RigidBody` has a `moveStep` property defined for velocity calculations.

---

### **7. Additional Notes (Optional)**
- Consider adding additional features such as diagonal movement or smoother acceleration in future versions.

---

### **8. Version**
- **Version Number:** 1.0.0
- **Last Modified:** 2024-10-04
