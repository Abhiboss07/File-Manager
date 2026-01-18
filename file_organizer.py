import os
import shutil
from pathlib import Path

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"],
}

def organize_folder(folder_path):
    folder = Path(folder_path)

    if not folder.exists():
        print("❌ Folder does not exist.")
        return

    for file in folder.iterdir():
        if file.is_file():
            moved = False
            for category, extensions in FILE_TYPES.items():
                if file.suffix.lower() in extensions:
                    target_dir = folder / category
                    target_dir.mkdir(exist_ok=True)
                    shutil.move(str(file), target_dir / file.name)
                    print(f"✅ Moved {file.name} -> {category}")
                    moved = True
                    break
            if not moved:
                other_dir = folder / "Others"
                other_dir.mkdir(exist_ok=True)
                shutil.move(str(file), other_dir / file.name)
                print(f"📁 Moved {file.name} -> Others")

if __name__ == "__main__":
    print("📂 Python CLI File Organizer")
    path = input("Enter folder path to organize: ").strip()
    organize_folder(path)
