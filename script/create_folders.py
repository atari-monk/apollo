import os
import argparse

def create_directory(path, description):
    """Creates a directory if it doesn't exist and logs the action."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created {description} directory: {path}")
    else:
        print(f"{description} directory already exists: {path}")

    # After creating the directory, create an index.md file
    create_index_file(path)

def create_index_file(folder_path):
    """Creates an index.md file with specific content in the given folder."""
    index_file_path = os.path.join(folder_path, "index.md")
    if not os.path.exists(index_file_path):
        with open(index_file_path, 'w') as file:
            file.write("# ")
        print(f"Created index.md in: {folder_path}")
    else:
        print(f"index.md already exists in: {folder_path}")

def create_storage_directories(root_dir, storage_number):
    # Define the storage directory name
    storage_dir = f"storage{storage_number}"
    full_storage_path = os.path.join(root_dir, storage_dir)
    
    # Create the root and storage directories
    create_directory(root_dir, "Root")
    create_directory(full_storage_path, "Storage")
    
    # Create 100 folders inside the storage directory
    for i in range(100):
        folder_name = f"folder{i:03}"  # Zero-padded folder names, e.g., folder000, folder001, etc.
        folder_path = os.path.join(full_storage_path, folder_name)
        create_directory(folder_path, f"Folder {folder_name}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Create storage directories with subfolders.")
    parser.add_argument('storage_number', type=int, help="The number of the storage directory to create")
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Define the root directory
    root_directory = "../data"
    
    # Create the directories based on the provided storage number
    create_storage_directories(root_directory, args.storage_number)

if __name__ == "__main__":
    main()
