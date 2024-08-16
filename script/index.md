# Requirements

1. Create index.py script.
2. Put each feature in separate function.
3. Only create any files if not there.
4. I have file system structure:

```plaintext
data
|__storage001
|   |__folder001
|   |   |__ file001
|   |   |__ file00n
|   |__folder002
|   |__...
|__storage002
    |__folder001
    |__folder002
    |__...
.
.
.
|__storage099
```

4. Take param, that means storage nr, n: 1-99.
5. Take param, that means folder nr, n: 1-99.
6. Add or override a file named `index.md` where in content generate numbered list of links to files in format [File001](file001.md).
7. For example `index 1 1` should add/override file 'index.md' to ../data/storage001/folder001 with links to files in this folder.
8. Next `file 2 2` should add file 'index.md' to ../data/storage002/folder002 and so on.
