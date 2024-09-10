# `Morpheus` Development Journal

## 2024-08

83 hours 7 minutes

### 04

23:12 - 23:36, 23:36 - 23:56  
44 minutes

1. Add score display to scene `football_editor` 2.0.0.  
   Updated sytem id from `playerState` to `playerStateV1` in scenes 1.0.0.

2. Introduced this `Development Journal` doc.

### 05

12:20 - 12:42, 12:55 - 13:17, [13:47 - 14:54, 15:14 - 15:28], 16:15 - 17:30  
3 hours 20 minutes

1. Add script 'goto'. One word to open files.

2. Add `player movement` to scene `football` and `football_editor` 2.0.0.

3. Add `player movement animations` to scene `football` and `football_editor` 2.0.0.  
   Add scale multiplication to renderer fliping sprite.

4. Test `ballDribble` scene in `football_editor 2.0.0` scene.

### 06

09:59 - 10:20, [12:12 - 14:08, 15:06 - 15:28], 17:12 - 19:20, 21:52 - 22:32  
5 hours 27 minutes

1. Setup scene for `ballDribble` feature 2.0.0.
2. Fixing key toggles.
3. Investigate collision detection on scaled canvas, by rendering its elements.
4. Visualization of collision detection in fixed resolution.

### 07

13:07 - 13:29, [13:51 - 14:44, 15:58 - 16:33, 16:53 - 18:20]  
3 hours 17 minutes

1. Fix visualization of collision detection in fixed resolution.
2. Visualization of collision detection in scaled canvas.  
   Concluded that markers need to be fixed first.

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

### 14

11:56 - 12:42, 12:42 - 14:10, 16:57 - 18:28, 19:06 - 19:48  
4 hours 27 minutes

1. Upgrade script printing file system.
2. Clean docs folder.
3. BallDribbleFactory.
4. BallDribbleWithScaling.

### 15

14:38 - 15:37, [16:37 - 17:54, 22:49 - 00:00]  
3 hours 26 minutes

1. Realized mistake in rendering.
2. Scene in version 3.0.0. Refactor to introduce new renderer.

### 16

13:31 - 14:05, 15:15 - 15:52  
x hours x minutes

1. Stash changes, that broke football 1.0.0 scene, proved it was these changes.
2. Turned out that flipped renderer had NormalDraw() on 0,0.  
   I have put position param there by mistake.  
   It takes 0,0 becouse translation() before uses position to translate canvas.

### 21

13:35 - 15:27  
1 hours 52 minutes

1. Fixed bugs. Investigated state of project.

### 22

21:03 - 23:30
2 hours 27 minutes

1. Flatten folders for sys builder. Docs.

### 23

18:17 - 20:11, 21:21 - 00:17
4 hours 50 minutes

1. SceneRenderer version in json.

### 24

00:23 - 01:27,
1 hours 4 minutes

1. Move one system.

### 25

[16:07 - 17:40, 22:11 - 01:00]
4 hours 22 minutes

1. Refactoring.  
   Flattening folders according to policy.  
   Factories with new system data features that control version,  
   isOn and sys additional features flags.

### 26

[11:47 - 12:50, 14:03 - 14:57, 15:25 - 15:55, 17:05 - 17:54, 20:14 - 21:00], 21:00 - 22:12
5 hours 14 minutes

1. Finished refactoring scene 1.0.0 to new system standard.
2. Finished refactoring scene 2.0.0 to new system standard.

### 27

[12:53 - 17:02, 22:03 - 23:03]
5 hours 9 minutes

1. Flattened assets folders in client. Fixing data to new system file standard.

### 28

14:12 - 15:06, 16:42 - 18:00, 18:43 - 19:35, 20:32 - 22:33, 23:30 - 01:41
7 hours 16 minutes

1. Flattened assets folders in client. Fixing data to new system file standard.

### 29

11:38 - 12:52, 15:18 - 16:40, 18:39 - 19:43, 22:10 - 23:36
5 hours 6 minutes

1. Finished with refactoring data.
2. Flattened file system to 1 level nearly evrywhere, some 2 level, max 3 level.
3. Removed wrappers on socket-io. Tested client, server sync.
4. Optimizing sprite renderer v1.

### 30

[15:06 - 16:22, 16:56 - 17:58], [19:34 - 20:59, 22:32 - 23:48]
4 hours 59 minutes

1. Introduce prototypes for spriteRenderer.
2. Refactoring versions of spriteRenderer, decluttering.

### 31

12:55 - 14:54, 18:40 - 20:00, 20:11 - 21:37, 22:51 - 00:24
6 hours 18 minutes

1. Fix data after consolidating spriteRenderer versions.
2. Addig scenes for version 3.0.0.
3. Setup sprite 3.0.0 scene.
4. More 3.0.0 scenes.

## 2024-09

38 hours 1 minutes

### 1

14:00 - 15:28, 15:29 - 18:17, 22:53 - 00:10, 00:10 - 00:46
6 hours 9 minutes

1. Scene football_editor 3.0.0. DrawDirection. Working on this is hell, need refactor.
2. Refactored system validation.
3. Refactored system validation, finish.
4. Refactored tests.

### 2

11:58 - 13:00, 13:21 - 14:03, 23:23 - 00:16
2 hours 37 minutes

1. Setup version 4.0.0, this should be more robust. To heal form 1-3.
2. RendererV4, worked, now need of test, refactor.
3. Add new scene, prepare scene rendering campaing.

### 3

15:07 - 15:38, 16:47 - 18:24, 20:23 - 22:12
3 hours 57 minutes

1. SpriteRendererV4, SpriteAnimatorV4 refactor.
2. Fix bug.
3. Improved Render2 scene. Bug fixing for SpriteRendererV4, SpriteAnimatorV4.
   todo: fixes, refactor, tests

### 4

13:40 - 19:22
5 hours 42 minutes

1. Unit test, scene slideshow, footballv4 feaure published as github page.

### 5

10:41 - 13:45, 14:01 - 14:53, 17:39 - 20:32
6 hours 49 minutes

1. First session. Bunch fixes/upgrades to football 4.0.0 scenes.
2. Scene 3, field colliders.
3. Scene 4, got a little lost adding to already working version  
   and that can lose time by breaking it and not gaining new feature,  
   thats way its good to use new versions.

### 6

16:22 - 17:30, 18:12 - 19:07, 23:02 - 00:22
3 hours 23 minutes

1. Scene5, goal posts.
   - todo: problem with ordering of renderers
2. Scene6-8, players, ball, score.

### 7

14:06 - 14:45, 14:46 - 14:59
0 hours 52 minutes

1. Ordered scenes 4.0.0, published slideshow, todo: make some resource cache so slideshow  
   dosent transfer so much data.
2. Scene with ball dribble. Works in scale 1,1.

### 9

10:48 - 11:51, 11:51 - 12:36, 19:57 - 21:17
3 hours 8 minutes

1. Creating script to request viewer count from twitch api with chatgpt,  
   got result, than failed reset, after showing my keys on stream.
2. Player04 scene. Feature - kick ball.
3. Player05 scene, draw Direction, mouse coordinates scaled.

### 10

10:30 - 11:16, 13:55 - 16:17, 16:17 - 17:48, 22:33 - 23:18
5 hours 24 minutes

1. Ecs systems for drawing scaling velocity and point.
2. Mending rendering methods for v 4.0.0.
3. Updating times script and data.
4. fillCenteredRectScaling method.

Feeling:, Productivity:
