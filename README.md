# Python CLI File Organizer

## Problem Statement
My system's Downloads folder often becomes cluttered with different types of files such as images, PDFs, videos, and archives.
Finding files becomes difficult and time-consuming.

## Solution
This command-line utility automatically organizes files into folders based on their file type.

## Features
- Organizes files into Images, Documents, Videos, Audio, Archives, and Others
- Uses only Python standard libraries
- Simple and user-friendly CLI interface

## How to Run
1. Make sure Python 3 is installed
2. Open terminal or command prompt
3. Run:
   python file_organizer.py
4. Enter the path of the folder you want to organize

## Design Decisions
- Used `pathlib` for clean path handling
- Used `shutil` for safe file movement
- Categorized files by extensions for simplicity
- Gracefully handles missing folders

## Sample Output
The terminal will show which files are moved into which folders.

## Author
Internship Assignment Submission
