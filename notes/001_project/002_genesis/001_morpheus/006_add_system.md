# How to add system to `Morpheus` engine

## Version 1.0.0

- To add new system into ecs one needs to preform steps:

1. Ctrl + J to open terminal and paste command:
   ```bash
   code packages/engine/src/ecs/system/builder/data_provider/step/instance/engineSystem.ts
   ```
2. Add new method thats is creating instance of new system
3. Run in terminal:

   ```bash
   code packages/engine/src/ecs/system/builder/data_provider/step/instance/engineSystemMap.ts
   ```

4. Add new map entry for this method
5. Run in terminal:

   ```bash
   code packages/engine/src/ecs/system/builder/data_provider/step/validation/systemValidationMap.ts
   ```

6. Add new map entry for this new system
7. Run in terminal, (use config you need, here editor as example):

   ```bash
   code packages/client/src/assets/data/config/editor.json
   ```

8. In system config add new entry and turn system flag on
9. Run in terminal, (use path you need to load your scene, here as example):

   ```bash
   code packages\client\src\assets\data\feature\scaling\field_colliders\system.json
   ```

10. Add new record for a system

---

Files that may need update:

```bash
code packages/engine/src/ecs/system/builder/data_provider/step/instance/engineSystem.ts
```

```bash
code packages/engine/src/ecs/system/builder/data_provider/step/instance/engineSystemMap.ts
```

```bash
code packages/engine/src/ecs/system/builder/data_provider/step/validation/systemValidationMap.ts
```

```bash
code packages/client/src/assets/data/config/editor.json
```
