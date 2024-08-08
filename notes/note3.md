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

Yes, you can enable a dark mode for your GitHub Pages site by adding custom CSS or using a Jekyll theme that supports dark mode. Here are a few ways you can implement dark mode:

### 1. **Using a Jekyll Theme with Dark Mode Support**

Some Jekyll themes come with built-in support for dark mode. You can enable dark mode by configuring the theme or using a toggle switch.

#### Example with Minimal Mistakes Theme:

The `minimal-mistakes` theme is a popular Jekyll theme with dark mode support.

**Steps:**

1. **Add `_config.yml`**: If you don’t have one, create a `_config.yml` file in the root of your repository.

2. **Set Up the Theme**:

    ```yaml
    remote_theme: mmistakes/minimal-mistakes
    plugins:
        - jekyll-remote-theme

    # Theme settings
    theme: minimal-mistakes
    minimal_mistakes_skin: dark
    ```

3. **Customizing**:
    - If you want to allow users to toggle between light and dark mode, you can add more customization. This might involve adding a JavaScript-based toggle switch.

### 2. **Custom CSS for Dark Mode**

You can add custom CSS to your site to implement dark mode, either as the default or with a toggle option.

#### Example:

1. **Create a CSS file (e.g., `assets/css/style.css`)**:

    ```css
    /* Dark Mode Styles */
    body {
        background-color: #121212;
        color: #ffffff;
    }
    a {
        color: #bb86fc;
    }
    /* Add more styles as needed */
    ```

2. **Link the CSS file in your HTML or Markdown files**:

    - In your `index.md` or `default.html`, add a link to the CSS file:

    ```html
    <link rel="stylesheet" href="/assets/css/style.css" />
    ```

3. **Optional: Implement Dark Mode Toggle with JavaScript**:

    - You can add a toggle switch using JavaScript to allow users to switch between light and dark mode.

    ```javascript
    // Dark mode toggle
    const toggleSwitch = document.querySelector(
        '.theme-switch input[type="checkbox"]'
    );
    const currentTheme = localStorage.getItem("theme");

    if (currentTheme) {
        document.documentElement.setAttribute("data-theme", currentTheme);

        if (currentTheme === "dark") {
            toggleSwitch.checked = true;
        }
    }

    toggleSwitch.addEventListener("change", function (e) {
        if (e.target.checked) {
            document.documentElement.setAttribute("data-theme", "dark");
            localStorage.setItem("theme", "dark");
        } else {
            document.documentElement.setAttribute("data-theme", "light");
            localStorage.setItem("theme", "light");
        }
    });
    ```

4. **HTML to Include the Toggle**:
    ```html
    <div class="theme-switch-wrapper">
        <label class="theme-switch" for="checkbox">
            <input type="checkbox" id="checkbox" />
            <div class="slider round"></div>
        </label>
        <em>Enable Dark Mode!</em>
    </div>
    ```

### 3. **Using CSS `prefers-color-scheme` Media Query**

Modern browsers support the `prefers-color-scheme` media query, which allows you to automatically adjust your site’s theme based on the user's system preference.

#### Example:

1. **Add CSS with `prefers-color-scheme`**:

    ```css
    @media (prefers-color-scheme: dark) {
        body {
            background-color: #121212;
            color: #ffffff;
        }
        a {
            color: #bb86fc;
        }
        /* Add more dark mode styles here */
    }

    @media (prefers-color-scheme: light) {
        body {
            background-color: #ffffff;
            color: #000000;
        }
        a {
            color: #1a0dab;
        }
        /* Add more light mode styles here */
    }
    ```

### Summary

-   **Jekyll Themes**: Use a theme with built-in dark mode support.
-   **Custom CSS**: Implement dark mode by creating custom CSS.
-   **User Toggle**: Allow users to switch between light and dark modes using JavaScript.
-   **Automatic Dark Mode**: Utilize the `prefers-color-scheme` media query for automatic dark mode based on user preferences.

By using these methods, you can have a dark mode for your GitHub Pages site, either as the default or as an option for your visitors.

---

[Back to Index](../index.md)
