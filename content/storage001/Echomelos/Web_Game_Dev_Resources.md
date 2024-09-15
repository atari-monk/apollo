# Web Game Dev Resources

### **1. Structuring Your Game with Vanilla JavaScript**

**a. Game Loop**

- Implement a game loop using `requestAnimationFrame` to handle rendering and updates.

  ```javascript
  function gameLoop() {
    update()
    render()
    requestAnimationFrame(gameLoop)
  }

  function update() {
    // Update game state
  }

  function render() {
    // Render game elements
  }

  requestAnimationFrame(gameLoop)
  ```

### **2. Rendering Options**

**a. DOM Manipulation**

- For simple games, you can use HTML elements and CSS for rendering.
  ```html
  <div
    id="player"
    style="position: absolute; width: 50px; height: 50px; background-color: red;"
  ></div>
  ```

**b. Canvas API**

- For more complex graphics, use the Canvas API.

  ```html
  <canvas id="gameCanvas" width="800" height="600"></canvas>
  ```

  ```javascript
  const canvas = document.getElementById('gameCanvas')
  const ctx = canvas.getContext('2d')

  function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height)
    // Draw game elements
    ctx.fillStyle = 'red'
    ctx.fillRect(player.x, player.y, 50, 50)
  }
  ```

### **3. Handling User Input**

- Use native event listeners to handle keyboard and mouse input.
  ```javascript
  window.addEventListener('keydown', (e) => {
    switch (e.key) {
      case 'ArrowUp':
        player.moveUp()
        break
      case 'ArrowDown':
        player.moveDown()
        break
      // Handle other keys
    }
  })
  ```

### **4. State Management**

- Manage game state with plain JavaScript objects or simple state management patterns.

  ```javascript
  const gameState = {
    player: { x: 100, y: 100, score: 0 },
    enemies: [],
    // Other state properties
  }

  function update() {
    // Update gameState based on game logic
  }
  ```

### **5. Enhancing Development with Libraries**

While Vanilla JS provides full control, certain libraries can simplify specific tasks without the overhead of a framework like React:

**a. Game Development Libraries**

- **Phaser.js**: A popular framework for creating HTML5 games. It provides a robust set of features while allowing you to work primarily with Vanilla JS.

  - [Phaser Documentation](https://phaser.io/documentation)

- **PixiJS**: A fast 2D rendering library that works well with the Canvas and WebGL.
  - [PixiJS Documentation](https://pixijs.com/)

**b. Utility Libraries**

- **lodash**: A utility library that can simplify common programming tasks.

  - [lodash Documentation](https://lodash.com/docs/)

- **Hammer.js**: For handling touch gestures if your game needs touch support.
  - [Hammer.js Documentation](https://hammerjs.github.io/)

### **6. Tools and Build Processes**

For small projects, you might not need a complex build process, but some tools can enhance your workflow:

**a. Bundlers**

- **Parcel** or **Vite**: Simple bundlers that require minimal configuration.
  - [Parcel](https://parceljs.org/)
  - [Vite](https://vitejs.dev/)

**b. Linters and Formatters**

- **ESLint**: To maintain code quality.

  - [ESLint Documentation](https://eslint.org/)

- **Prettier**: For consistent code formatting.
  - [Prettier Documentation](https://prettier.io/)

### **7. Learning Resources**

- **MDN Web Docs**: Comprehensive resources on JavaScript, Canvas API, and web development.

  - [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
  - [MDN Canvas API](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API)

- **Eloquent JavaScript**: A free book that covers JavaScript fundamentals and beyond.

  - [Eloquent JavaScript](https://eloquentjavascript.net/)

- **Game Development Tutorials**
  - **Phaser Tutorials**: [Phaser Tutorials](https://phaser.io/learn)
  - **MDN Game Development**: [MDN Game Development](https://developer.mozilla.org/en-US/docs/Games)

### **8. When to Consider Frameworks Later**

Starting with Vanilla JS gives you a solid foundation and full control. As your game grows, you might find the need for more structure or advanced features, at which point you can integrate frameworks or libraries incrementally. This approach ensures you only add complexity when it's genuinely needed.
