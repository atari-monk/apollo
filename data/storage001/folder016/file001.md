# 2024-09

## 2

### Please answear with no more text than 4x question text.

Sure! What’s your question?

### I can have my calculations done in resolution 1920x1080 and having a scale of canvas, i can scale all my sprites using canvas transform, i dont have to manually multiply all my points by scale. Is that correct or not ?

Yes, that's correct!

### Then i am afraid i wasted a lot of time. Well nevermind. I think i should start yet another version of my classes that will try to do this.

It happens! Starting fresh might streamline your work. Good luck!

### Ok so the plan is, i will do this 4th version. Witch should be solid enouth to remove prevois ones.

Sounds like a solid plan! Focus on making this version robust.

### I am thinking also that starting a new repo and rewriting my code again, but with tests and more documentation, might help.

Starting a new repo with tests and documentation sounds like a great idea! It’ll lead to cleaner, more maintainable code.

### When i put my tests in src, nx compiles them no problem, wehen i put them on same level as source, errors, ?

The issue likely arises because when tests are placed outside the `src` folder, they might not be included in the build process or may cause conflicts with the project's configuration.

Make sure your `nx` configuration is set up to recognize tests outside `src`, or consider keeping them within `src` for simplicity. Alternatively, you can adjust your build or test configurations to correctly reference tests at the same level as the source code.

### I have set up the scene to render field, asset is added in webpack config, i forgot for moment.

No worries! It's easy to overlook details like that. Sounds like you're back on track now.

### I will still try to clean this project on right track withot rewriting from scratch.

That’s a smart approach! Cleaning up the project without starting from scratch can save time while still improving the structure and quality.

### Goal is simple 2d web games, with no frameworks beside environment ones.

That’s a great goal! Keeping it simple with just the essential tools will give you more control and a deeper understanding of your project.

### I decluttered SpriteRendererV4 class, still not perfect but ok for now.

The class looks much cleaner now! It’s well-structured, focusing on core functionality. You’ve done a great job organizing the logic and dependencies. With further refinement and testing, it should become even more robust. Keep up the good work!

### I think RendererV4 worked fine, sprite is drawn so that position is in center, and it scales with resizing canvas. Much tests and refactor need to be done still.

It looks like your `drawNormal` function is well-implemented for centering the sprite and scaling it with the canvas. Testing and refactoring will definitely help ensure robustness and maintainability. Great progress!

### I think i will name my scenes render1, render2, ... and last number will have full scene rendered.

That’s a straightforward and effective naming convention! It will help you easily track the progression of your scenes.

### Will this be sorted in order ?

If you're using a system that sorts files alphabetically, `render1`, `render2`, etc., will sort correctly up to `render9`. However, starting with `render10`, it might sort like this: `render1`, `render10`, `render2`, and so on.

To ensure proper sorting, consider using zero-padding, like `render01`, `render02`, etc. This way, even `render10` and beyond will sort in the correct order.

### So 99 will sort ok.

Yes, with zero-padding, `render01` to `render99` will sort correctly in order. Just ensure you pad all numbers consistently (e.g., `render01`, `render02`, ..., `render99`).

### I am ashamed, i got very lost with this project, i am just begining to get better

No need to be ashamed! Getting lost in a project is a common part of learning and growth. It’s great that you’re finding your way and improving. Keep at it, and your skills will continue to develop!

## 3

### I think i will create folder animatorV4, I hope this will be version that will gradually remove others.

Creating a dedicated `animatorV4` folder sounds like a smart move. It gives you a fresh start while keeping things organized, and you can phase out older versions as `V4` becomes stable. Great plan!

## I give up. From now on i am doing this just becouse my mind cant be still. No other goals.

It's okay to shift your mindset. Sometimes, focusing on the process rather than the outcome can lead to surprising insights and creativity. Keep going at your own pace, and let it be a source of enjoyment and growth.

## Should i do export default class ? or no default ?

It depends on your use case:

- **Use `export default class`** if the class is the primary export of the module. It makes importing simpler, as you can import the class without curly braces:

  ```javascript
  import MyClass from './MyClass'
  ```

- **Use `export class` (no default)** if the module may have multiple exports or if you prefer named imports. This approach provides more clarity and consistency in larger projects:
  ```javascript
  import { MyClass } from './MyClass'
  ```

Choose based on your project structure and preferences. If the class is the main focus of the module, `export default` is a common choice.

## I will now try to enable animations in my render_player scene

That sounds like a great next step! Enabling animations in your `render_player` scene will bring your project to life. Take your time, and don’t hesitate to test and iterate as you go. Good luck!

## I want to switch to other animation

To switch to a different animation in your scene, you’ll typically need to:

1. **Trigger the Animation Switch**: This could be based on an event (e.g., a key press or a game state change) or a condition in your game logic.

2. **Update the Animator**: In your code, you'd call a method like `switchAnimation(animId)` on your animator to change the current animation. This method should update the current animation frame sequence.

## 4

### For start we made unit test for SequentialAnimation algorithm.

Creating unit tests for your SequentialAnimation algorithm is a great idea. It will help ensure that your animations behave as expected.

## Now i need to connect with some audience. I need to publish web page.

Publishing a webpage is a great way to connect with an audience!
GitHub Pages: Ideal for simple, static sites. You can host directly from a GitHub repository.

## This command uses a simple Node.js-based server to serve your app localy.

```bash
npx serve dist/apps/[project-name]
```

or

```bash
npx http-server dist/apps/[project-name] -o
```

## To publish slideshow, on githubpages, base/root in index has to be changed from / to repo name.

```html
<title>Client</title> <base href="/football_slideshow/" />
```

It is good to try hit resources directly when debuging page hosting.

```html
https://atari-monk.github.io/football_slideshow/styles.1b3d768c319267ac.js
```

Also it is good to download artefact from githuba pages from branch to see what files are missing.

## 5

### Noticed that having audience improves art, since show must be given.

### Noticed my thouth atacking me very hard. Spoils the joy.

### Commits

1. Selecting initial animation from system feature prop in json.
2. Simulating key press half time in a silde.
3. Key pressing in slides.
4. Fix object scaling.
5. Todo: upgrade or fix arts.
6. Change footbal_slideshow publish on github pages to static content (simpler, faster).
7. Change footbal_slideshow title to Slideshow
8. Add py script to copy build.
9. Add scene with field colliders.

### AIMovement

Using new system template and method for pressing key.  
Can i similate player movement ?  
Player uses WSAD, position is in transform.  
Center of screen is 960, 540. Player starts from 760, 540.  
Can u write simulating movment in circular shape ?  
By just simulating key presses in some times.  
U can check position to correct stuff.  
Or maybe you have better idea for this kind of movement simulation.

## 11

Goal is to fix collision system.  
Witch is pain but... I need collisions.  
V2,V3 were 'insane'.  
V4 is original/normal rect algo used, plus point in center correction  
and plus correct position of transform.position.add(collider.center).
