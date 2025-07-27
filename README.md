# Project Setup guide
## Create Project Folder and Environment Setup

# Create a new project folder
mkdir <project_folder_name>

# Move into the project folder
cd <project_folder_name>

# Open the folder in VS Code
code .

# Create a new UV environment with Python 3.12
UV venv .venv

# Activate the environment (use full path to the environment)-- using Gitbash
source .venv/scripts/activate

# Install dependencies from requirements.txt
pip install -r requirements.txt