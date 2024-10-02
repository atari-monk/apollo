# Tutorial Notes

Optional commands used for info, upgrade and stuff

python.exe -m pip install --upgrade pip

python --version

This runs python interpreter as cli ?

python

to exit

exit()

In chatgpt:

If hitting enter sends the message instead of creating a new line,  
you can try using **Shift + Enter** (or **Shift + Return**) to insert a line break without sending the message.  
This way, you can format your text over multiple lines before sending it. Let me know if you need more help!

---
Project flow:

mkdir farm-todo
mkdir frontend
mkdir backend

cd backend

python -m venv venv

---
It looks like you're working through setting up a Python virtual environment for your project on Windows. Here's a quick guide to help you with the process:

### Steps to Activate a Virtual Environment on Windows

1. **Navigate to your project directory:**
   ```bash
   cd C:\atari-monk\code\farm-todo\backend
   ```

2. **Create the virtual environment:**
   You already created it with:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   On Windows, you can activate it by running:
   ```bash
   .\venv\Scripts\activate
   ```

4. **Verify the virtual environment is active:**
   Once activated, your command prompt will change, showing something like:
   ```bash
   (venv) C:\atari-monk\code\farm-todo\backend>
   ```

5. **Deactivate the virtual environment:**
   When you're done, you can deactivate it with:
   ```bash
   deactivate
   ```

### Notes:
- The script you are seeing is part of how the `activate` and `deactivate` commands manage the environment. On Windows, you typically just need to run the `activate` script from the `Scripts` folder to get the virtual environment up and running.

Let me know if you need further help!
---

Create files 

Dockerfile
pyproject.toml

Install ((venv) PS C:\atari-monk\code\farm-todo\backend>)

pip install "fastapi[all]" motor beanie aiostream 

In tutorial it was 

pip install "motor[srv]"

but newest vesrsion dosent have this extra, ignored for now.

Create file with command

pip freeze > requirements.txt

This file is same as project.json in typescript, when in other machine just use this list with pip install to get dependencies.

---

Open Dockerfile and paste

```Dockerfile
FROM python:3

WORKDIR /usr/src/app
COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

EXPOSE 3001

CMD ["python", "./src/server.py"]
```

---

.gitignore for python

```plaintext
# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd
*.egg-info/
dist/
build/
*.egg
*.whl
*.env
*.venv
.venv/
ENV/
env/
env.bak/
venv/
*.sqlite3
*.log

# Jupyter Notebook
.ipynb_checkpoints/

# Pytest
.cache
*.cover
*.coverage
coverage.xml
*.hypothesis/

# IDE and editor specific
.vscode/
.idea/
*.sublime-workspace
*.sublime-project

# OS specific files
.DS_Store
Thumbs.db

# Backup files
*~
*.bak
```
---

Added api files.
