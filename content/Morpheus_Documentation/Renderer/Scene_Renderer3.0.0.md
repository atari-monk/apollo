### **Scene Name:** `Scene Renderer 3.0.0`

---

### **1. Scene Overview**
- **Description:**
  This scene is designed to test the `RendererV3` system.  
  The key difference in this version is that the `transform.position` is rendered as the center of the sprite.  
  Sprite scaling is managed by the canvas scaler, but the scaling process is still performed manually through multiplication. This feature is deprecated.

- **Version:** `3.0.0`

---

### **2. Key Features**
- **Primary Elements:**
  - List and explain the primary elements within the scene, such as sprites, objects, or UI components.

    - **Element 1: Player1**
      - **Position:** Defined via `transform.position`.
      - **Description:** Rendered using the `transform.position` as the sprite's center.

    - **Element 2: Player2**
      - **Position:** Affected by canvas scaling.
      - **Description:** Scaled manually through multiplication with the canvas scale value, despite being influenced by `canvasScaler`.

- **Core System Components:**
  - `RendererV3 3.0.0`
    - **Description:** Renders the `transform.position` as the center of the sprite instead of the top-left corner.
  
  - `canvasScaler`
    - **Description:** Handles scene scaling, though scaling is still performed manually.

---

### **3. Behavior and Logic**
- **Special Behavior:**
  - **transform.position Rendering:** In this version, the `transform.position` is used as the center point for rendering the sprite rather than the top-left corner.
  - **Manual Sprite Scaling:** Sprite scaling is influenced by the `canvasScaler`, but scaling is manually done via multiplication.

- **Behavioral Notes:**
  - The use of manual multiplication for sprite scaling, despite the presence of the `canvasScaler`, is now considered deprecated. This method remains for reference and compatibility.

---

### **4. Usage and Configuration**
- **How to Load the Scene:**
  Provide instructions on how to configure and load this scene.

  ```json
  "select": {
      "folder": "engine",
      "subFolder": "",
      "scene": "renderer300"
  }
  ```

---

### **5. Dependencies and Interactions**
- **Dependencies:**
  - This scene depends on the `RendererV3` system and the `canvasScaler` component.

- **Interactions with Other Systems:**
  - The scene interacts with the `canvasScaler` to handle scene-wide scaling, though the manual sprite scaling conflicts with its automatic functionality.

---

### **6. Limitations and Assumptions**
- **Known Limitations:**
  - The sprite scaling process is inefficient due to the continued use of manual multiplication for scaling, despite the presence of the `canvasScaler`.

- **Assumptions:**
  - It is assumed that the canvas scaling will continue to be applied manually despite the inclusion of the `canvasScaler` for compatibility reasons.

---

### **7. Historical Notes (Optional)**
- **Reasoning for Deprecated/Legacy Features:**
  - The manual sprite scaling method has been deprecated in favor of more efficient practices, but it remains for backward compatibility and as a reference for understanding earlier design decisions.

---