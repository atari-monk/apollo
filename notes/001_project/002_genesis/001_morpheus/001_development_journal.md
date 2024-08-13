# `Morpheus` Development Journal

[Up](index.md)
[Main](../../../../index.md)

## 2024-08

25 hours 26 minutes

### 04

23:12 - 23:36, 23:36 - 23:56  
44 minutes

1. Add score display to scene `football_editor` 2.0.0.  
   Updated sytem id from `playerState` to `playerStateV1` in scenes 1.0.0.

2. Introduced this `Development Journal` doc.

---

### 05

12:20 - 12:42, 12:55 - 13:17, [13:47 - 14:54, 15:14 - 15:28], 16:15 - 17:30  
3 hours 20 minutes

1. Add script 'goto'. One word to open files.

2. Add `player movement` to scene `football` and `football_editor` 2.0.0.

3. Add `player movement animations` to scene `football` and `football_editor` 2.0.0.  
   Add scale multiplication to renderer fliping sprite.

4. Test `ballDribble` scene in `football_editor 2.0.0` scene.

---

### 06

09:59 - 10:20, [12:12 - 14:08, 15:06 - 15:28], 17:12 - 19:20, 21:52 - 22:32  
5 hours 27 minutes

1. Setup scene for `ballDribble` feature 2.0.0.
2. Fixing key toggles.
3. Investigate collision detection on scaled canvas, by rendering its elements.
4. Visualization of collision detection in fixed resolution.

---

### 07

13:07 - 13:29, [13:51 - 14:44, 15:58 - 16:33, 16:53 - 18:20]  
3 hours 17 minutes

1. Fix visualization of collision detection in fixed resolution.
2. Visualization of collision detection in scaled canvas.  
   Concluded that markers need to be fixed first.

---

### 08

12:25 - 14:19, [15:06 - 16:08, 16:32 - 17:07], 17:07 - 17:22, 18:14 - 19:15, 19:15 - 19:38  
4 hours 47 minutes

1. Fix bugs introduced by debug renders in collision detection.  
   Add document CanvasScaler.md.  
   Add scene `player` 1.0.0 with player features.

2. Fill scene `player` 1.0.0 with player features.
   Add documents `KeyboardMapping.md`, `SpriteRendererV1.md`, `DebugRenderer.md`, `MarkersRenderer.md`.  
   Fix keys for DebugRenderer and MarkersRenderer.

3. Refactor instance builder and validator for DebugRenderer and MarkersRenderer.

4. Add scene `player` 2.0.0 with player features.

5. Update `Development Journal` format.

### 12

17:51 - 18:47, 21:26 - 22:49, 22:49 - 23:43  
3 hours 13 minutes

1. Add documentation files, move from project.
2. Document markersV2 and use them in ballDribbleV2.
3. Script to calculate journal times using json.

### 13

10:47 - 12:38, [13:43 - 14:08, 14:20 - 14:48], 17:03 - 17:59, 19:06 - 19:41  
4 hours 15 minutes

1. Fix points rendering in `CenterCollisionWithScaling`.  
   Issues with points and rect rendering.
2. Investigate `CollisionBoxRenderer`.
3. Investigate `CenterCollisionWithScaling`. Fix calculations.
4. Investigate `BallDribble`.

[Up](index.md)
[Main](../../../../index.md)
