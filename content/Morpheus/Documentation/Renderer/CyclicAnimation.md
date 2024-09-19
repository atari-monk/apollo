## CyclicAnimation Documentation

### Path

- `packages\engine\src\ecs_system\CyclicAnimation.ts`

### Related Paths

- `packages\engine\src\animator\AnimationState.ts`
- `packages\engine\src\animator\IAnimationStrategy.ts`

---

### Short Description

`CyclicAnimation` is a class that implements the `IAnimationStrategy` interface to manage frame updates in a cyclic manner, where the animation alternates between forward and backward frame progression, creating a ping-pong animation effect.

---

### Longer Description

The `CyclicAnimation` class provides a mechanism to animate frames in a cyclic (ping-pong) sequence, advancing frames forward until the last frame is reached, and then reversing the direction to go backward through the frames. It continuously toggles between forward and backward animation, creating a smooth looping effect.

This behavior is achieved by tracking whether the animation is progressing forward or backward using the `isForward` flag in the `AnimationState`. It is useful for animations that require a back-and-forth movement, such as breathing effects or pendulum-like motions.

---

### Constructor

`CyclicAnimation` does not require any parameters for its constructor, as it only implements the `update` method as part of the `IAnimationStrategy` interface.

---

### Methods

#### 1. **update**

```typescript
update(deltaTime: number, state: AnimationState): void
```

- **Description**:
  - This method updates the current frame of the animation based on the elapsed time (`deltaTime`), moving forward or backward through the frames depending on the `isForward` state. It toggles the direction once the first or last frame is reached.
- **Parameters**:
  - `deltaTime: number`: The time passed since the last update, in milliseconds.
  - `state: AnimationState`: The current state of the animation, containing the frame data, duration, and time since the last frame change.
- **Functionality**:
  - Increments `timeSinceLastFrame` by `deltaTime`.
  - If the accumulated time exceeds the frame duration (`frameDuration`), it advances the frame.
  - When in the forward state (`isForward = true`), it increments the `currentFrameIndex` until the last frame is reached.
  - Once the last frame is reached, it toggles the direction (`isForward = false`) and starts decrementing the frame index.
  - When the first frame is reached, it toggles back to the forward direction (`isForward = true`).
  - Resets `timeSinceLastFrame` after each frame change to ensure proper timing for the next update.

---

### Example Usage

```typescript
const cyclicAnimation = new CyclicAnimation()
cyclicAnimation.update(deltaTime, animationState)
```

- This call updates the current animation state, toggling the frame index forward or backward based on the current direction and elapsed time.

---

### Dependencies

- **IAnimationStrategy**:
  - The interface that defines the required `update` method for animation strategies. `CyclicAnimation` implements this to create a cyclic update mechanism.
- **AnimationState**:
  - Manages the animation's current frame, direction (forward or backward), and timing data.

---

### Conclusion

`CyclicAnimation` offers an efficient and flexible way to implement ping-pong style animations, where frames are cycled forward and then backward in a loop. This class is particularly useful for animations with smooth oscillating effects, commonly found in character breathing animations, pendulum movements, or other repetitive actions that need to reverse direction.