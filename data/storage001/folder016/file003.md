# 2024-09-04

## For start we made unit test for SequentialAnimation algorithm.

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
