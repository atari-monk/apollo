# Planning

## Please answear with no more text than 4x question text.

Sure! What’s your question?

## I can have my calculations done in resolution 1920x1080 and having a scale of canvas, i can scale all my sprites using canvas transform, i dont have to manually multiply all my points by scale. Is that correct or not ?

Yes, that's correct!

## Then i am afraid i wasted a lot of time. Well nevermind. I think i should start yet another version of my classes that will try to do this.

It happens! Starting fresh might streamline your work. Good luck!

## Ok so the plan is, i will do this 4th version. Witch should be solid enouth to remove prevois ones.

Sounds like a solid plan! Focus on making this version robust.

## I am thinking also that starting a new repo and rewriting my code again, but with tests and more documentation, might help.

Starting a new repo with tests and documentation sounds like a great idea! It’ll lead to cleaner, more maintainable code.

## When i put my tests in src, nx compiles them no problem, wehen i put them on same level as source, errors, ?

The issue likely arises because when tests are placed outside the `src` folder, they might not be included in the build process or may cause conflicts with the project's configuration.

Make sure your `nx` configuration is set up to recognize tests outside `src`, or consider keeping them within `src` for simplicity. Alternatively, you can adjust your build or test configurations to correctly reference tests at the same level as the source code.

## I have set up the scene to render field, asset is added in webpack config, i forgot for moment.

No worries! It's easy to overlook details like that. Sounds like you're back on track now.

## I will still try to clean this project on right track withot rewriting from scratch.

That’s a smart approach! Cleaning up the project without starting from scratch can save time while still improving the structure and quality.

## Goal is simple 2d web games, with no frameworks beside environment ones.

That’s a great goal! Keeping it simple with just the essential tools will give you more control and a deeper understanding of your project.

## I decluttered SpriteRendererV4 class, still not perfect but ok for now.

The class looks much cleaner now! It’s well-structured, focusing on core functionality. You’ve done a great job organizing the logic and dependencies. With further refinement and testing, it should become even more robust. Keep up the good work!

## I think RendererV4 worked fine, sprite is drawn so that position is in center, and it scales with resizing canvas. Much tests and refactor need to be done still.

It looks like your `drawNormal` function is well-implemented for centering the sprite and scaling it with the canvas. Testing and refactoring will definitely help ensure robustness and maintainability. Great progress!
