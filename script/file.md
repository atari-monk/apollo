# Requirements

1. Create file.py script.
2. Put each feature in separate function.
3. Only create any files if not there.
4. I have file system structure:

```plaintext
data
|__storage001
|   |__folder001
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
6. Take param, that means file count, n: 1-999 to generate.
7. Add number of files with proper name file00n.md, create if not there, add new till 999.
8. Do not add files beyound 999 in folder.
9. For example `file 1 1 1` should add file 'file001.md' to ../data/storage001/folder001.
10. Next `file 1 1 1` should add file 'file002.md' to ../data/storage001/folder001.
11. Next `file 1 1 2` should add file 'file003.md'...'file004.md' to ../data/storage001/.
11. Next `file 1 2 1` should add file 'file001.md' to ../data/storage001/folder001.
