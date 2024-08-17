# Requirements

- This is my md page layout for github pages.

```html
<!doctype html>
<html lang="{{ site.lang | default: "en-US" }}">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    {% seo %}

    <!-- Load theme CSS first -->
    <link rel="stylesheet" href="{{ '/assets/css/style.css?v=' | append: site.github.build_revision | relative_url }}">

    <!-- Load additional CSS -->
    <link rel="stylesheet" href="{{ '/assets/css/custom.css' | relative_url }}">

    <!-- Load JavaScript libraries -->
    <script src="https://code.jquery.com/jquery-1.12.4.min.js" integrity="sha256-ZosEbRLbNQzLpnKIkEdrPv7lOy9C27hHQ+Xp8a4MxAQ=" crossorigin="anonymous"></script>
    <script src="{{ '/assets/js/respond.js' | relative_url }}"></script>
    <!-- HTML5 shim and Respond.js for IE8 support -->
    <!--[if lt IE 9]>
      <script src="//html5shiv.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
    <!--[if lt IE 8]>
      <link rel="stylesheet" href="{{ '/assets/css/ie.css' | relative_url }}">
    <![endif]-->

    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
    {% include head-custom.html %}
  </head>
  <body>
      <div id="header">
        <nav>
          <ul>
            <li class="fork"><a href="{{ site.github.repository_url }}">View On GitHub</a></li>
            {% if site.show_downloads %}
              <li class="downloads"><a href="{{ site.github.zip_url }}">ZIP</a></li>
              <li class="downloads"><a href="{{ site.github.tar_url }}">TAR</a></li>
              <li class="title">DOWNLOADS</li>
            {% endif %}
          </ul>
        </nav>
      </div><!-- end header -->

    <div class="wrapper">
      <section>
        <div id="title">
          <h1>{{ site.title | default: site.github.repository_name }}</h1>
          <p>{{ site.description | default: site.github.project_tagline }}</p>
          <hr>
          <span class="credits left">Project maintained by <a href="{{ site.github.owner_url }}">{{ site.github.owner_name }}</a></span>
          <span class="credits right">Hosted on GitHub Pages &mdash; Theme by <a href="https://twitter.com/mattgraham">mattgraham</a></span>
        </div>

        {{ content }}

      </section>
    </div>
    <script src="{{ '/assets/js/copy-code.js' | relative_url }}"></script>
  </body>
</html>

```

- In assets i have also copy-code.js and custom.css.

1. Add section available whole time on page where i can put links.

- [Home](../../../index.md), this link when i am on index.md page in folder00n
- [Index](index.md)
  [Main](../../../index.md), these links when i am on file00n page in folder00n

2. Use js, css and layout.
3. Put each feature in its function.
4. Yes but you see file and folder names are numberd 001, 099 for folders and more for files.
5. This is my link `https://atari-monk.github.io/apollo/` to Home page that i want to have on each page like 'https://atari-monk.github.io/apollo/data/storage001/folder001/' where numbers are variable.
6. When on page ``we should also provide link to`https://atari-monk.github.io/apollo/data/storage001/folder001/` index page like this, but numbers can vary depending on witch path it is.
7. Use absolute links for github not relative .md ones.