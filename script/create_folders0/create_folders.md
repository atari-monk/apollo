# Script `create_folders.py` prompts.

1. Ok create me a cript that will make root and storageN with 100 folders but only if it dosent exist, take storage nr as param.

2. Dont create subfolders 0..100 if they present.

3. Do 100 not 101 folders so i gues 99.

4. I see code is not dry.

5. Lets leave root folder name hard coded but lets take storage number as script param.

6. This is fine, now add a method that will generate index.md in each folder001 - 99 with this content: #.

7. Ok but do not place index.md in data and storage folders, only in folder000, also start numbering folders form 001 to 099.

8. I would like also file001 - file010 created along with index.md

```markdown
#

1. [File001](file001.md)
```

With each invoke of script it should add 10 more files and update index.md.

9.  Thats fine but number files independently in each folder from 001 up.

10. Yes but i invoked script `python .\create_folders.py 1` and once more.  
    It didnt generate files from 011.  
    Didnt update index.md and numbers in index are only 1.

11. Create a method that will add default content to files.  
    Can we do something about index ?  
    It should have a numbered list, we should also update this.

    ```markdown
        #

        1. [File001](file001.md)
        2. [File002](file002.md)
        3. [File003](file003.md)
        ...
    ```

12. Lets do something diffrent. Lets take two params. First is storage number and second is folder number.  
    I want to add so many folders as specified, to storage and 5 files to each. Rest stays same.

13. That is great but lest add yet another param, when 3 params are used we add files to storage number and folder number and add number of files, also we should update index accordingly.