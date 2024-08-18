# Nx Cli api

```bash
npx -version
npm install -g npm@latest
npx create-nx-workspace@latest
npx create-nx-workspace@latest ts-engine-nx
npm install --save-dev @nrwl/js
nx g @nx/js:library engine --directory packages/engine
nx build engine
nx reset
nx build engine
npm install @nrwl/web
npx nx generate @nrwl/web:app client --directory=packages/client --framework=none --style=css --babel
npm i
nx build client
nx serve client
npm i socket.io-client
npm install --save-dev @nrwl/node
nx generate @nrwl/node:application server --directory=packages/server
npm i socket.io
nx reset
npm install -g @nrwl/cli
npm install @nrwl/cli --save-dev
npm install typescript@latest --save-dev
npm i --save-dev @types/jest
nx test engine
nx add @nx/webpack
cd path
code path
```
