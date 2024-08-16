import os
import argparse

def create_directory(path, description):
    """Creates a directory if it doesn't exist and logs the action."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created {description} directory: {path}")
    else:
        print(f"{description} directory already exists: {path}")

def create_file(path, content):
    """Creates a file with the specified content if it doesn't exist."""
    if not os.path.exists(path):
        with open(path, 'w') as file:
            file.write(content)
        print(f"Created file: {path}")
    else:
        print(f"File already exists: {path}")

def update_index_file(folder_path):
    """Updates the index.md file with links to all files created in the folder."""
    index_file_path = os.path.join(folder_path, "index.md")
    
    # Prepare the content to be added to index.md
    content = "#\n\n"
    file_list = sorted([f for f in os.listdir(folder_path) if f.startswith('file') and f.endswith('.md')])
    for file_name in file_list:
        content += f"1. [{file_name}](file/{file_name})\n"
    
    # Write the content to index.md
    create_file(index_file_path, content)

def create_storage_directories(root_dir, storage_number):
    # Define the storage directory name
    storage_dir = f"storage{storage_number}"
    full_storage_path = os.path.join(root_dir, storage_dir)
    
    # Create the root and storage directories
    create_directory(root_dir, "Root")
    create_directory(full_storage_path, "Storage")
    
    # Create 99 folders inside the storage directory, starting from folder001 to folder099
    for i in range(1, 100):  # Loop from 1 to 99
        folder_name = f"folder{i:03}"  # Zero-padded folder names, e.g., folder001, folder002, etc.
        folder_path = os.path.join(full_storage_path, folder_name)
        create_directory(folder_path, f"Folder {folder_name}")
        
        # Determine the starting number for new files
        existing_files = [f for f in os.listdir(folder_path) if f.startswith('file') and f.endswith('.md')]
        start_file_number = len(existing_files) + 1
        
        # Create 10 new files in each folder starting from the next available number
        for j in range(start_file_number, start_file_number + 10):
            file_name = f"file{j:03}.md"
            file_path = os.path.join(folder_path, file_name)
            create_file(file_path, "")
        
        # Update index.md to reflect all files
        update_index_file(folder_path)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Create storage directories with subfolders and files.")
    parser.add_argument('storage_number', type=int, help="The number of the storage directory to create")
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Define the root directory
    root_directory = "../data"
    
    # Create the directories based on the provided storage number
    create_storage_directories(root_directory, args.storage_number)

if __name__ == "__main__":
    main()