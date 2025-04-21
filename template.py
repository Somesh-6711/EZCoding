import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "EZCoding"

# List of all required files and folders
list_of_files = [
    # Backend structure
    f"{project_name}/backend/app/__init__.py",
    f"{project_name}/backend/app/api/__init__.py",
    f"{project_name}/backend/app/api/routes.py",
    f"{project_name}/backend/app/core/__init__.py",
    f"{project_name}/backend/app/core/language_detection.py",
    f"{project_name}/backend/app/models/__init__.py",
    f"{project_name}/backend/app/models/code_explainer.py",
    f"{project_name}/backend/app/config/__init__.py",
    f"{project_name}/backend/app/config/settings.py",
    f"{project_name}/backend/app/main.py",
    f"{project_name}/backend/requirements.txt",
    f"{project_name}/backend/Dockerfile",
    f"{project_name}/backend/README.md",

    # Frontend structure
    f"{project_name}/frontend/public/.gitkeep",
    f"{project_name}/frontend/src/components/.gitkeep",
    f"{project_name}/frontend/src/pages/.gitkeep",
    f"{project_name}/frontend/src/services/.gitkeep",
    f"{project_name}/frontend/src/utils/.gitkeep",
    f"{project_name}/frontend/src/App.js",
    f"{project_name}/frontend/package.json",
    f"{project_name}/frontend/.env",
    f"{project_name}/frontend/README.md",

    # Documentation folder
    f"{project_name}/docs/.gitkeep",

    # Main project readme and license
    f"{project_name}/README.md",
    f"{project_name}/LICENSE",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")
