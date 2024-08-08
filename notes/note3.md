# Apollo Notes

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

If you don't have a `_config.yml` file in your GitHub Pages repository, it means that your site is either using GitHub Pages with the default settings or you're relying on the default Jekyll configuration provided by GitHub. In this case, if you're seeing an "Edit this page" link on your site, it may be due to one of the following reasons:

### Possible Reasons for "Edit this page" Link

1. **Theme Defaults**:

    - Some Jekyll themes automatically include an "Edit this page" link without needing `_config.yml`. Even without a `_config.yml` file, your theme might be set to include these links by default.

2. **GitHub Pages Defaults**:
    - If you're using a Jekyll theme provided by GitHub Pages (like `minima` or `jekyll-theme-midnight`), these themes might have built-in functionality to show an "Edit this page" link on every Markdown-rendered page.

### What Can You Do?

Since you don't have a `_config.yml` file, you can create one to customize the behavior of your site, including potentially disabling the "Edit this page" link.

#### 1. **Create a `_config.yml` File**

-   You can create a `_config.yml` file in the root of your repository to override the default settings.
-   Here’s how to create a basic `_config.yml` file that disables the "Edit this page" link:

```yaml
# _config.yml

# Site settings
title: Apollo Notes
description: Notes repository

# Disable the 'Edit this page' link
github_edit_link: false
```

Note that the above `github_edit_link` setting might vary depending on the theme you're using. If the theme you're using supports this option, it will disable the "Edit this page" link.

#### 2. **Switch to a Different Layout or Theme**

-   If your current setup doesn't allow easy removal of the "Edit this page" link, consider switching to a different Jekyll theme that doesn't include this link by default.

#### 3. **Manually Edit Theme Files (if applicable)**

-   If you're comfortable with editing the theme directly and if the theme files are in your repository, you can look into the `_layouts` folder or specific files where the "Edit this page" link might be included.
-   Typically, this might be found in a file like `post.html`, `page.html`, or `default.html` within the `_layouts` directory.

### How to Proceed

1. **Check Theme Documentation**:

    - First, try to determine which theme you're using by looking for a `.theme` file or by reviewing the `Gemfile` (if it exists).
    - Search the theme's documentation online to find out how to disable or customize the "Edit this page" link.

2. **Experiment with `_config.yml`**:

    - Even a minimal `_config.yml` can be helpful. Start by adding one to your repository and include basic settings to control the theme and links.

3. **Review Theme Files**:
    - If you have access to the theme files (e.g., if they are stored locally in your repository), you can manually edit the layout files to remove the "Edit this page" link.

### Summary

Without a `_config.yml`, you're relying on default settings provided by GitHub Pages or your theme. To take control over features like the "Edit this page" link, creating a `_config.yml` file is the best approach. This will allow you to customize your site further, including disabling any unwanted links. If you can't disable the link through `_config.yml`, manually editing the theme files or switching to a simpler theme may be necessary.

---

[Back to Index](../index.md)
