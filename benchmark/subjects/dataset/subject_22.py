from typing import List
import os

def find_python_files(directory_path: str) -> List[str]:
    python_files = []

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))

    return python_files