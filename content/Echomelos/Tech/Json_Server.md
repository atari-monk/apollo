# Json Server

## How can i make some server, very simple that will provide json docs to my webpage

To set up a simple server that provides JSON documents to your webpage, you can follow these basic steps. Here's how you can do it using Node.js and Express, a lightweight and flexible framework for Node.js.

### Step 1: Install Node.js and Express

First, ensure that you have [Node.js](https://nodejs.org/en/download/) installed. You can check this by running:

```bash
node -v
npm -v
```

Then, set up a new project directory, initialize `npm`, and install Express:

```bash
mkdir simple-server
cd simple-server
npm init -y
npm install express
```

### Step 2: Create a Simple Server

In the `simple-server` directory, create a file called `server.js` and write the following code:

```js
const express = require('express')
const app = express()
const port = 3000

// Serve JSON data at a simple endpoint
app.get('/data', (req, res) => {
  const jsonData = {
    message: 'Hello, World!',
    date: new Date(),
    items: [1, 2, 3, 4],
  }
  res.json(jsonData)
})

// Start the server
app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`)
})
```

This simple Express server will listen on port 3000 and provide a JSON response when accessing the `/data` endpoint.

### Step 3: Serve the Webpage

You can also serve an HTML webpage that requests this JSON data. Add a `public` directory to store static files and create an `index.html` file inside it:

```bash
mkdir public
touch public/index.html
```

In `index.html`, add the following code:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Simple JSON Data Fetch</title>
    <script>
      async function fetchData() {
        const response = await fetch('/data')
        const data = await response.json()
        document.getElementById('json-data').textContent = JSON.stringify(
          data,
          null,
          2
        )
      }
    </script>
  </head>
  <body onload="fetchData()">
    <h1>Data from Server</h1>
    <pre id="json-data"></pre>
  </body>
</html>
```

This webpage fetches the JSON data from the server when loaded and displays it.

### Step 4: Modify the Server to Serve Static Files

In your `server.js`, add the line to serve static files:

```js
app.use(express.static('public'))
```

So your final `server.js` file should look like this:

```js
const express = require('express')
const app = express()
const port = 3000

// Serve static files (e.g., HTML)
app.use(express.static('public'))

// Serve JSON data at a simple endpoint
app.get('/data', (req, res) => {
  const jsonData = {
    message: 'Hello, World!',
    date: new Date(),
    items: [1, 2, 3, 4],
  }
  res.json(jsonData)
})

// Start the server
app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`)
})
```

### Step 5: Run the Server

To start the server, run:

```bash
node server.js
```

You can now visit `http://localhost:3000` in your browser to view the webpage and the JSON data from `/data`.

This provides a basic JSON API and a webpage that fetches and displays the data. You can expand on this by customizing the JSON content, handling more endpoints, or even integrating databases.
