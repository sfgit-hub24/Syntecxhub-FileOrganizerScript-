# Syntecxhub-FileOrganizerScript
A Python automation script that organizes files into folders based on file extensions, developed as Week 2 internship task.

## Internship Task – Week 2
This project is a Python-based file organizer script developed as part of **Week 2 internship task**.  
The script scans a directory and automatically organizes files into subfolders based on file extensions.
---
## Features
- Organizes files by extension (PDFs, Images, Documents, etc.)
- Automatically creates folders if not present
- Handles name collisions safely
- Dry-run mode to preview changes
- Logging of moved files for tracking
---
## Technologies Used
- Python 3
- os module
- shutil module
- logging module
--- 
## How to Run
1. Clone the repository or download the ZIP:
```bash
git clone https://github.com/sfgit-hub24/python-file-organizer.git
```
2. Navigate to the Source Folder:
cd python-file-organizer/src
3. Run the Script:
python file_organizer.py
4. The script will organize files in the specified directory based on their extensions
---
## Features
- Organizes files into folders based on file extension
- Supports dry-run mode (no files are moved)
- Handles name collisions safely
- Logs all file movements
- Works on Windows and Linux
---
# Dry Run Mode
Dry-run mode shows what files *would* be moved without actually moving them.
```bash
python file_organizer.py --dry-run
```
# Logging
- All file movements are recorded in a log file
- Log file: `logs/file_organizer.log`
- Useful for:
  Tracking file operations
  Debugging issues
  Verifying successful execution
# Naming Handling Collision
- The script checks if a file with the same name already exists
- If a collision is detected, it automatically renames the file by appending a counter or timestamp
 - Example:
   report.pdf
   report_1.pdf
   report_2.pdf
- Useful for:
  No files are overwritten
  All files are safely preserved
  The file organization process runs smoothly without errors
---
## Technologies Used
- Python 3
- os module
- shutil module
- logging module
---
## Author
Safa Fatima
---
Internship Task 2 – Python Automation Script
---
