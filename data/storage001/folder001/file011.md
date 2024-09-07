# I have a github page based on md, now if i use static contet action it wont generate html page flrom md like in jekyl witch is default for github page from branch right ?

You're correct. If you're using a **GitHub Pages** setup that serves static content (e.g., with a custom action), it won't automatically generate HTML from Markdown files the way Jekyll (the default engine for GitHub Pages) does when you're using the `gh-pages` branch or another branch.

Here's a breakdown:

- **Jekyll (Default for GitHub Pages)**: GitHub Pages automatically uses Jekyll to convert `.md` files into `.html` if you're using Jekyll as the static site generator. It will build your Markdown files into a fully rendered static site.
- **Static Content with Custom Actions**: If you're using a custom GitHub Actions workflow to serve static content, you'll need to explicitly set up the conversion from Markdown to HTML. This would involve adding a static site generator like Jekyll, Hugo, or another tool (or a custom script) in the GitHub Actions workflow to process the Markdown.

If you want to stick with Markdown but not use Jekyll, you can set up your GitHub Actions to use a static site generator of your choice, or convert the Markdown manually. If you're moving away from Jekyll, you lose its automatic handling and need to manage the content generation yourself.
