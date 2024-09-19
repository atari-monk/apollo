## SequentialAnimation Documentation

### Path

- `packages\engine\src\ecs_system\SequentialAnimation.ts`

### Related Paths

- `packages\engine\src\animator\AnimationState.ts`
- `packages\engine\src\animator\IAnimationStrategy.ts`

---

### Short Description

`SequentialAnimation` is a class that implements the `IAnimationStrategy` interface to provide a mechanism for updating animation frames sequentially based on elapsed time. It ensures that frames play in a linear order, looping back to the start after the last frame.

---

### Longer Description

The `SequentialAnimation` class handles the progression of animation frames by advancing the current frame index in a sequence based on the time passed since the last frame update. When the last frame of the animation is reached, it loops back to the first frame, creating a continuous animation cycle. This class is especially useful for non-repeating, linear animations or those that loop in a sequential order.

It interacts with the `AnimationState` to track the time between frames and the current frame index of the active animation.

---

### Constructor

`SequentialAnimation` does not require any parameters for its constructor as it simply implements the `update` method defined by the `IAnimationStrategy` interface.

---

### Methods

#### 1. **update**

```typescript
update(deltaTime: number, state: AnimationState): void
```

- **Description**:
  - This method updates the current animation frame based on the elapsed time (`deltaTime`). It checks whether enough time has passed to move to the next frame. If so, it increments the `currentFrameIndex` or loops back to the first frame if the animation has reached its end.
- **Parameters**:
  - `deltaTime: number`: The time that has passed since the last update, in milliseconds.
  - `state: AnimationState`: The current state of the animation, which includes the current frame index, the duration of each frame, and timing data.
- **Functionality**:
  - Increments the `timeSinceLastFrame` by the value of `deltaTime`.
  - If the accumulated time exceeds the duration of the current frame (`frameDuration`), it moves to the next frame.
  - Resets the frame index to 0 if the last frame of the animation has been reached, ensuring the animation loops continuously.
  - Resets `timeSinceLastFrame` after switching to the next frame to ensure accurate timing for the next update.

---

### Example Usage

```typescript
const sequentialAnimation = new SequentialAnimation()
sequentialAnimation.update(deltaTime, animationState)
```

- This updates the current animation state, advancing to the next frame if enough time has passed since the last update.

---

### Dependencies

- **IAnimationStrategy**:
  - Interface that defines the structure for animation strategies. `SequentialAnimation` implements the `update` method required by this interface.
- **AnimationState**:
  - Manages the current state of the animation, including the current frame, frame durations, and time tracking between frame updates.

---

### Conclusion

`SequentialAnimation` provides a simple and efficient way to manage frame updates for sequential animations. It is ideal for animations that need to play in a linear order, looping continuously. This class forms a crucial part of any sprite animation system, particularly in game development and other 2D rendering applications.