# Log

## A lot of time lost using nx generator, template wont compile. (nextjs, react)

## Log of setup that worked

npm install -g nx
npm install -g npm@10.8.3
npx create-nx-workspace@latest helios
https://nx.dev/getting-started/intro
√ Which stack do you want to use? · none
√ Package-based monorepo, integrated monorepo, or standalone project? · integrated
√ Which CI provider would you like to use? · github
PS C:\atari-monk\code> cd .\helios\
npm install @nrwl/next
nx g @nrwl/next:app helios_client --style=tailwind --ts
 NX  Generating @nrwl/next:application
√ Which E2E test runner would you like to use? · playwright
√ Would you like to use the App Router (recommended)? (Y/n) · true
√ Would you like to use `src/` directory? (Y/n) · true
√ What should be the project name and where should it be generated? · helios_client @ helios_client
Fetching prettier...
Fetching @nx/playwright...
Fetching @nx/jest...
CREATE tsconfig.base.json
CREATE .prettierrc
CREATE .prettierignore
UPDATE .vscode/extensions.json
UPDATE package.json
UPDATE nx.json
UPDATE .gitignore
CREATE helios_client/index.d.ts
CREATE helios_client/next-env.d.ts
CREATE helios_client/next.config.js
CREATE helios_client/public/.gitkeep
CREATE helios_client/public/favicon.ico
CREATE helios_client/specs/index.spec.tsx
CREATE helios_client/tsconfig.json
CREATE helios_client/src/app/api/hello/route.ts
CREATE helios_client/src/app/global.css
CREATE helios_client/src/app/page.tsx
CREATE helios_client/src/app/layout.tsx
CREATE helios_client/project.json
CREATE helios_client-e2e/project.json
CREATE helios_client-e2e/playwright.config.ts
CREATE helios_client-e2e/src/example.spec.ts
CREATE helios_client-e2e/tsconfig.json
CREATE .eslintrc.json
CREATE .eslintignore
CREATE helios_client-e2e/.eslintrc.json
CREATE jest.preset.js
CREATE jest.config.ts
CREATE helios_client/jest.config.ts
CREATE helios_client/tsconfig.spec.json
CREATE helios_client/.eslintrc.json
CREATE helios_client/postcss.config.js
CREATE helios_client/tailwind.config.js
Run "nx show project helios_client" to view details about this project.

## Project commands

npx nx run helios_client:dev 

## Babylon integration

npm install @babylonjs/core @babylonjs/gui @babylonjs/loaders
