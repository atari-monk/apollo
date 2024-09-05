# Script prompting example

## From this path, C:\atari-monk\code\ts-engine-nx\dist\packages\client, copy all files and folders, exept those from exclusion lists, and move them to path C:\atari-monk\code\football_slideshow, deleting its content fisrst but not excluded from this. Also it would be nice to define a json config for this with all this obj data in array so it can be used to many paths and list of files, us py, can u do it ?

Yes, I can help you with that. To achieve this, you can use a Python script. Here’s how you can structure the script to copy files and folders from one path to another, while excluding certain files and folders, and using a JSON configuration.

### Step 1: Define the JSON Configuration

Create a `config.json` file with the following structure:

```json
{
  "source_path": "C:\\atari-monk\\code\\ts-engine-nx\\dist\\packages\\client",
  "destination_path": "C:\\atari-monk\\code\\football_slideshow",
  "exclude_list": ["exclude_file1.txt", "exclude_folder1"]
}
```

### Step 2: Python Script

You can use the following Python script to copy files and folders according to the configuration:

```python
import os
import shutil
import json

def load_config(config_file):
    with open(config_file, 'r') as f:
        return json.load(f)

def clear_destination_folder(destination_path, exclude_list):
    for item in os.listdir(destination_path):
        item_path = os.path.join(destination_path, item)
        if item not in exclude_list:
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)

def copy_files(source_path, destination_path, exclude_list):
    for root, dirs, files in os.walk(source_path):
        for name in dirs:
            if name not in exclude_list:
                src_dir = os.path.join(root, name)
                dst_dir = os.path.join(destination_path, os.path.relpath(src_dir, source_path))
                if not os.path.exists(dst_dir):
                    os.makedirs(dst_dir)

        for name in files:
            if name not in exclude_list:
                src_file = os.path.join(root, name)
                dst_file = os.path.join(destination_path, os.path.relpath(src_file, source_path))
                shutil.copy2(src_file, dst_file)

def main():
    config = load_config('config.json')

    source_path = config['source_path']
    destination_path = config['destination_path']
    exclude_list = config['exclude_list']

    # Clear the destination folder
    clear_destination_folder(destination_path, exclude_list)

    # Copy files and folders
    copy_files(source_path, destination_path, exclude_list)

if __name__ == "__main__":
    main()
```

### Instructions

1. Save the JSON configuration as `config.json`.
2. Save the Python script in the same directory as `config.json`.
3. Run the Python script.

### Notes

- Make sure the paths in `config.json` are correctly formatted for your operating system.
- This script does not handle complex exclusion patterns (e.g., partial matches) or nested exclusions. You can extend it if needed.

Let me know if you need any adjustments or further assistance!

## Add [] and another example to json and modiffy script.

Certainly! I'll update the JSON configuration to support multiple paths and exclusions, and modify the Python script accordingly.

### Updated JSON Configuration

Here's an example of the updated `config.json`:

```json
{
  "tasks": [
    {
      "source_path": "C:\\atari-monk\\code\\ts-engine-nx\\dist\\packages\\client",
      "destination_path": "C:\\atari-monk\\code\\football_slideshow",
      "exclude_list": ["exclude_file1.txt", "exclude_folder1"]
    },
    {
      "source_path": "C:\\another-source-path",
      "destination_path": "C:\\another-destination-path",
      "exclude_list": ["excluded_file.txt", "excluded_folder"]
    }
  ]
}
```

### Updated Python Script

Here's the modified Python script to handle multiple tasks:

```python
import os
import shutil
import json

def load_config(config_file):
    with open(config_file, 'r') as f:
        return json.load(f)

def clear_destination_folder(destination_path, exclude_list):
    for item in os.listdir(destination_path):
        item_path = os.path.join(destination_path, item)
        if item not in exclude_list:
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)

def copy_files(source_path, destination_path, exclude_list):
    for root, dirs, files in os.walk(source_path):
        for name in dirs:
            if name not in exclude_list:
                src_dir = os.path.join(root, name)
                dst_dir = os.path.join(destination_path, os.path.relpath(src_dir, source_path))
                if not os.path.exists(dst_dir):
                    os.makedirs(dst_dir)

        for name in files:
            if name not in exclude_list:
                src_file = os.path.join(root, name)
                dst_file = os.path.join(destination_path, os.path.relpath(src_file, source_path))
                shutil.copy2(src_file, dst_file)

def process_task(task):
    source_path = task['source_path']
    destination_path = task['destination_path']
    exclude_list = task['exclude_list']

    # Clear the destination folder
    if os.path.exists(destination_path):
        clear_destination_folder(destination_path, exclude_list)
    else:
        os.makedirs(destination_path)

    # Copy files and folders
    copy_files(source_path, destination_path, exclude_list)

def main():
    config = load_config('config.json')

    for task in config['tasks']:
        process_task(task)

if __name__ == "__main__":
    main()
```

### Instructions

1. Save the updated JSON configuration as `config.json`.
2. Save the modified Python script in the same directory as `config.json`.
3. Run the Python script.

This script now handles multiple tasks defined in the `config.json` file, where each task specifies a source path, destination path, and an exclusion list. Each task is processed sequentially.

## But i need cpy_exclude_list and delete_exclude list pls.

Got it! To address your requirements, we’ll need to handle two separate exclusion lists:

1. **`copy_exclude_list`**: Files and folders to exclude from copying.
2. **`delete_exclude_list`**: Files and folders to exclude from deletion.

### Updated JSON Configuration

Here’s an updated `config.json` with separate exclusion lists for copying and deletion:

```json
{
  "tasks": [
    {
      "source_path": "C:\\atari-monk\\code\\ts-engine-nx\\dist\\packages\\client",
      "destination_path": "C:\\atari-monk\\code\\football_slideshow",
      "copy_exclude_list": ["exclude_file1.txt", "exclude_folder1"],
      "delete_exclude_list": ["keep_file.txt", "keep_folder"]
    },
    {
      "source_path": "C:\\another-source-path",
      "destination_path": "C:\\another-destination-path",
      "copy_exclude_list": ["excluded_file.txt", "excluded_folder"],
      "delete_exclude_list": ["another_keep_file.txt", "another_keep_folder"]
    }
  ]
}
```

### Updated Python Script

Here’s the updated script to handle both exclusion lists:

```python
import os
import shutil
import json

def load_config(config_file):
    with open(config_file, 'r') as f:
        return json.load(f)

def clear_destination_folder(destination_path, delete_exclude_list):
    for item in os.listdir(destination_path):
        item_path = os.path.join(destination_path, item)
        if item not in delete_exclude_list:
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)

def copy_files(source_path, destination_path, copy_exclude_list):
    for root, dirs, files in os.walk(source_path):
        # Exclude directories during copying
        dirs[:] = [d for d in dirs if d not in copy_exclude_list]

        for name in dirs:
            src_dir = os.path.join(root, name)
            dst_dir = os.path.join(destination_path, os.path.relpath(src_dir, source_path))
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)

        for name in files:
            if name not in copy_exclude_list:
                src_file = os.path.join(root, name)
                dst_file = os.path.join(destination_path, os.path.relpath(src_file, source_path))
                shutil.copy2(src_file, dst_file)

def process_task(task):
    source_path = task['source_path']
    destination_path = task['destination_path']
    copy_exclude_list = task['copy_exclude_list']
    delete_exclude_list = task['delete_exclude_list']

    # Ensure destination folder exists
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    # Clear the destination folder
    clear_destination_folder(destination_path, delete_exclude_list)

    # Copy files and folders
    copy_files(source_path, destination_path, copy_exclude_list)

def main():
    config = load_config('config.json')

    for task in config['tasks']:
        process_task(task)

if __name__ == "__main__":
    main()
```

### Explanation

- **`clear_destination_folder`**: Deletes files and folders in the destination directory, excluding those specified in `delete_exclude_list`.
- **`copy_files`**: Copies files and folders from the source to the destination, excluding those specified in `copy_exclude_list`.
- **`process_task`**: Handles each task by first clearing the destination folder (excluding files and folders in `delete_exclude_list`), then copying files and folders (excluding those in `copy_exclude_list`).

### Instructions

1. Save the updated JSON configuration as `config.json`.
2. Save the modified Python script in the same directory as `config.json`.
3. Run the Python script.

Let me know if you need further adjustments!

## Also pls add a flag for if task is active to be done or not.

To incorporate a flag for each task indicating whether it is active, you can add an `active` field to the JSON configuration and modify the Python script to check this flag before processing each task.

### Updated JSON Configuration

Here’s the updated `config.json` with an `active` flag:

```json
{
  "tasks": [
    {
      "source_path": "C:\\atari-monk\\code\\ts-engine-nx\\dist\\packages\\client",
      "destination_path": "C:\\atari-monk\\code\\football_slideshow",
      "copy_exclude_list": ["exclude_file1.txt", "exclude_folder1"],
      "delete_exclude_list": ["keep_file.txt", "keep_folder"],
      "active": true
    },
    {
      "source_path": "C:\\another-source-path",
      "destination_path": "C:\\another-destination-path",
      "copy_exclude_list": ["excluded_file.txt", "excluded_folder"],
      "delete_exclude_list": ["another_keep_file.txt", "another_keep_folder"],
      "active": false
    }
  ]
}
```

### Updated Python Script

Here’s the updated script to handle the `active` flag:

```python
import os
import shutil
import json

def load_config(config_file):
    with open(config_file, 'r') as f:
        return json.load(f)

def clear_destination_folder(destination_path, delete_exclude_list):
    for item in os.listdir(destination_path):
        item_path = os.path.join(destination_path, item)
        if item not in delete_exclude_list:
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)

def copy_files(source_path, destination_path, copy_exclude_list):
    for root, dirs, files in os.walk(source_path):
        # Exclude directories during copying
        dirs[:] = [d for d in dirs if d not in copy_exclude_list]

        for name in dirs:
            src_dir = os.path.join(root, name)
            dst_dir = os.path.join(destination_path, os.path.relpath(src_dir, source_path))
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)

        for name in files:
            if name not in copy_exclude_list:
                src_file = os.path.join(root, name)
                dst_file = os.path.join(destination_path, os.path.relpath(src_file, source_path))
                shutil.copy2(src_file, dst_file)

def process_task(task):
    if not task.get('active', True):
        print(f"Skipping inactive task: {task['source_path']}")
        return

    source_path = task['source_path']
    destination_path = task['destination_path']
    copy_exclude_list = task['copy_exclude_list']
    delete_exclude_list = task['delete_exclude_list']

    # Ensure destination folder exists
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    # Clear the destination folder
    clear_destination_folder(destination_path, delete_exclude_list)

    # Copy files and folders
    copy_files(source_path, destination_path, copy_exclude_list)

def main():
    config = load_config('config.json')

    for task in config['tasks']:
        process_task(task)

if __name__ == "__main__":
    main()
```

### Explanation

- **`process_task`**: Checks the `active` flag. If the task is not active (`active` is `false` or missing), it skips the task and prints a message.

### Instructions

1. Save the updated JSON configuration as `config.json`.
2. Save the modified Python script in the same directory as `config.json`.
3. Run the Python script.

This setup allows you to control which tasks are executed by toggling the `active` flag in your JSON configuration. Let me know if there’s anything else you need!
