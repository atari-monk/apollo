import os
import sys

def get_storage_folder_path(storage_num):
    """Return the path to the specified storage folder."""
    return f'../data/storage{storage_num:03}'

def get_folder_path(storage_num, folder_num):
    """Return the path to the specified folder within a storage folder."""
    storage_folder_path = get_storage_folder_path(storage_num)
    return os.path.join(storage_folder_path, f'folder{folder_num:03}')

def create_files(folder_path, num_files):
    """Create the specified number of markdown files in the given folder."""
    if not os.path.exists(folder_path):
        print(f"Error: {folder_path} does not exist.")
        sys.exit(1)

    existing_files = [f for f in os.listdir(folder_path) if f.startswith('file') and f.endswith('.md')]
    existing_files.sort()

    if existing_files:
        last_file = existing_files[-1]
        last_index = int(last_file[4:7])  # Extract the number part of file name 'file00n.md'
    else:
        last_index = 0

    if last_index + num_files > 999:
        print("Error: Cannot create more than 999 files in a folder.")
        sys.exit(1)

    new_files = []
    for i in range(last_index + 1, last_index + 1 + num_files):
        file_name = f'file{i:03}.md'
        file_path = os.path.join(folder_path, file_name)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                file.write(f"# {file_name}\n\nThis is {file_name}.\n\n")
            print(f"Created file: {file_path}")
            new_files.append(file_name)

    return new_files

def main():
    if len(sys.argv) != 4:
        print("Usage: python file.py <storage_num> <folder_num> <num_files>")
        sys.exit(1)

    try:
        storage_num = int(sys.argv[1])
        folder_num = int(sys.argv[2])
        num_files = int(sys.argv[3])

        if not (1 <= storage_num <= 99):
            raise ValueError("Storage number must be between 1 and 99.")

        if not (1 <= folder_num <= 99):
            raise ValueError("Folder number must be between 1 and 99.")

        if not (1 <= num_files <= 999):
            raise ValueError("File count must be between 1 and 999.")

    except ValueError as ve:
        print(f"Invalid input: {ve}")
        sys.exit(1)

    folder_path = get_folder_path(storage_num, folder_num)
    create_files(folder_path, num_files)

if __name__ == "__main__":
    main()
