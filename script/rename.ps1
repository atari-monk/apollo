$FolderPath = "C:\atari-monk\code\apollo\content"  # Set your folder path here
$OldFileName = "Index.md"
$NewFileName = "temp.md"

# Check if the folder exists
if (-Not (Test-Path -Path $FolderPath)) {
    Write-Host "The specified folder does not exist."
    exit
}

# Get all index.md files in the specified folder and subfolders
$files = Get-ChildItem -Path $FolderPath -Recurse -Filter $OldFileName

foreach ($file in $files) {
    $newFilePath = Join-Path -Path $file.DirectoryName -ChildPath $NewFileName

    # Rename the file
    Rename-Item -Path $file.FullName -NewName $newFilePath

    Write-Host "Renamed '$($file.FullName)' to '$newFilePath'"
}

Write-Host "All files renamed successfully."
