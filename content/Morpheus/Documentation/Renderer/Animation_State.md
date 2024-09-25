### **Class Name:** `AnimationState`

---

### **1. Class Purpose**
- **Description:**
  This class manages the state of animations, including the current frame index, the time elapsed since the last frame, and the direction of the animation playback. It enables smooth transitions between frames and supports multiple animations.

---

### **2. Key Methods and Properties**
- **Primary Methods:**
  - *(No methods currently defined in the class; consider adding methods for frame updates, animation playback control, etc.)*

- **Key Properties:**
  - `currentFrameIndex`
    - **Description:** Represents the index of the current frame being displayed in the animation.
    - **Behavior:** This property updates based on the progression of time and direction of the animation.
    
  - `timeSinceLastFrame`
    - **Description:** The time elapsed since the last frame was displayed.
    - **Behavior:** This value is used to determine when to switch to the next frame based on the defined frame durations.
    
  - `isForward`
    - **Description:** Indicates the direction of the animation playback (forward or backward).
    - **Behavior:** This affects how the `currentFrameIndex` is updated during playback.
    
  - `currentAnimationIndex`
    - **Description:** The index of the currently playing animation from the list of animations.
    - **Behavior:** Changes when switching between different animations defined in the `animations` property.

---

### **3. Usage Examples**
- **Example 1:**
  Demonstrates how to create an instance of `AnimationState` and initialize it with frame durations and animations.

  ```javascript
  const frameDurations = [100, 200, 150]; // Duration of each frame in milliseconds
  const animations = [
    [/* IAnimationFrame data for animation 1 */],
    [/* IAnimationFrame data for animation 2 */],
  ];

  const animationState = new AnimationState(frameDurations, animations);
  console.log(animationState.currentFrameIndex); // Output: 0
  ```

- **Example 2 (Optional):**
  Shows an advanced use case where the current animation index and frame index are set.

  ```javascript
  const animationState = new AnimationState(frameDurations, animations, 1, 0);
  animationState.timeSinceLastFrame = 50; // Time elapsed since last frame
  console.log(animationState.isForward); // Output: true
  ```

---

### **4. Dependencies and Interactions**
- **Dependencies:**
  - This class relies on the `IAnimationFrame` interface for defining the structure of animation frames.

- **Interactions with Other Classes:**
  - This class is likely to interact with animation controllers or renderers that utilize the animation state to display frames based on the current state.

---

### **5. Limitations and Assumptions**
- **Known Limitations:**
  - This class does not currently implement methods for updating the animation state or transitioning between frames. Additional functionality will be required for complete animation control.

- **Assumptions:**
  - It assumes that the `frameDurations` array has the same length as the frames in each animation and that the `animations` array contains valid `IAnimationFrame` data.

---

### **6. Additional Notes (Optional)**
- Future improvements could include adding methods for starting, stopping, and updating animations based on time, as well as handling user input for animation control.

---