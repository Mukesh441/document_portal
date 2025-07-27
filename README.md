# Project Setup guide
## Create Project Folder and Environment Setup

# Create a new project folder
mkdir <project_folder_name>

# Move into the project folder
cd <project_folder_name>

# Open the folder in VS Code
code .

# Initialize the UV
uv init 
# Create a new UV environment with Python 3.12
uv venv .venv

# Activate the environment (use full path to the environment)-- using Gitbash
source .venv/scripts/activate

# Install dependencies from requirements.txt
uv pip install -r requirements.txt