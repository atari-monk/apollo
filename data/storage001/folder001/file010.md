# Styles

### Write me a css theme for my notes github page based on md.

To create a CSS theme for your notes on a GitHub Page using Markdown (`md`), you can style your page with custom CSS. Below is a sample CSS that provides a clean, readable, and minimalistic theme with a focus on notes, which works well with Markdown elements like headings, lists, code blocks, etc.

Save the following CSS code as `style.css` in your repository, and link it in your GitHub Pages HTML or Markdown files:

```css
/* General Styling */
body {
  font-family: 'Open Sans', sans-serif;
  background-color: #f5f7fa;
  color: #333;
  line-height: 1.8;
  padding: 20px;
  max-width: 800px;
  margin: auto;
}

a {
  color: #3498db;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

code {
  font-family: 'Source Code Pro', monospace;
  background-color: #f4f4f4;
  padding: 2px 4px;
  border-radius: 4px;
}

pre {
  background-color: #282c34;
  color: #abb2bf;
  padding: 10px;
  border-radius: 5px;
  overflow-x: auto;
}

blockquote {
  border-left: 5px solid #3498db;
  background-color: #f0f8ff;
  padding: 10px 20px;
  margin: 20px 0;
  color: #666;
}

hr {
  border: none;
  height: 1px;
  background-color: #eaeaea;
  margin: 40px 0;
}

/* Headings */
h1,
h2,
h3,
h4,
h5,
h6 {
  color: #2c3e50;
  margin-top: 1.5em;
}

h1 {
  font-size: 2.5em;
  border-bottom: 2px solid #eaeaea;
  padding-bottom: 0.3em;
}

h2 {
  font-size: 2em;
  border-bottom: 1px solid #eaeaea;
  padding-bottom: 0.2em;
}

h3 {
  font-size: 1.75em;
}

h4 {
  font-size: 1.5em;
}

/* Lists */
ul {
  list-style-type: disc;
  margin-left: 2em;
}

ol {
  list-style-type: decimal;
  margin-left: 2em;
}

/* Tables */
table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
}

table th,
table td {
  border: 1px solid #ddd;
  padding: 12px 15px;
  text-align: left;
}

table th {
  background-color: #3498db;
  color: #fff;
}

table tr:nth-child(even) {
  background-color: #f9f9f9;
}

table tr:hover {
  background-color: #f1f1f1;
}

/* Images */
img {
  max-width: 100%;
  height: auto;
  border-radius: 5px;
  margin: 10px 0;
}

/* Footer */
footer {
  text-align: center;
  padding: 20px;
  font-size: 0.8em;
  color: #999;
}
```

### Instructions to Apply the CSS:

1. Create a `style.css` file in your repository.
2. In your `README.md` or any Markdown file, add the following to the top or use the default GitHub Pages configuration:
   ```html
   <link rel="stylesheet" href="style.css" />
   ```

This theme includes styles for common Markdown elements like headings, paragraphs, code blocks, tables, lists, and blockquotes, providing a clean and functional look for your notes. Feel free to adjust the colors, font sizes, and spacing to your preference!

### That is nice but i would like to have dark mode and light mode, maybe also medium. Also i woul like it to work well on pc and mobile and laptop.

To create a theme that supports **dark mode**, **light mode**, and a **medium mode**, along with ensuring it works well on PC, laptop, and mobile, you can use **CSS custom properties** (variables) to define colors for each mode. You can then use media queries to switch between light and dark modes automatically based on the user's system preferences. Additionally, I'll include responsive design to ensure the theme looks great on various screen sizes.

Here’s how you can achieve this:

### CSS Theme with Light, Medium, and Dark Modes and Responsive Design

```css
/* Base Theme with CSS Variables */
:root {
  --background-color-light: #f5f7fa;
  --background-color-medium: #e0e5ec;
  --background-color-dark: #1e1e1e;

  --text-color-light: #333;
  --text-color-medium: #555;
  --text-color-dark: #f0f0f0;

  --link-color-light: #3498db;
  --link-color-dark: #62b6ff;

  --code-background-light: #f4f4f4;
  --code-background-dark: #2d2d2d;

  --pre-background-light: #f4f4f4;
  --pre-background-dark: #1e1e1e;

  --blockquote-background-light: #f0f8ff;
  --blockquote-background-dark: #282c34;

  --table-header-light: #3498db;
  --table-header-dark: #4a90e2;

  --table-row-odd-light: #f9f9f9;
  --table-row-odd-dark: #333;
  --table-row-even-light: #fff;
  --table-row-even-dark: #444;
}

/* Light Mode */
body.light-mode {
  background-color: var(--background-color-light);
  color: var(--text-color-light);
}

a.light-mode {
  color: var(--link-color-light);
}

code.light-mode {
  background-color: var(--code-background-light);
}

pre.light-mode {
  background-color: var(--pre-background-light);
  color: var(--text-color-light);
}

blockquote.light-mode {
  background-color: var(--blockquote-background-light);
  color: var(--text-color-medium);
}

table.light-mode th {
  background-color: var(--table-header-light);
  color: white;
}

table.light-mode tr:nth-child(odd) {
  background-color: var(--table-row-odd-light);
}

table.light-mode tr:nth-child(even) {
  background-color: var(--table-row-even-light);
}

/* Dark Mode */
body.dark-mode {
  background-color: var(--background-color-dark);
  color: var(--text-color-dark);
}

a.dark-mode {
  color: var(--link-color-dark);
}

code.dark-mode {
  background-color: var(--code-background-dark);
}

pre.dark-mode {
  background-color: var(--pre-background-dark);
  color: var(--text-color-dark);
}

blockquote.dark-mode {
  background-color: var(--blockquote-background-dark);
  color: var(--text-color-dark);
}

table.dark-mode th {
  background-color: var(--table-header-dark);
  color: white;
}

table.dark-mode tr:nth-child(odd) {
  background-color: var(--table-row-odd-dark);
}

table.dark-mode tr:nth-child(even) {
  background-color: var(--table-row-even-dark);
}

/* Medium Mode */
body.medium-mode {
  background-color: var(--background-color-medium);
  color: var(--text-color-medium);
}

a.medium-mode {
  color: var(--link-color-light);
}

code.medium-mode {
  background-color: var(--code-background-light);
}

pre.medium-mode {
  background-color: var(--pre-background-light);
  color: var(--text-color-medium);
}

blockquote.medium-mode {
  background-color: var(--blockquote-background-light);
  color: var(--text-color-medium);
}

table.medium-mode th {
  background-color: var(--table-header-light);
  color: white;
}

table.medium-mode tr:nth-child(odd) {
  background-color: var(--table-row-odd-light);
}

table.medium-mode tr:nth-child(even) {
  background-color: var(--table-row-even-light);
}

/* Responsive Design */
@media only screen and (max-width: 768px) {
  body {
    padding: 10px;
  }

  table {
    width: 100%;
    font-size: 0.9em;
  }

  pre {
    font-size: 0.9em;
  }
}

/* System Preference for Light/Dark Mode */
@media (prefers-color-scheme: dark) {
  body {
    background-color: var(--background-color-dark);
    color: var(--text-color-dark);
  }

  a {
    color: var(--link-color-dark);
  }
}

/* General Styling */
body {
  font-family: 'Open Sans', sans-serif;
  line-height: 1.8;
  padding: 20px;
  max-width: 800px;
  margin: auto;
}

a {
  text-decoration: none;
}

code {
  font-family: 'Source Code Pro', monospace;
  padding: 2px 4px;
  border-radius: 4px;
}

pre {
  padding: 10px;
  border-radius: 5px;
  overflow-x: auto;
}

blockquote {
  border-left: 5px solid var(--link-color-light);
  padding: 10px 20px;
  margin: 20px 0;
}

hr {
  border: none;
  height: 1px;
  background-color: #eaeaea;
  margin: 40px 0;
}

h1,
h2,
h3,
h4,
h5,
h6 {
  margin-top: 1.5em;
}

ul {
  list-style-type: disc;
  margin-left: 2em;
}

ol {
  list-style-type: decimal;
  margin-left: 2em;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
}

table th,
table td {
  border: 1px solid #ddd;
  padding: 12px 15px;
  text-align: left;
}

img {
  max-width: 100%;
  height: auto;
  border-radius: 5px;
  margin: 10px 0;
}

footer {
  text-align: center;
  padding: 20px;
  font-size: 0.8em;
  color: #999;
}
```

### Features:

1. **Theme Modes**: Supports **light**, **medium**, and **dark modes** using CSS classes like `light-mode`, `medium-mode`, and `dark-mode`. These classes can be toggled via JavaScript or CSS.
2. **System Preference Detection**: The theme will automatically switch to dark mode if the user's system is set to dark mode (`prefers-color-scheme: dark`). You can add a manual toggle using JavaScript to switch between modes.
3. **Responsive Design**: The theme adjusts itself for mobile and smaller screens using media queries to reduce padding, font sizes, and table dimensions.
4. **Readable on Multiple Devices**: It’s designed to be legible on PC, laptop, and mobile devices with readable font sizes and adjustable table sizes.

### How to Add Theme Switching with JavaScript:

You can add a button or a switch to toggle between modes dynamically:

```html
<script>
  function switchMode(mode) {
    document.body.className = mode
  }

  // Detect system preference and apply the mode
  const prefersDark =
    window.matchMedia &&
    window.matchMedia('(prefers-color-scheme: dark)').matches
  if (prefersDark) {
    switchMode('dark-mode')
  } else {
    switchMode('light-mode')
  }
</script>

<button onclick="switchMode('light-mode')">Light Mode</button>
<button onclick="switchMode('medium-mode')">Medium Mode</button>
<button onclick="switchMode('dark-mode')">Dark Mode</button>
```

With this setup, users can manually switch between the modes, and it adapts based on system preferences.
