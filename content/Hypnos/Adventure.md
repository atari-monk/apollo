# Hypnos - Typescript API Adventure

Teach me fast way of creating api in typescript.  
10 day adventure. Promot is a day.  
I mean one answer of yours is a day. Next

## Day 1

Sounds like a fun challenge! Let's begin your 10-day API adventure with TypeScript.

---

**Day 1: Setting Up the Project**

To start off, you need to set up your development environment. Here's a quick guide:

1. **Install Node.js** (skip this if already installed)
   - [Download Node.js](https://nodejs.org) and install the latest LTS version.
2. **Initialize a TypeScript Project**
   Open your terminal and create a new project folder, then initialize it:

   ```bash
   mkdir hypnos
   cd hypnos
   npm init -y
   ```

3. **Install TypeScript and Express**
   Install TypeScript and Express.js (a web framework) with these commands:

   ```bash
   npm install typescript --save-dev
   npm install express
   npm i --save-dev @types/express
   ```

4. **Set Up TypeScript Configuration**
   Initialize a TypeScript config file:

   ```bash
   npx tsc --init
   ```

   In your `tsconfig.json`, modify `"outDir"` to point to a `dist` folder where the compiled code will go:

   ```json
   "outDir": "./dist",
   ```

5. **Create Source Folders**
   Set up your project structure like this:

   ```
   /hypnos
     /src
       app.ts
   ```

   In `app.ts`, write a basic Express setup to start your server:

   ```typescript
   import express from 'express'

   const app = express()
   const port = 3000

   app.get('/', (req, res) => {
     res.send('Hello, TypeScript API!')
   })

   app.listen(port, () => {
     console.log(`Server running on http://localhost:${port}`)
   })
   ```

6. **Run Your API**
   Update `package.json` scripts to compile and run the API:

   ```json
   "scripts": {
     "start": "node dist/app.js",
     "build": "tsc"
   }
   ```

   Compile the TypeScript code:

   ```bash
   npm run build
   ```

   Then start the server:

   ```bash
   npm start
   ```
   
   Create and publish repository to github.
   
   Add .gitignore
   
   ```plaintext
   node_modules
   ```
   
   Add .prettierrc
   
   ```plaintext
   {
     "singleQuote": true,
     "indent": 2,
     "semi": false
   }
   ```

That’s the end of **Day 1**! You've got your TypeScript API project initialized with Express.

---

Ready for Day 2?

## Day 2

**Day 2: Creating Your First API Endpoint**

Today, we’ll expand our API by adding more endpoints and learning how to handle JSON data.

### Step 1: Update `app.ts` for JSON Parsing

First, let's allow our Express app to handle JSON requests. Update your `app.ts` file:

```typescript
import express from 'express';

const app = express();
const port = 3000;

// Middleware to parse JSON requests
app.use(express.json());

app.get('/', (req, res) => {
  res.send('Hello, TypeScript API!');
});

// New endpoint to create a user
app.post('/users', (req, res) => {
  const newUser = req.body; // Get user data from request body
  console.log('New user:', newUser);
  res.status(201).json({ message: 'User created', user: newUser });
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
```

### Step 2: Test Your Endpoint

To test the new endpoint, you can use a tool like Postman or CURL.

1. **Using Postman:**
   - Open Postman and create a new POST request to `http://localhost:3000/users`.
   - In the Body tab, select "raw" and choose JSON as the format.
   - Enter the following JSON:

   ```json
   {
     "name": "John Doe",
     "email": "john.doe@example.com"
   }
   ```

   - Click "Send". You should see a response confirming the user creation.

2. **Using CURL:**
   Open your terminal and run:

   ```bash
   curl -X POST http://localhost:3000/users -H "Content-Type: application/json" -d '{"name":"John Doe","email":"john.doe@example.com"}'
   ```

   You should receive a similar response.

### Step 3: Understanding the Code

- **`app.use(express.json())`:** This middleware function parses incoming requests with JSON payloads, making the data accessible via `req.body`.
- **`app.post('/users', ...)`:** This defines a new POST endpoint. When a request is sent to `/users`, it logs the new user data and responds with a confirmation message.

### Step 4: Clean Up

To improve your project structure, consider separating the API routes into their own file. For now, you can keep this structure simple, but we'll address this in a later day.

That’s it for **Day 2**! You’ve successfully added your first POST endpoint to the API.

---

Ready for Day 3?

## Day 3

**Day 3: Structuring Your Project with Routes**

Today, we’ll refactor our API to separate routes into their own module, making it more organized and scalable. This will set the groundwork for adding more functionality later.

### Step 1: Create a Routes Folder

First, let's create a folder for your routes:

1. Create a new folder called `routes` inside the `src` directory:

   ```
   /my-api
     /src
       /routes
         userRoutes.ts
       app.ts
   ```

### Step 2: Set Up User Routes

Next, move your user-related logic into `userRoutes.ts`. Create the file and add the following code:

```typescript
// src/routes/userRoutes.ts
import { Router } from 'express';

const router = Router();

// GET request for testing
router.get('/', (req, res) => {
  res.send('User route');
});

// POST endpoint to create a user
router.post('/', (req, res) => {
  const newUser = req.body; // Get user data from request body
  console.log('New user:', newUser);
  res.status(201).json({ message: 'User created', user: newUser });
});

export default router;
```

### Step 3: Modify `app.ts` to Use User Routes

Now, update your `app.ts` to use this new route module:

```typescript
import express from 'express';
import userRoutes from './routes/userRoutes';

const app = express();
const port = 3000;

// Middleware to parse JSON requests
app.use(express.json());

// Use the user routes
app.use('/users', userRoutes);

app.get('/', (req, res) => {
  res.send('Hello, TypeScript API!');
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
```

### Step 4: Test Your Updated API

1. Restart your server if it's still running.
2. Use Postman or CURL to test the new user route:

   - **Using Postman:**
     - Send a POST request to `http://localhost:3000/users` with the same JSON body as before.
   
   - **Using CURL:**
     ```bash
     curl -X POST http://localhost:3000/users -H "Content-Type: application/json" -d '{"name":"Jane Doe","email":"jane.doe@example.com"}'
     ```

   You should receive a response confirming user creation.

### Step 5: Understanding the Changes

- **`import { Router } from 'express';`:** This imports the Router class from Express, which is used to create route handlers.
- **`router.get('/', ...)` and `router.post('/', ...)`:** Define the GET and POST routes for users. The `/` here refers to the `/users` endpoint in the main app.
- **`app.use('/users', userRoutes);`:** This mounts the user routes at the `/users` path, allowing you to organize routes logically.

### Summary

You’ve successfully structured your API by moving user-related routes into their own module, which enhances code maintainability and readability.

That’s the end of **Day 3**! You’re well on your way to creating a robust API.

---

Ready for Day 4?

## Day 4

**Day 4: Adding TypeScript Interfaces for Type Safety**

Today, we’ll introduce TypeScript interfaces to enforce type safety in your API. This will help ensure that the data structure is consistent across your application, making it easier to manage and debug.

### Step 1: Create an Interfaces Folder

Create a folder for your interfaces in the `src` directory:

```
/my-api
  /src
    /interfaces
      user.ts
    /routes
      userRoutes.ts
    app.ts
```

### Step 2: Define the User Interface

Inside the `interfaces` folder, create a file named `user.ts` and define the `User` interface:

```typescript
// src/interfaces/user.ts
export interface User {
  name: string;
  email: string;
}
```

### Step 3: Update the User Routes to Use the Interface

Modify your `userRoutes.ts` file to use the `User` interface for type-checking:

```typescript
// src/routes/userRoutes.ts
import { Router, Request, Response } from 'express';
import { User } from '../interfaces/user';

const router = Router();

// GET request for testing
router.get('/', (req: Request, res: Response) => {
  res.send('User route');
});

// POST endpoint to create a user
router.post('/', (req: Request, res: Response) => {
  const newUser: User = req.body; // Enforce User interface
  console.log('New user:', newUser);
  res.status(201).json({ message: 'User created', user: newUser });
});

export default router;
```

### Step 4: Update Type Definitions in Your API

Using the `User` interface helps ensure that any data passed to your API matches the defined structure. If a user sends data that doesn't conform to the `User` interface, TypeScript will throw an error during development, helping catch issues early.

### Step 5: Testing Your Updated API

1. Restart your server.
2. Test the POST endpoint again with a valid user object in Postman or CURL:

   ```json
   {
     "name": "Alice Smith",
     "email": "alice.smith@example.com"
   }
   ```

   You should still receive a confirmation response.

3. If you send an invalid object, like missing the `name` field, TypeScript won't catch this at runtime, but it's a good practice to validate user inputs. You can implement validation later.

### Summary

You’ve successfully integrated TypeScript interfaces into your API, improving type safety and code reliability. This will help you manage data more effectively as your API grows.

That wraps up **Day 4**! You’re doing great!

---

Ready for Day 5?

## Day 5

**Day 5: Implementing Input Validation with Middleware**

Today, we’ll add input validation to ensure that users provide the correct data structure when creating a user. This will enhance the reliability of your API and prevent potential errors.

### Step 1: Install `express-validator`

We’ll use the `express-validator` library for input validation. Install it with the following command:

```bash
npm install express-validator
```

### Step 2: Create a Validation Middleware

Create a new folder called `middleware` inside the `src` directory:

```
/my-api
  /src
    /interfaces
      user.ts
    /middleware
      validateUser.ts
    /routes
      userRoutes.ts
    app.ts
```

Inside the `middleware` folder, create a file named `validateUser.ts` and add the following code to handle validation:

```typescript
// src/middleware/validateUser.ts
import { body, validationResult } from 'express-validator';
import { Request, Response, NextFunction } from 'express';

export const validateUser = [
  body('name').isString().notEmpty().withMessage('Name is required and must be a string.'),
  body('email').isEmail().withMessage('Email is required and must be a valid email address.'),
  
  (req: Request, res: Response, next: NextFunction) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }
    next();
  },
];
```

This is fix as original had some issues. 

```typescript
import { body, validationResult } from 'express-validator'
import { Request, Response, NextFunction, RequestHandler } from 'express'

export const validateUser = [
  body('name')
    .isString()
    .notEmpty()
    .withMessage('Name is required and must be a string.'),
  body('email')
    .isEmail()
    .withMessage('Email is required and must be a valid email address.'),
]

export const checkValidationResult: RequestHandler = (
  req: Request,
  res: Response,
  next: NextFunction
): void => {
  const errors = validationResult(req)
  if (!errors.isEmpty()) {
    res.status(400).json({ errors: errors.array() })
    return
  }
  next()
}

```

### Step 3: Update User Routes to Use Validation Middleware

Modify your `userRoutes.ts` to include the validation middleware before the POST endpoint:

```typescript
// src/routes/userRoutes.ts
import { Router, Request, Response } from 'express';
import { User } from '../interfaces/user';
import { validateUser } from '../middleware/validateUser';

const router = Router();

// GET request for testing
router.get('/', (req: Request, res: Response) => {
  res.send('User route');
});

// POST endpoint to create a user
router.post('/', validateUser, (req: Request, res: Response) => {
  const newUser: User = req.body; // Enforce User interface
  console.log('New user:', newUser);
  res.status(201).json({ message: 'User created', user: newUser });
});

export default router;
```

This is fix as original had some issues. 

```typescript
router.post(
  '/',
  validateUser,
  checkValidationResult,
  ...
)
```

### Step 4: Test Input Validation

1. Restart your server.
2. Test the POST endpoint with various inputs:

   - **Valid Request:**
     ```json
     {
       "name": "Alice Smith",
       "email": "alice.smith@example.com"
     }
     ```
     You should get a successful creation response.

   - **Invalid Request:**
     - Missing name:
       ```json
       {
         "email": "alice.smith@example.com"
       }
       ```
     - Invalid email:
       ```json
       {
         "name": "Alice Smith",
         "email": "not-an-email"
       }
       ```

   In both cases, you should receive a `400 Bad Request` response with an error message detailing what went wrong.

### Summary

You’ve implemented input validation using middleware, ensuring that only valid data can be processed by your API. This is crucial for maintaining data integrity and improving user experience.

That concludes **Day 5**! You’re making excellent progress!

---

Ready for Day 6?

## Day 6

**Day 6: Connecting to a Database with TypeORM**

Today, we’ll integrate a database into our API using TypeORM, an Object-Relational Mapping (ORM) tool for TypeScript and JavaScript. We’ll set up a database connection and create a user entity to manage user data.

### Step 1: Install TypeORM and Database Driver

You’ll need to install TypeORM along with a database driver. For this example, we'll use SQLite for simplicity, but you can choose other databases like PostgreSQL or MySQL if preferred.

Run the following command to install TypeORM and the SQLite driver:

```bash
npm install typeorm sqlite3
```

### Step 2: Create a TypeORM Configuration

Create a new file named `ormconfig.json` in the root of your project to configure TypeORM:

```json
{
  "type": "sqlite",
  "database": "database.sqlite",
  "synchronize": true,
  "logging": false,
  "entities": ["src/entities/**/*.ts"]
}
```

- `synchronize`: This option automatically creates the database schema on every application launch (good for development but not recommended for production).
- `entities`: This points to the location of your entity classes.

### Step 3: Create a User Entity

Now, create a new folder called `entities` inside the `src` directory:

```
/my-api
  /src
    /entities
      User.ts
    /interfaces
      user.ts
    /middleware
      validateUser.ts
    /routes
      userRoutes.ts
    app.ts
```

Inside the `entities` folder, create a file named `User.ts` and define the user entity:

```typescript
// src/entities/User.ts
import { Entity, PrimaryGeneratedColumn, Column } from 'typeorm';

@Entity()
export class User {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  name: string;

  @Column()
  email: string;
}
```

### Step 4: Set Up Database Connection in `app.ts`

Update your `app.ts` file to establish a database connection when the application starts:

```typescript
import express from 'express';
import { createConnection } from 'typeorm';
import userRoutes from './routes/userRoutes';

const app = express();
const port = 3000;

// Middleware to parse JSON requests
app.use(express.json());

// Use the user routes
app.use('/users', userRoutes);

// Establish database connection
createConnection()
  .then(() => {
    console.log('Database connected successfully!');
    app.listen(port, () => {
      console.log(`Server running on http://localhost:${port}`);
    });
  })
  .catch((error) => {
    console.error('Database connection failed:', error);
  });
```

### Step 5: Update the User Route to Save Users

Modify your `userRoutes.ts` to save the user data to the database:

```typescript
// src/routes/userRoutes.ts
import { Router, Request, Response } from 'express';
import { User } from '../interfaces/user';
import { validateUser } from '../middleware/validateUser';
import { getRepository } from 'typeorm';
import { User as UserEntity } from '../entities/User';

const router = Router();

// GET request for testing
router.get('/', async (req: Request, res: Response) => {
  const users = await getRepository(UserEntity).find();
  res.json(users);
});

// POST endpoint to create a user
router.post('/', validateUser, async (req: Request, res: Response) => {
  const newUser: User = req.body; // Enforce User interface

  // Create a new user instance
  const userEntity = getRepository(UserEntity).create(newUser);

  // Save the user to the database
  const savedUser = await getRepository(UserEntity).save(userEntity);

  res.status(201).json({ message: 'User created', user: savedUser });
});

export default router;
```

### Step 6: Test the Database Integration

1. Restart your server.
2. Use Postman or CURL to test the `/users` endpoint with a valid POST request:

   ```json
   {
     "name": "Bob Johnson",
     "email": "bob.johnson@example.com"
   }
   ```

3. Then, test the GET request on `/users` to see all users stored in the database:

   ```bash
   curl http://localhost:3000/users
   ```

   You should see a list of users, including the one you just created.

### Summary

You’ve successfully integrated a SQLite database into your API using TypeORM, created a user entity, and added functionality to save and retrieve users. This foundational work will allow you to build more complex features in your API.

That wraps up **Day 6**! You’re advancing quickly!

---

Ready for Day 7?

## Day 7

