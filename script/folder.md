# Requirements

1. Create folders.py script.
2. Put each feature in separate function.
3. Only create any folders if not there.
4. Create root folder `../data`.
5. Take first param witch is number of storage folder.
6. Create storage folder named 'storage00n` where n: 1-99.
7. Take second param witch is number of folders to create.
8. Create folders named 'folder00n' where n: 1-99.
9. If folders already exist start adding to existing ones.
10. For example `folders.py 1 5` should add data/storage001 and folder001...folder005.
11. `folders.py 1 1` should add folder006 to data/storage001.
12. `folders.py 2 1` should add folder001 to data/storage002.
13. `folders.py 1 2` should add folder007..folder008 to data/storage001 and so on.
