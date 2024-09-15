# Coffe, Tea app

## Please create me app in typescript, where we have two pictures, coffe, tea. We click on one and date time is saved to json. We should have client for this and also api in nestjs. We should use nx for project, can u do it?

Sure, I can guide you through setting up a TypeScript application with Nx that involves a client-side app and an API. We’ll create a simple application where users can click on images of coffee or tea, and the date and time of the click will be saved to a JSON file. Here’s a step-by-step guide:

### Step 1: Set Up the Nx Workspace

1. **Install Nx CLI**:
   If you don’t have Nx CLI installed, you can install it globally using npm:

   ```bash
   npm install -g nx
   ```

2. **Create a New Nx Workspace**:

   ```bash
   npx create-nx-workspace@latest my-app
   ```

   Follow the prompts to set up your workspace. You can select `empty` to start from scratch.

3. **Navigate to Your Workspace**:
   ```bash
   cd my-app
   ```

### Step 2: Generate the Applications and Libraries

1. **Generate the NestJS API**:

   ```bash
   nx generate @nrwl/nest:application api
   ```

   This will create a NestJS application under the `apps/api` directory.

2. **Generate the React Client Application**:
   ```bash
   nx generate @nrwl/react:application client
   ```
   This will create a React application under the `apps/client` directory.

### Step 3: Implement the NestJS API

1. **Create a Service to Handle Click Data**:

   In `apps/api/src/app/clicks/clicks.service.ts`:

   ```typescript
   import { Injectable } from '@nestjs/common'
   import * as fs from 'fs'
   import * as path from 'path'

   @Injectable()
   export class ClicksService {
     private readonly filePath = path.join(__dirname, '../../clicks.json')

     logClick(dateTime: string) {
       const data = this.readData()
       data.push({ dateTime })
       fs.writeFileSync(this.filePath, JSON.stringify(data, null, 2))
     }

     private readData() {
       if (!fs.existsSync(this.filePath)) {
         return []
       }
       return JSON.parse(fs.readFileSync(this.filePath, 'utf8'))
     }
   }
   ```

2. **Create a Controller**:

   In `apps/api/src/app/clicks/clicks.controller.ts`:

   ```typescript
   import { Controller, Post, Body } from '@nestjs/common'
   import { ClicksService } from './clicks.service'

   @Controller('clicks')
   export class ClicksController {
     constructor(private readonly clicksService: ClicksService) {}

     @Post()
     logClick(@Body('dateTime') dateTime: string) {
       this.clicksService.logClick(dateTime)
     }
   }
   ```

3. **Update the Module**:

   In `apps/api/src/app/app.module.ts`:

   ```typescript
   import { Module } from '@nestjs/common'
   import { ClicksController } from './clicks/clicks.controller'
   import { ClicksService } from './clicks/clicks.service'

   @Module({
     imports: [],
     controllers: [ClicksController],
     providers: [ClicksService],
   })
   export class AppModule {}
   ```

### Step 4: Implement the React Client

1. **Set Up the Component**:

   In `apps/client/src/app/app.tsx`:

   ```typescript
   import React from 'react'
   import axios from 'axios'

   function App() {
     const handleClick = async (drink: string) => {
       const dateTime = new Date().toISOString()
       await axios.post('http://localhost:3333/clicks', { dateTime })
       alert(`Clicked on ${drink}`)
     }

     return (
       <div>
         <h1>Choose a Drink</h1>
         <img
           src="/assets/coffee.png"
           alt="Coffee"
           onClick={() => handleClick('coffee')}
           style={{ cursor: 'pointer', width: '100px' }}
         />
         <img
           src="/assets/tea.png"
           alt="Tea"
           onClick={() => handleClick('tea')}
           style={{ cursor: 'pointer', width: '100px' }}
         />
       </div>
     )
   }

   export default App
   ```

2. **Add Assets**:
   Place `coffee.png` and `tea.png` in `apps/client/src/assets/`.

### Step 5: Run the Application

1. **Start the API**:

   ```bash
   nx serve api
   ```

2. **Start the Client**:
   ```bash
   nx serve client
   ```

Now, you should be able to access the React client at `http://localhost:4200` and the NestJS API at `http://localhost:3333`. Clicking on either image will send a POST request to the API, which will log the click with the current date and time to `clicks.json`.

### Note

- Ensure you have the necessary dependencies installed (`axios` for HTTP requests).
- For a production setup, you might want to consider using a more robust storage solution than a JSON file, such as a database.

This setup provides a basic framework for what you need. You can extend it with more features or enhance it according to your requirements.

## We need to register user by asking him for id, check if it's unique and records will be for this is always. Also mail maybe so we can send him id if he forget.

To enhance the application with user registration, including ID uniqueness check and email functionality for forgotten IDs, follow these steps:

### Step 1: Extend the NestJS API

#### 1.1. Install Required Packages

First, install the required packages for email handling and validation:

```bash
npm install @nestjs/mailer nodemailer class-validator class-transformer
```

#### 1.2. Update the API Module

In `apps/api/src/app/app.module.ts`, import and configure the MailerModule:

```typescript
import { Module } from '@nestjs/common'
import { MailerModule } from '@nestjs/mailer'
import { ClicksController } from './clicks/clicks.controller'
import { ClicksService } from './clicks/clicks.service'
import { UsersController } from './users/users.controller'
import { UsersService } from './users/users.service'
import { TypeOrmModule } from '@nestjs/typeorm'
import { User } from './users/user.entity'

@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: 'sqlite',
      database: 'db.sqlite',
      entities: [User],
      synchronize: true,
    }),
    TypeOrmModule.forFeature([User]),
    MailerModule.forRoot({
      transport: {
        host: 'smtp.example.com', // Replace with your SMTP server
        port: 587,
        secure: false,
        auth: {
          user: 'user@example.com', // Replace with your email
          pass: 'password', // Replace with your email password
        },
      },
    }),
  ],
  controllers: [ClicksController, UsersController],
  providers: [ClicksService, UsersService],
})
export class AppModule {}
```

#### 1.3. Create User Entity

In `apps/api/src/app/users/user.entity.ts`:

```typescript
import { Entity, Column, PrimaryGeneratedColumn } from 'typeorm'

@Entity()
export class User {
  @PrimaryGeneratedColumn()
  id: number

  @Column({ unique: true })
  userId: string

  @Column()
  email: string
}
```

#### 1.4. Create User DTOs

In `apps/api/src/app/users/dto/create-user.dto.ts`:

```typescript
import { IsEmail, IsNotEmpty } from 'class-validator'

export class CreateUserDto {
  @IsNotEmpty()
  userId: string

  @IsEmail()
  email: string
}
```

#### 1.5. Create User Service

In `apps/api/src/app/users/users.service.ts`:

```typescript
import {
  Injectable,
  ConflictException,
  NotFoundException,
} from '@nestjs/common'
import { InjectRepository } from '@nestjs/typeorm'
import { Repository } from 'typeorm'
import { User } from './user.entity'
import { CreateUserDto } from './dto/create-user.dto'
import { MailerService } from '@nestjs/mailer'

@Injectable()
export class UsersService {
  constructor(
    @InjectRepository(User)
    private usersRepository: Repository<User>,
    private mailerService: MailerService
  ) {}

  async createUser(createUserDto: CreateUserDto): Promise<User> {
    const { userId, email } = createUserDto

    const existingUser = await this.usersRepository.findOne({
      where: { userId },
    })
    if (existingUser) {
      throw new ConflictException('User ID already exists')
    }

    const user = this.usersRepository.create({ userId, email })
    await this.usersRepository.save(user)

    // Send email with userId
    await this.mailerService.sendMail({
      to: email,
      subject: 'Your User ID',
      text: `Your User ID is ${userId}`,
    })

    return user
  }

  async findUserById(userId: string): Promise<User> {
    const user = await this.usersRepository.findOne({ where: { userId } })
    if (!user) {
      throw new NotFoundException('User not found')
    }
    return user
  }
}
```

#### 1.6. Create User Controller

In `apps/api/src/app/users/users.controller.ts`:

```typescript
import {
  Body,
  Controller,
  Post,
  Get,
  Param,
  NotFoundException,
} from '@nestjs/common'
import { UsersService } from './users.service'
import { CreateUserDto } from './dto/create-user.dto'

@Controller('users')
export class UsersController {
  constructor(private readonly usersService: UsersService) {}

  @Post()
  async createUser(@Body() createUserDto: CreateUserDto) {
    return this.usersService.createUser(createUserDto)
  }

  @Get(':userId')
  async findUserById(@Param('userId') userId: string) {
    try {
      return await this.usersService.findUserById(userId)
    } catch (e) {
      throw new NotFoundException('User not found')
    }
  }
}
```

### Step 2: Update the React Client

#### 2.1. Update the Registration Form

In `apps/client/src/app/app.tsx`, add a registration form and handle user registration:

```typescript
import React, { useState } from 'react'
import axios from 'axios'

function App() {
  const [userId, setUserId] = useState('')
  const [email, setEmail] = useState('')
  const [message, setMessage] = useState('')

  const handleRegister = async () => {
    try {
      const response = await axios.post('http://localhost:3333/users', {
        userId,
        email,
      })
      setMessage(`User registered with ID: ${response.data.userId}`)
    } catch (error) {
      setMessage('Registration failed. Please check your details.')
    }
  }

  return (
    <div>
      <h1>Register User</h1>
      <input
        type="text"
        placeholder="User ID"
        value={userId}
        onChange={(e) => setUserId(e.target.value)}
      />
      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <button onClick={handleRegister}>Register</button>
      <p>{message}</p>
    </div>
  )
}

export default App
```

### Step 3: Run and Test the Application

1. **Start the API**:

   ```bash
   nx serve api
   ```

2. **Start the Client**:
   ```bash
   nx serve client
   ```

Make sure to replace the SMTP configuration with valid details for sending emails. The NestJS API will handle user creation, ensure unique IDs, and send confirmation emails. The React client allows users to register and will show a message based on the registration outcome.

This setup ensures that user IDs are unique, handles user registration, and integrates email functionality to notify users of their IDs.
