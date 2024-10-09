### **Scene Name:** Animator

---

### **1. Scene Overview**

- **Description:**
  This scene is designed to test the animator, focusing on player sprites and ball animations. It enables animation switching for four player characters and a ball. Additionally, it includes flags in the entity JSON files for sprite centering, scaling, and canvas auto-scaling.  
  TODO: Add UI components to test these flags by reloading scene switching flags.

- **Version:** `1.0.0`

---

### **2. Key Features**

- **Primary Elements:**

  - **Element 1: Player1**
    - **Position:** `760, 340`
    - **Description:** A red player sprite with animation capabilities, rendered with a scale of 2x.
  - **Element 2: Player2**
    - **Position:** `1160, 340`
    - **Description:** A flipped red player sprite to demonstrate animation and state transitions.
  - **Element 3: Player3**
    - **Position:** `760, 740`
    - **Description:** A blue player sprite for testing animation switching and scaling.
  - **Element 4: Player4**
    - **Position:** `1160, 740`
    - **Description:** A flipped blue player sprite to test animation states.
  - **Element 5: Ball**
    - **Position:** `960, 540`
    - **Description:** A ball sprite with animation features to evaluate animation transitions.

- **Core System Components:**
  - `canvasScaler 1.0.0`
    - **Description:** Manages scaling for the scene, including auto-scaling features.
  - `keyboardMapping 1.0.0`
    - **Description:** Handles input mapping for UI interactions.
  - `spriteRenderer 2.0.0`
    - **Description:** Renders player and ball sprites, including animation support.
  - `drawTransformPosition 2.0.0`
    - **Description:** Visualizes the transform position of entities in the scene.

---

### **3. Behavior and Logic**

- **Special Behavior:**

  - **Animation Switching:** Players can switch between different animations based on their states (e.g., idle, moving).
  - **Flags in JSON:** Flags in the entity JSON files control sprite centering, scaling, and canvas auto-scaling, influencing how sprites are rendered in relation to the scene.

- **Behavioral Notes:**
  - Initial design considerations include the implementation of animation states and the use of flags for configuration. This allows for flexible adjustments based on scene requirements.

---

### **4. Usage and Configuration**

- **How to Load the Scene:**
  Provide instructions on how to configure and load this scene.

  ```json
  "select": {
      "folder": "engine/renderer/animator",
      "subFolder": "",
      "scene": "YourSceneName"
  }
  ```

---

### **5. Dependencies and Interactions**

- **Dependencies:**

  - Depends on the `canvasScaler`, `keyboardMapping`, and `spriteRenderer` systems to function properly.

- **Interactions with Other Systems:**
  - The scene interacts with the UI system to allow for user inputs and control over animation states, as well as the rendering system for visual representation of sprites.

---

### **6. Limitations and Assumptions**

- **Known Limitations:**

  - The current implementation may not fully utilize optimal animation management techniques due to legacy design choices.

- **Assumptions:**
  - Assumes that the flags in the JSON files will correctly influence the rendering and behavior of sprites based on user input and configuration.

---

### **7. Historical Notes (Optional)**

- **Reasoning for Deprecated/Legacy Features:**
  - Some legacy features have been kept for reference and educational purposes, helping to illustrate design decisions that could be improved in future iterations.

---
