# Folder Backup by Date

## Overview
This Python script automates copying a folder from a given source location to a destination directory. The copied folder is named after the current date, ensuring organized backups.

## Features
- Automatically organizes backups by date.
- Prevents overwriting existing folders.
- Simple user input for source and destination.

## Requirements
- Python 3.x

## Usage
1. Run the script.
2. Enter the source and destination folder paths.
3. The script will copy the folder into the destination with the current date as its name.

## Example
```
Enter the source location: C:\Users\User\Documents\MyFolder
Enter the destination location: D:\Backup
Folder copied to D:\Backup\2025-03-14
```

If a folder with the same date already exists, it will notify the user:
```
Folder already exists in: D:\Backup
```

