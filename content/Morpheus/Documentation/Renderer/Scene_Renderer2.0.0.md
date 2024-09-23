### **Scene Name:** `Renderer2.0.0`

---

### **1. Scene Overview**
- **Description:**
  This scene is designed to test the `RendererV2` and `SpriteRendererV2` systems.  
  It demonstrates how `transform.position` is used for positioning the top-left corner of a sprite and includes testing of sprite flipping.  
  Unlike version 1.0.0, `spriteOffset` is deprecated, and the center of the sprite is now calculated in multiple systems.  
  **This need to calculate stuff is removed in newer versions. This one is kept for record.**

- **Version:** `2.0.0`

---

### **2. Key Features**
- **Primary Elements:**
  - List and explain the primary elements within the scene, such as sprites, objects, or UI components.

	- **Element 1: Player1**
	  - **Position:** `430, 540`
	  - **Description:** Rendered to demonstrate that `transform.position` places the sprite at the top-left corner.

	- **Element 2: Player2**
	  - **Position:** _Defined via transform.position._
	  - **Description:** Rendered to test horizontal sprite flipping. Sprite flipping has been improved in this version without the need for a `spriteOffset` property.
	  
- **Core System Components:**
  - `RendererV2 2.0.0`
	- **Description:** Renders the transform position from the top-left corner of the sprite, with enhanced sprite flipping and centering.

  - `SpriteRendererV2`
	- **Description:** New version of the sprite renderer, now without the use of `sprite.spriteOffset`, as sprite centering is calculated internally.

---

### **3. Behavior and Logic**
- **Special Behavior:**
  - **SpriteRendererV2 Positioning:** The system renders `transform.position` as the top-left point of the sprite, with no need for manual offset adjustments.
  - **Horizontal Sprite Flip:** Player2 demonstrates the horizontal sprite flipping functionality of `RendererV2`.
  
- **Behavioral Notes:**
  - The use of `sprite.spriteOffset` has been deprecated as centering is handled automatically in `RendererV2` and related systems. This is a key improvement over version 1.0.0.

---

### **4. Usage and Configuration**
- **How to Load the Scene:**
  Provide instructions on how to configure and load this scene.

	```json
	"select": {
		"folder": "engine",
		"subFolder": "",
		"scene": "renderer200"
	}
	```

---

### **5. Dependencies and Interactions**
- **Dependencies:**
  - Depends on the `RendererV2` system and `SpriteRendererV2` for rendering and sprite handling.
  
- **Interactions with Other Systems:**
  - This scene interacts with systems that rely on sprite positioning and flipping, including player controls and animation systems.

---

### **6. Limitations and Assumptions**
- **Known Limitations:**
  - No sprite offset functionality is available in this version. All centering is handled by internal calculations.
  
- **Assumptions:**
  - Assumes that sprite flipping will only require horizontal orientation. Vertical flipping may require additional configuration if needed.

---

### **7. Historical Notes (Optional)**
- **Reasoning for Deprecated/Legacy Features:**
  - The `sprite.spriteOffset` was removed as the system now calculates sprite centering in many subsystems. Kept as a reference for legacy purposes.

--- 