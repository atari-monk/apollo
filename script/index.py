import os
import sys

def get_storage_folder_path(storage_num):
    """Return the path to the specified storage folder."""
    return f'../data/storage{storage_num:03}'

def get_folder_path(storage_num, folder_num):
    """Return the path to the specified folder within a storage folder."""
    storage_folder_path = get_storage_folder_path(storage_num)
    return os.path.join(storage_folder_path, f'folder{folder_num:03}')

def create_index_file(folder_path):
    """Create or update an index.md file with links to all files in the specified folder."""
    if not os.path.exists(folder_path):
        print(f"Error: {folder_path} does not exist.")
        sys.exit(1)
    
    files = [f for f in os.listdir(folder_path) if f.startswith('file') and f.endswith('.md')]
    files.sort()
    
    index_file_path = os.path.join(folder_path, 'index.md')
    
    with open(index_file_path, 'w') as index_file:
        for i, file_name in enumerate(files, start=1):
            index_file.write(f"{i}. [{file_name}]({file_name})\n")
        
        # Add the "Home" link after the list of files
        index_file.write("\n[Home](../../../index.md)\n")
    
    print(f"Created/Updated index file: {index_file_path}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python index.py <storage_num> <folder_num>")
        sys.exit(1)

    try:
        storage_num = int(sys.argv[1])
        folder_num = int(sys.argv[2])

        if not (1 <= storage_num <= 99):
            raise ValueError("Storage number must be between 1 and 99.")

        if not (1 <= folder_num <= 99):
            raise ValueError("Folder number must be between 1 and 99.")

    except ValueError as ve:
        print(f"Invalid input: {ve}")
        sys.exit(1)

    folder_path = get_folder_path(storage_num, folder_num)
    create_index_file(folder_path)

if __name__ == "__main__":
    main()
