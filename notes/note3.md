# Apollo Notes

[Back to Index](../index.md)

Creating a structured approach for your notes with a single Markdown file per note and an index page is a good strategy for organization and navigation. Here’s how you can structure your GitHub Pages repository to achieve this:

### Suggested Structure

```
.
├── index.md
├── _config.yml
├── notes/
│   ├── note1.md
│   ├── note2.md
│   ├── note3.md
│   └── ...
└── assets/ (optional for images, CSS, etc.)
```

### Explanation:

1. **`index.md`**:

    - This will be your homepage or the index of your notes.
    - It will contain links to all individual note files stored in the `notes/` directory.

2. **`_config.yml`** (optional):

    - This file is used by Jekyll to configure your GitHub Pages site. You can specify settings like the title of your site, theme, and any plugins you want to use.

3. **`notes/`**:

    - This directory contains individual Markdown files for each of your notes.
    - Each file (e.g., `note1.md`, `note2.md`) is a separate note.

4. **`assets/`** (optional):
    - This directory can hold images, CSS files, or other assets you might want to include in your notes.

### Example Files

#### `index.md` (Your Index Page)

```markdown
# Welcome to Apollo Notes

This is the index of all my notes.

## Notes

-   [Note 1](notes/note1.md)
-   [Note 2](notes/note2.md)
-   [Note 3](notes/note3.md)
```

#### `notes/note1.md` (An Example Note)

```markdown
# Note 1

This is the content of Note 1.

## Subheading

Some more detailed content.
```

#### `notes/note2.md` (Another Note)

```markdown
# Note 2

This is the content of Note 2.

## Subheading

Further details about this topic.
```

### Steps to Set Up

1. **Create the Repository**:

    - Set up a new repository on GitHub. Name it `username.github.io` if it’s your personal site.

2. **Add Markdown Files**:

    - Create `index.md` in the root of the repository.
    - Create a `notes/` directory and add your individual note files there (e.g., `note1.md`, `note2.md`).

3. **Configure GitHub Pages**:

    - Go to the repository settings, scroll to the GitHub Pages section, and select the branch (usually `main`) where your files are located.

4. **Push the Changes**:

    - Commit and push your changes to GitHub.

5. **Access Your Site**:
    - Your site should now be accessible at `https://username.github.io/`, with the index page listing links to your notes.

### Navigation Tips

-   **Back to Index**: Include a link back to the `index.md` at the top or bottom of each note for easy navigation.

    ```markdown
    [Back to Index](../index.md)
    ```

-   **Cross-Referencing**: You can cross-reference notes by linking to other Markdown files within the `notes/` directory.

    ```markdown
    See [Note 2](note2.md) for more details on this topic.
    ```

### Advantages of This Structure:

-   **Scalability**: Easy to add new notes by simply adding a new file in the `notes/` directory.
-   **Organization**: Clear separation between the index and the notes, making it easier to manage and navigate.
-   **Modularity**: Each note is independent, allowing for focused content per file.

This structure will make your GitHub Pages site clean, easy to navigate, and maintainable as your collection of notes grows.

---

### Additions

#### 1. **Create a `_config.yml` File**

-   You can create a `_config.yml` file in the root of your repository to override the default settings.
-   Here’s how to create a basic `_config.yml`:

```yaml
# _config.yml

# Site settings
title: Apollo Notes
description: Notes repository
```

#### 2. **Selecting a Theme**

[Adding a Theme](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/adding-a-theme-to-your-github-pages-site-using-jekyll#adding-a-theme)

[Supported themes](https://pages.github.com/themes/)

-   This one worked

```yaml
plugins:
    - jekyll-remote-theme

remote_theme: pages-themes/midnight@v0.2.0

title: Apollo Notes
description: Notes repository
```

---

[Back to Index](../index.md)
