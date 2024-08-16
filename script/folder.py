import os
import sys

def create_root_folder():
    """Create the root folder '../data' if it does not exist."""
    root_folder = '../data'
    if not os.path.exists(root_folder):
        os.makedirs(root_folder)
        print(f"Created root folder: {root_folder}")

def create_storage_folder(storage_num):
    """Create a storage folder named 'storage00n' where n is the storage number."""
    root_folder = '../data'
    storage_folder_name = f'storage{storage_num:03}'
    storage_folder_path = os.path.join(root_folder, storage_folder_name)
    
    if not os.path.exists(storage_folder_path):
        os.makedirs(storage_folder_path)
        print(f"Created storage folder: {storage_folder_path}")
    
    return storage_folder_path

def create_folders(storage_folder_path, num_folders):
    """Create the specified number of folders in the given storage folder."""
    existing_folders = [d for d in os.listdir(storage_folder_path) if os.path.isdir(os.path.join(storage_folder_path, d))]
    
    if existing_folders:
        existing_folders.sort()
        last_folder = existing_folders[-1]
        last_index = int(last_folder[6:])  # Extract the number part of folder name 'folder00n'
    else:
        last_index = 0
    
    new_folders = []
    for i in range(last_index + 1, last_index + 1 + num_folders):
        folder_name = f'folder{i:03}'
        folder_path = os.path.join(storage_folder_path, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")
            new_folders.append(folder_name)
    
    return new_folders

def main():
    if len(sys.argv) != 3:
        print("Usage: python folders.py <storage_num> <num_folders>")
        sys.exit(1)
    
    try:
        storage_num = int(sys.argv[1])
        num_folders = int(sys.argv[2])
        
        if not (1 <= storage_num <= 99):
            raise ValueError("Storage number must be between 1 and 99.")
        
        if num_folders <= 0:
            raise ValueError("Number of folders must be positive.")
        
    except ValueError as ve:
        print(f"Invalid input: {ve}")
        sys.exit(1)
    
    create_root_folder()
    storage_folder_path = create_storage_folder(storage_num)
    create_folders(storage_folder_path, num_folders)

if __name__ == "__main__":
    main()
