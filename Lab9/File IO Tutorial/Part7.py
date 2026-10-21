# Part 7: Error Handling with Files
# Add error handling to your previous file programs

from pathlib import Path

file_path = Path("input.txt")

try:
    with file_path.open("r", encoding="utf-8") as file:
        contents = file.read()
except FileNotFoundError:
    print(f"File not found: {file_path}")
except PermissionError:
    print(f"Permission denied: {file_path}")
except UnicodeDecodeError:
    print(f"Could not decode: {file_path}")
except OSError as error:
    print(f"File operation failed: {error}")
else:
    print("File read successfully.")
    print(contents)
