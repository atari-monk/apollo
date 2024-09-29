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
import express from 'express'

const app = express()
const port = 3000

// Middleware to parse JSON requests
app.use(express.json())

app.get('/', (req, res) => {
  res.send('Hello, TypeScript API!')
})

// New endpoint to create a user
app.post('/users', (req, res) => {
  const newUser = req.body // Get user data from request body
  console.log('New user:', newUser)
  res.status(201).json({ message: 'User created', user: newUser })
})

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`)
})
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
import { Router } from 'express'

const router = Router()

// GET request for testing
router.get('/', (req, res) => {
  res.send('User route')
})

// POST endpoint to create a user
router.post('/', (req, res) => {
  const newUser = req.body // Get user data from request body
  console.log('New user:', newUser)
  res.status(201).json({ message: 'User created', user: newUser })
})

export default router
```

### Step 3: Modify `app.ts` to Use User Routes

Now, update your `app.ts` to use this new route module:

```typescript
import express from 'express'
import userRoutes from './routes/userRoutes'

const app = express()
const port = 3000

// Middleware to parse JSON requests
app.use(express.json())

// Use the user routes
app.use('/users', userRoutes)

app.get('/', (req, res) => {
  res.send('Hello, TypeScript API!')
})

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`)
})
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
  name: string
  email: string
}
```

### Step 3: Update the User Routes to Use the Interface

Modify your `userRoutes.ts` file to use the `User` interface for type-checking:

```typescript
// src/routes/userRoutes.ts
import { Router, Request, Response } from 'express'
import { User } from '../interfaces/user'

const router = Router()

// GET request for testing
router.get('/', (req: Request, res: Response) => {
  res.send('User route')
})

// POST endpoint to create a user
router.post('/', (req: Request, res: Response) => {
  const newUser: User = req.body // Enforce User interface
  console.log('New user:', newUser)
  res.status(201).json({ message: 'User created', user: newUser })
})

export default router
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
import { body, validationResult } from 'express-validator'
import { Request, Response, NextFunction } from 'express'

export const validateUser = [
  body('name')
    .isString()
    .notEmpty()
    .withMessage('Name is required and must be a string.'),
  body('email')
    .isEmail()
    .withMessage('Email is required and must be a valid email address.'),

  (req: Request, res: Response, next: NextFunction) => {
    const errors = validationResult(req)
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() })
    }
    next()
  },
]
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
import { Router, Request, Response } from 'express'
import { User } from '../interfaces/user'
import { validateUser } from '../middleware/validateUser'

const router = Router()

// GET request for testing
router.get('/', (req: Request, res: Response) => {
  res.send('User route')
})

// POST endpoint to create a user
router.post('/', validateUser, (req: Request, res: Response) => {
  const newUser: User = req.body // Enforce User interface
  console.log('New user:', newUser)
  res.status(201).json({ message: 'User created', user: newUser })
})

export default router
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
import { Entity, PrimaryGeneratedColumn, Column } from 'typeorm'

@Entity()
export class User {
  @PrimaryGeneratedColumn()
  id: number

  @Column()
  name: string

  @Column()
  email: string
}
```

For this model to work, update tsconfig.

```json
{
  "compilerOptions": {
    "experimentalDecorators": true,
    "emitDecoratorMetadata": true,
    "target": "ES2020", // Or at least ES6+
    "module": "commonjs", // Or another valid module system
    "strictPropertyInitialization": false
  }
}
```

### Step 4: Set Up Database Connection in `app.ts`

Update your `app.ts` file to establish a database connection when the application starts:

```typescript
import express from 'express'
import { createConnection } from 'typeorm'
import userRoutes from './routes/userRoutes'

const app = express()
const port = 3000

// Middleware to parse JSON requests
app.use(express.json())

// Use the user routes
app.use('/users', userRoutes)

// Establish database connection
createConnection()
  .then(() => {
    console.log('Database connected successfully!')
    app.listen(port, () => {
      console.log(`Server running on http://localhost:${port}`)
    })
  })
  .catch((error) => {
    console.error('Database connection failed:', error)
  })
```

This createConnection was deprecated.  
Fixed with:

```typescript
//data_source.ts
const AppDataSource = new DataSource({
  type: 'mysql', // or your database type, e.g., 'postgres'
  host: 'localhost',
  port: 3306, // or the appropriate port
  username: 'your_db_username',
  password: 'your_db_password',
  database: 'your_db_name',
  synchronize: true, // synchronize schema
  entities: ['src/entity/*.ts'], // or wherever your entities are located
})

//app.ts
// Initialize the DataSource (connection to the database)
AppDataSource.initialize()
  .then(() => {
    console.log('Database connected successfully!')
    app.listen(port, () => {
      console.log(`Server running on http://localhost:${port}`)
    })
  })
  .catch((error) => {
    console.error('Database connection failed:', error)
  })
```

### Step 5: Update the User Route to Save Users

Modify your `userRoutes.ts` to save the user data to the database:

```typescript
// src/routes/userRoutes.ts
import { Router, Request, Response } from 'express'
import { User } from '../interfaces/user'
import { validateUser } from '../middleware/validateUser'
import { getRepository } from 'typeorm'
import { User as UserEntity } from '../entities/User'

const router = Router()

// GET request for testing
router.get('/', async (req: Request, res: Response) => {
  const users = await getRepository(UserEntity).find()
  res.json(users)
})

// POST endpoint to create a user
router.post('/', validateUser, async (req: Request, res: Response) => {
  const newUser: User = req.body // Enforce User interface

  // Create a new user instance
  const userEntity = getRepository(UserEntity).create(newUser)

  // Save the user to the database
  const savedUser = await getRepository(UserEntity).save(userEntity)

  res.status(201).json({ message: 'User created', user: savedUser })
})

export default router
```

To fix this above:

```typescript
// GET request for testing
router.get('/', async (req: Request, res: Response) => {
  try {
    const userRepository = AppDataSource.getRepository(UserEntity)
    const users = await userRepository.find()
    res.json(users)
  } catch (error) {
    res.status(500).json({ message: 'Failed to retrieve users', error })
  }
})

// POST endpoint to create a user
router.post('/', validateUser, async (req: Request, res: Response) => {
  try {
    const newUser: User = req.body // Enforce User interface

    // Get the repository and create a new user instance
    const userRepository = AppDataSource.getRepository(UserEntity)
    const userEntity = userRepository.create(newUser)

    // Save the user to the database
    const savedUser = await userRepository.save(userEntity)

    res.status(201).json({ message: 'User created', user: savedUser })
  } catch (error) {
    res.status(500).json({ message: 'Failed to create user', error })
  }
})
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

**Day 7: Implementing User Data Retrieval and Deletion**

Today, we’ll expand our API by adding functionality to retrieve a single user by ID and to delete a user. This will enhance the CRUD capabilities of your API.

### Step 1: Update User Routes for Retrieval and Deletion

Modify your `userRoutes.ts` file to include GET and DELETE endpoints:

```typescript
// src/routes/userRoutes.ts
import { Router, Request, Response } from 'express'
import { User } from '../interfaces/user'
import { validateUser } from '../middleware/validateUser'
import { getRepository } from 'typeorm'
import { User as UserEntity } from '../entities/User'

const router = Router()

// GET all users
router.get('/', async (req: Request, res: Response) => {
  const users = await getRepository(UserEntity).find()
  res.json(users)
})

// POST endpoint to create a user
router.post('/', validateUser, async (req: Request, res: Response) => {
  const newUser: User = req.body // Enforce User interface
  const userEntity = getRepository(UserEntity).create(newUser)
  const savedUser = await getRepository(UserEntity).save(userEntity)
  res.status(201).json({ message: 'User created', user: savedUser })
})

// GET a user by ID
router.get('/:id', async (req: Request, res: Response) => {
  const userId = parseInt(req.params.id)
  const user = await getRepository(UserEntity).findOne(userId)

  if (!user) {
    return res.status(404).json({ message: 'User not found' })
  }

  res.json(user)
})

// DELETE a user by ID
router.delete('/:id', async (req: Request, res: Response) => {
  const userId = parseInt(req.params.id)
  const result = await getRepository(UserEntity).delete(userId)

  if (result.affected === 0) {
    return res.status(404).json({ message: 'User not found' })
  }

  res.status(204).send() // No content to send back
})

export default router
```

### Step 2: Testing the New Endpoints

1. **Get a User by ID:**

   - First, create a user using the POST request to `http://localhost:3000/users`.

   - Then, retrieve that user by making a GET request to `http://localhost:3000/users/{id}`, replacing `{id}` with the actual user ID.

   **Using Postman:**

   - URL: `http://localhost:3000/users/1` (assuming 1 is the user ID).
   - You should receive the user data in response.

   **Using CURL:**

   ```bash
   curl http://localhost:3000/users/1
   ```

2. **Delete a User by ID:**

   - To delete a user, send a DELETE request to `http://localhost:3000/users/{id}`.

   **Using Postman:**

   - Method: DELETE
   - URL: `http://localhost:3000/users/1`.

   **Using CURL:**

   ```bash
   curl -X DELETE http://localhost:3000/users/1
   ```

   You should receive a `204 No Content` response if the user was successfully deleted. If the user does not exist, you will get a `404 Not Found` response.

### Summary

You’ve added retrieval and deletion functionality to your API, allowing users to be fetched by ID and removed from the database. This enhances the API’s CRUD capabilities significantly.

That concludes **Day 7**! You’re building a comprehensive API!

---

Ready for Day 8?

## Day 8

**Day 8: Adding Update Functionality and Response Formatting**

Today, we’ll implement the ability to update user details in our API. We will also standardize our response formatting to ensure consistency across different endpoints.

### Step 1: Update User Routes for Updating User Data

Modify your `userRoutes.ts` file to include a PUT endpoint for updating user details:

```typescript
// src/routes/userRoutes.ts
import { Router, Request, Response } from 'express'
import { User } from '../interfaces/user'
import { validateUser } from '../middleware/validateUser'
import { getRepository } from 'typeorm'
import { User as UserEntity } from '../entities/User'

const router = Router()

// GET all users
router.get('/', async (req: Request, res: Response) => {
  const users = await getRepository(UserEntity).find()
  res.json({ message: 'Users retrieved successfully', data: users })
})

// POST endpoint to create a user
router.post('/', validateUser, async (req: Request, res: Response) => {
  const newUser: User = req.body
  const userEntity = getRepository(UserEntity).create(newUser)
  const savedUser = await getRepository(UserEntity).save(userEntity)
  res
    .status(201)
    .json({ message: 'User created successfully', data: savedUser })
})

// GET a user by ID
router.get('/:id', async (req: Request, res: Response) => {
  const userId = parseInt(req.params.id)
  const user = await getRepository(UserEntity).findOne(userId)

  if (!user) {
    return res.status(404).json({ message: 'User not found' })
  }

  res.json({ message: 'User retrieved successfully', data: user })
})

// DELETE a user by ID
router.delete('/:id', async (req: Request, res: Response) => {
  const userId = parseInt(req.params.id)
  const result = await getRepository(UserEntity).delete(userId)

  if (result.affected === 0) {
    return res.status(404).json({ message: 'User not found' })
  }

  res.status(204).send() // No content to send back
})

// PUT endpoint to update user details
router.put('/:id', validateUser, async (req: Request, res: Response) => {
  const userId = parseInt(req.params.id)
  const updatedData: User = req.body

  // Find the existing user
  const user = await getRepository(UserEntity).findOne(userId)

  if (!user) {
    return res.status(404).json({ message: 'User not found' })
  }

  // Update user data
  getRepository(UserEntity).merge(user, updatedData)
  const updatedUser = await getRepository(UserEntity).save(user)

  res.json({ message: 'User updated successfully', data: updatedUser })
})

export default router
```

### Step 2: Understanding the New PUT Endpoint

1. **PUT /users/:id**:
   - The PUT endpoint accepts user data and updates the specified user.
   - It first checks if the user exists. If not, it returns a `404 Not Found`.
   - If the user is found, it merges the existing user with the new data and saves it.

### Step 3: Testing the Update Functionality

1. **Create a user** using the POST endpoint if you haven’t done so already.

2. **Update a user** by sending a PUT request to the endpoint.

   **Using Postman:**

   - URL: `http://localhost:3000/users/1` (replace `1` with the actual user ID).
   - Method: PUT
   - Body:
     ```json
     {
       "name": "Alice Updated",
       "email": "alice.updated@example.com"
     }
     ```

   **Using CURL:**

   ```bash
   curl -X PUT http://localhost:3000/users/1 -H "Content-Type: application/json" -d '{"name":"Alice Updated","email":"alice.updated@example.com"}'
   ```

   You should receive a response confirming that the user has been updated.

3. **Retrieve the user again** using the GET endpoint to verify the changes.

### Summary

You’ve successfully added update functionality to your API, allowing users to modify their details. Additionally, you standardized the response format across different endpoints for better consistency.

That wraps up **Day 8**! You’re getting closer to having a fully functional API!

---

Ready for Day 9?

## Day 9

**Day 9: Adding Authentication with JWT**

Today, we’ll implement authentication for your API using JSON Web Tokens (JWT). This will allow you to secure your routes and ensure that only authenticated users can access certain resources.

### Step 1: Install Required Packages

You’ll need to install `jsonwebtoken` and `bcrypt` for handling token generation and password hashing:

```bash
npm install jsonwebtoken bcrypt
```

### Step 2: Update User Entity for Password Storage

Modify your `User` entity to include a password field. Update your `src/entities/User.ts` file:

```typescript
// src/entities/User.ts
import { Entity, PrimaryGeneratedColumn, Column } from 'typeorm'

@Entity()
export class User {
  @PrimaryGeneratedColumn()
  id: number

  @Column()
  name: string

  @Column()
  email: string

  @Column()
  password: string // New password field
}
```

### Step 3: Create Authentication Routes

Create a new file named `authRoutes.ts` in the `src/routes` directory:

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
      authRoutes.ts
    app.ts
```

In `authRoutes.ts`, implement user registration and login functionality:

```typescript
// src/routes/authRoutes.ts
import { Router, Request, Response } from 'express'
import { getRepository } from 'typeorm'
import bcrypt from 'bcrypt'
import jwt from 'jsonwebtoken'
import { User as UserEntity } from '../entities/User'
import { User } from '../interfaces/user'

const router = Router()
const JWT_SECRET = 'your_jwt_secret' // Use a secure key in production

// POST endpoint to register a user
router.post('/register', async (req: Request, res: Response) => {
  const { name, email, password }: User = req.body

  // Hash the password
  const hashedPassword = await bcrypt.hash(password, 10)

  // Create and save user
  const user = getRepository(UserEntity).create({
    name,
    email,
    password: hashedPassword,
  })

  const savedUser = await getRepository(UserEntity).save(user)
  res
    .status(201)
    .json({ message: 'User registered successfully', data: savedUser })
})

// POST endpoint to login a user
router.post('/login', async (req: Request, res: Response) => {
  const { email, password } = req.body

  // Find user by email
  const user = await getRepository(UserEntity).findOne({ where: { email } })

  if (!user) {
    return res.status(401).json({ message: 'Invalid email or password' })
  }

  // Compare password with hashed password
  const isPasswordValid = await bcrypt.compare(password, user.password)

  if (!isPasswordValid) {
    return res.status(401).json({ message: 'Invalid email or password' })
  }

  // Create JWT token
  const token = jwt.sign({ id: user.id }, JWT_SECRET, { expiresIn: '1h' })

  res.json({ message: 'Login successful', token })
})

export default router
```

### Step 4: Secure Your Routes

Now, you need to create middleware for protecting your routes. Create a new file named `authMiddleware.ts` in the `src/middleware` directory:

```
/my-api
  /src
    /middleware
      authMiddleware.ts
```

Add the following code to `authMiddleware.ts`:

```typescript
// src/middleware/authMiddleware.ts
import { Request, Response, NextFunction } from 'express'
import jwt from 'jsonwebtoken'

const JWT_SECRET = 'your_jwt_secret' // Use the same secret key

export const authenticateJWT = (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  const token = req.headers['authorization']?.split(' ')[1]

  if (!token) {
    return res.sendStatus(401)
  }

  jwt.verify(token, JWT_SECRET, (err, user) => {
    if (err) {
      return res.sendStatus(403)
    }
    req.user = user // Save user info in the request
    next()
  })
}
```

### Step 5: Use the Authentication Middleware

Update your `app.ts` to include the authentication routes and protect user-related routes:

```typescript
import express from 'express'
import { createConnection } from 'typeorm'
import userRoutes from './routes/userRoutes'
import authRoutes from './routes/authRoutes'
import { authenticateJWT } from './middleware/authMiddleware'

const app = express()
const port = 3000

// Middleware to parse JSON requests
app.use(express.json())

// Use authentication routes
app.use('/auth', authRoutes)

// Use user routes and protect them
app.use('/users', authenticateJWT, userRoutes)

// Establish database connection
createConnection()
  .then(() => {
    console.log('Database connected successfully!')
    app.listen(port, () => {
      console.log(`Server running on http://localhost:${port}`)
    })
  })
  .catch((error) => {
    console.error('Database connection failed:', error)
  })
```

### Step 6: Testing the Authentication Functionality

1. **Register a User:**

   - Make a POST request to `http://localhost:3000/auth/register` with the following JSON body:

   ```json
   {
     "name": "John Doe",
     "email": "john.doe@example.com",
     "password": "your_secure_password"
   }
   ```

2. **Login to Get a Token:**

   - Make a POST request to `http://localhost:3000/auth/login` with the following JSON body:

   ```json
   {
     "email": "john.doe@example.com",
     "password": "your_secure_password"
   }
   ```

   - You should receive a token in the response.

3. **Access Protected User Routes:**

   - Use the token received from the login response to access the user routes. For example, make a GET request to `http://localhost:3000/users`:

   **Using Postman:**

   - Set the Authorization header to `Bearer your_token`.

   **Using CURL:**

   ```bash
   curl http://localhost:3000/users -H "Authorization: Bearer your_token"
   ```

   If the token is valid, you should receive the list of users. If the token is missing or invalid, you will get a `401 Unauthorized` response.

### Summary

You’ve successfully implemented authentication in your API using JWT. This allows you to secure your routes, ensuring that only authenticated users can access sensitive information.

That wraps up **Day 9**! You’re almost at the finish line!

---

Ready for Day 10?

## Day 10

**Day 10: Final Touches and Deployment Preparation**

Congratulations on reaching Day 10! Today, we’ll focus on finalizing your API by adding error handling, configuring environment variables, and discussing deployment strategies.

### Step 1: Adding Error Handling

To ensure your API responds gracefully to errors, create a centralized error-handling middleware.

1. **Create an error handling middleware:**

   Create a new file named `errorMiddleware.ts` in the `src/middleware` directory:

   ```typescript
   // src/middleware/errorMiddleware.ts
   import { Request, Response, NextFunction } from 'express'

   export const errorHandler = (
     err: any,
     req: Request,
     res: Response,
     next: NextFunction
   ) => {
     console.error(err.stack) // Log the error for debugging
     res.status(500).json({ message: 'An unexpected error occurred' })
   }
   ```

2. **Update `app.ts` to include the error handling middleware:**

   Add the error handling middleware after your route definitions in `app.ts`:

   ```typescript
   import express from 'express'
   import { createConnection } from 'typeorm'
   import userRoutes from './routes/userRoutes'
   import authRoutes from './routes/authRoutes'
   import { authenticateJWT } from './middleware/authMiddleware'
   import { errorHandler } from './middleware/errorMiddleware'

   const app = express()
   const port = 3000

   app.use(express.json())
   app.use('/auth', authRoutes)
   app.use('/users', authenticateJWT, userRoutes)

   // Centralized error handling middleware
   app.use(errorHandler)

   createConnection()
     .then(() => {
       console.log('Database connected successfully!')
       app.listen(port, () => {
         console.log(`Server running on http://localhost:${port}`)
       })
     })
     .catch((error) => {
       console.error('Database connection failed:', error)
     })
   ```

### Step 2: Configuring Environment Variables

To avoid hardcoding sensitive information like JWT secret and database configurations, use environment variables.

1. **Install `dotenv` package:**

   ```bash
   npm install dotenv
   ```

2. **Create a `.env` file in the root of your project:**

   ```plaintext
   JWT_SECRET=your_jwt_secret
   DATABASE_TYPE=sqlite
   DATABASE_NAME=database.sqlite
   ```

3. **Update your `app.ts` to load environment variables:**

   At the top of `app.ts`, import and configure `dotenv`:

   ```typescript
   import express from 'express'
   import { createConnection } from 'typeorm'
   import userRoutes from './routes/userRoutes'
   import authRoutes from './routes/authRoutes'
   import { authenticateJWT } from './middleware/authMiddleware'
   import { errorHandler } from './middleware/errorMiddleware'
   import dotenv from 'dotenv'

   dotenv.config() // Load environment variables from .env file

   const app = express()
   const port = 3000

   app.use(express.json())
   app.use('/auth', authRoutes)
   app.use('/users', authenticateJWT, userRoutes)
   app.use(errorHandler)

   createConnection({
     type: process.env.DATABASE_TYPE as 'sqlite',
     database: process.env.DATABASE_NAME,
     synchronize: true,
     entities: ['src/entities/**/*.ts'],
   })
     .then(() => {
       console.log('Database connected successfully!')
       app.listen(port, () => {
         console.log(`Server running on http://localhost:${port}`)
       })
     })
     .catch((error) => {
       console.error('Database connection failed:', error)
     })
   ```

### Step 3: Testing Your API

Before deploying, ensure everything works as expected:

- Test all endpoints: Register, login, retrieve, update, and delete users.
- Confirm that error handling works by testing invalid requests.

### Step 4: Deployment Preparation

Now, let's discuss how to deploy your API.

1. **Choose a Hosting Provider:**

   - Popular options include Heroku, Vercel, AWS, or DigitalOcean.

2. **Prepare Your Application:**

   - Ensure you have a `start` script in your `package.json`:
     ```json
     "scripts": {
       "start": "node dist/app.js",
       "build": "tsc"
     }
     ```

3. **Build Your Application:**

   - Run TypeScript compiler to generate JavaScript files:
     ```bash
     npm run build
     ```

4. **Deploy Your Application:**

   - Follow the deployment instructions for your chosen provider. For example, on Heroku, you can use:
     ```bash
     heroku create
     git push heroku main
     ```

5. **Set Environment Variables on the Server:**
   - Use the platform’s dashboard or CLI to set your environment variables for JWT secret and database connection.

### Summary

You’ve completed your API project by adding error handling, configuring environment variables, and preparing for deployment. You now have a fully functional and secure RESTful API!

**Final Thoughts:**

- Explore additional features such as rate limiting, input validation, or integration with frontend applications.
- Keep learning about best practices in API development.

That concludes your **10-day adventure** in creating a RESTful API with TypeScript! Congratulations on your achievement!

---

If you have any questions or need further assistance, feel free to ask!
