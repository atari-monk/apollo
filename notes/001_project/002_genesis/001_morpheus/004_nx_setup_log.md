# Nx Setup

[Up](index.md)
[Main](../../../../index.md)

- Logs from terminal collected during ts-engine-nx initial setup

```bash
//ctrl + c to cancel command
PS C:\atari-monk\code>
npx -version
10.8.2
npm install -g npm@latest
npx -version
10.8.2
//no folder, will prompt
npx create-nx-workspace@latest
//with folder
npx create-nx-workspace@latest ts-engine-nx
NX Let's create a new workspace [https://nx.dev/getting-started/intro]
√ Which stack do you want to use? · none
√ Package-based monorepo, integrated monorepo, or standalone project? · package-based
√ Set up CI with caching, distribution and test deflaking · github
NX Creating your v19.4.2 workspace.
✔ Installing dependencies with npm
✔ Successfully created the workspace: ts-engine-nx.
Switched to a new branch 'main'
warning: LF will be replaced by CRLF in .gitignore.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in .vscode/extensions.json.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in README.md.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in nx.json.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in package-lock.json.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in package.json.
The file will have its original line endings in your working directory
✔ CI workflow with Nx Cloud has been generated successfully
✔ CI workflow has been generated successfully
NX Your Nx Cloud workspace is ready.
To claim it, connect it to your Nx Cloud account:

- Push your repository to your git hosting provider.
- Go to the following URL to connect your workspace to Nx Cloud:
  https://cloud.nx.app/connect/afKwkExnVn
  NX First time using Nx? Check out this interactive Nx tutorial.
  https://nx.dev/getting-started/tutorials/npm-workspaces-tutorial
  npm install --save-dev @nrwl/js
  nx g @nx/js:library engine --directory packages/engine
  NX Generating @nx/js:library
  √ Which unit test runner would you like to use? · jest
  √ Which bundler would you like to use to build the library? Choose 'none' to skip build setup. · tsc
  √ What should be the project name and where should it be generated? · engine @ packages/engine
  CREATE tsconfig.base.json
  CREATE .prettierrc
  CREATE .prettierignore
  UPDATE .vscode/extensions.json
  UPDATE package.json
  CREATE packages/engine/tsconfig.json
  CREATE packages/engine/src/index.ts
  CREATE packages/engine/src/lib/engine.spec.ts
  CREATE packages/engine/src/lib/engine.ts
  CREATE packages/engine/tsconfig.lib.json
  CREATE packages/engine/README.md
  CREATE packages/engine/package.json
  UPDATE nx.json
  CREATE packages/engine/project.json
  CREATE .eslintrc.json
  CREATE .eslintignore
  CREATE packages/engine/.eslintrc.json
  CREATE jest.preset.js
  CREATE jest.config.ts
  CREATE packages/engine/jest.config.ts
  CREATE packages/engine/tsconfig.spec.json
  npm warn deprecated inflight@1.0.6: This module is not supported, and leaks memory. Do not use it. Check out lru-cache if you want a good and tested way to coalesce async requests by a key value, which is much more comprehensive and powerful.
  npm warn deprecated @humanwhocodes/config-array@0.11.14: Use @eslint/config-array instead
  npm warn deprecated rimraf@3.0.2: Rimraf versions prior to v4 are no longer supported
  npm warn deprecated glob@7.2.3: Glob versions prior to v9 are no longer supported
  npm warn deprecated @humanwhocodes/object-schema@2.0.3: Use @eslint/object-schema instead
  changed 249 packages, and audited 608 packages in 19s
  82 packages are looking for funding
  run `npm fund` for details
  found 0 vulnerabilities
  NX 👀 View Details of engine
  Run "nx show project engine --web" to view details about this project.
  nx build engine
  nx reset
  nx build engine
  npm install @nrwl/web
  npx nx generate @nrwl/web:app client --directory=packages/client --framework=none --style=css --babel
  NX Generating @nrwl/web:application
  √ Which bundler do you want to use? · webpack
  √ Which E2E test runner would you like to use? · playwright
  √ What should be the project name and where should it be generated? · client @ packages/client
  Fetching @nx/webpack...
  Fetching @nx/playwright...
  UPDATE package.json
  Fetching @nx/webpack...
  Fetching @nx/playwright...
  UPDATE package.json
  UPDATE package.json
  CREATE packages/client/project.json
  UPDATE nx.json
  CREATE packages/client/webpack.config.js
  CREATE packages/client/src/app/app.element.spec.ts
  CREATE packages/client/src/app/app.element.ts
  CREATE packages/client/src/app/app.element.css
  CREATE packages/client/src/assets/.gitkeep
  CREATE packages/client/src/favicon.ico
  CREATE packages/client/src/index.html
  CREATE packages/client/src/main.ts
  CREATE packages/client/src/styles.css
  CREATE packages/client/tsconfig.app.json
  CREATE packages/client/tsconfig.json
  CREATE packages/client/.eslintrc.json
  CREATE packages/client-e2e/project.json
  CREATE packages/client-e2e/playwright.config.ts
  CREATE packages/client-e2e/src/example.spec.ts
  CREATE packages/client-e2e/tsconfig.json
  CREATE packages/client-e2e/.eslintrc.json
  UPDATE .vscode/extensions.json
  CREATE packages/client/jest.config.ts
  CREATE packages/client/src/test-setup.ts
  CREATE packages/client/tsconfig.spec.json
  CREATE packages/client/.swcrc
  npm warn deprecated abab@2.0.6: Use your platform's native atob() and btoa() methods instead
  npm warn deprecated domexception@4.0.0: Use your platform's native DOMException instead
  added 457 packages, removed 1 package, and audited 1103 packages in 1m
  168 packages are looking for funding
  run `npm fund` for details
  found 0 vulnerabilities
  NX Ensuring Playwright is installed.
  use --skipInstall to skip installation.
  NX 👀 View Details of client
  Run "nx show project client --web" to view details about this project.
  npm i
  nx build client
  > nx run client:build
  > webpack-cli build --node-env=production
  > Entrypoint main 26.5 KiB = runtime.25b303e50953793c.js 2.09 KiB main.16e04f53007d5b66.css 6.15 KiB main.c2d6cfe60eff9fa3.js 18.3 KiB
  > Entrypoint styles 2.24 KiB = runtime.25b303e50953793c.js 2.09 KiB styles.ef46db3751d8e999.css 0 bytes styles.59f32afc157522b3.js 152 bytes
  > chunk (runtime: runtime) runtime.25b303e50953793c.js (runtime) 2.45 KiB [entry] [rendered]
  > chunk (runtime: runtime) main.16e04f53007d5b66.css, main.c2d6cfe60eff9fa3.js (main) 18.2 KiB (javascript) 8.85 KiB (css/mini-extract) [initial] [rendered]
  > chunk (runtime: runtime) styles.ef46db3751d8e999.css, styles.59f32afc157522b3.js (styles) 50 bytes (javascript) 80 bytes (css/mini-extract) [initial] [rendered]
  > webpack compiled successfully (781e6335ea838c7d)
  > ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  > NX Successfully ran target build for project client (7s)
  > View logs and investigate cache misses at https://nx.app/runs/TFNH3ctLND
  > nx serve client
  > nx run client:serve
  > webpack-cli serve --node-env=development
  > <i> [webpack-dev-server] Project is running at:
  > <i> [webpack-dev-server] Loopback: http://localhost:4200/
  > <i> [webpack-dev-server] On Your Network (IPv4): http://192.168.1.25:4200/ > <i> [webpack-dev-server] Content not from webpack is served from 'C:\atari-monk\code\ts-engine-nx\packages\client\public' directory
  > Entrypoint main [big] 261 KiB (417 KiB) = runtime.js 46.9 KiB vendor.js 186 KiB main.css 8.89 KiB main.js 19.3 KiB 4 auxiliary assets
  > Entrypoint styles 234 KiB (385 KiB) = runtime.js 46.9 KiB styles.css 119 bytes styles.js 187 KiB 3 auxiliary assets
  > chunk (runtime: runtime) main.css, main.js (main) 18.6 KiB (javascript) 8.85 KiB (css/mini-extract) [initial] [rendered]
  > chunk (runtime: runtime) runtime.js (runtime) 31.6 KiB [entry] [rendered]
  > chunk (runtime: runtime) styles.css, styles.js (styles) 180 KiB (javascript) 80 bytes (css/mini-extract) [initial] [rendered]
  > chunk (runtime: runtime) vendor.js (vendor) (id hint: vendor) 180 KiB [initial] [rendered] split chunk (cache group: vendor) (name: vendor)
  > webpack compiled successfully (d747fecf3949bb22)
  > Type-checking in progress...
  > No errors found.
  > npm i socket.io-client
  > npm install --save-dev @nrwl/node
  > added 19 packages, and audited 1133 packages in 25s
  > 168 packages are looking for funding
  > run `npm fund` for details
  > found 0 vulnerabilities
  > PS C:\atari-monk\code\ts-engine-nx> nx generate @nrwl/node:application server --directory=packages/server
  > NX Generating @nrwl/node:application
  > √ Which framework do you want to use? · express
  > √ What should be the project name and where should it be generated? · server @ packages/server
  > UPDATE package.json
  > CREATE packages/server/src/assets/.gitkeep
  > CREATE packages/server/src/main.ts
  > CREATE packages/server/tsconfig.app.json
  > CREATE packages/server/tsconfig.json
  > UPDATE nx.json
  > CREATE packages/server/project.json
  > CREATE packages/server/.eslintrc.json
  > CREATE packages/server/jest.config.ts
  > CREATE packages/server/tsconfig.spec.json
  > CREATE packages/server-e2e/project.json
  > CREATE packages/server-e2e/jest.config.ts
  > CREATE packages/server-e2e/src/support/global-setup.ts
  > CREATE packages/server-e2e/src/support/global-teardown.ts
  > CREATE packages/server-e2e/src/support/test-setup.ts
  > CREATE packages/server-e2e/src/server/server.spec.ts
  > CREATE packages/server-e2e/tsconfig.json
  > CREATE packages/server-e2e/tsconfig.spec.json
  > CREATE packages/server-e2e/.eslintrc.json
  > added 46 packages, removed 13 packages, changed 7 packages, and audited 1166 packages in 19s
  > 168 packages are looking for funding
  > run `npm fund` for details
  > 1 moderate severity vulnerability
  > To address all issues, run:
  > npm audit fix --force
  > Run `npm audit` for details.
  > NX 👀 View Details of server-e2e
  > Run "nx show project server-e2e --web" to view details about this project.
  > NX 👀 View Details of server
  > Run "nx show project server --web" to view details about this project.
```

[Up](index.md)
[Main](../../../../index.md)
