# Generating Api

Task: Generating api.  
Stack: NX, NestJS.

## Installation

### NX

    ```bash
    npm install -g nx
    ```

    or if you're using Yarn:

    ```bash
    yarn global add nx
    ```

    ```bash
    nx --version
    ```

    or

    ```bash
    nx -v
    ```

---

## Create Workspace (project)

-   notes-nx is example name

```bash
npx create-nx-workspace@latest notes-nx
```

-   Add NestJS plugin

```bash
npm install --save-dev @nrwl/nest
```

or

```bash
yarn add --dev @nrwl/nest
```

---

## Generate nestjs app

```bash
npx nx g @nrwl/nest:application packages/notes-api
```

---

[Back to Index](../index.md)
