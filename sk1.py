import os
import subprocess
import shutil
import sys

def install_python():
    try:
        # Install Python in Termux
        subprocess.run(["pkg", "install", "python", "-y"])
    except subprocess.CalledProcessError as e:
        print(f"Error installing Python: {e}")
        sys.exit(1)

def install_git():
    try:
        # Install Git in Termux
        subprocess.run(["pkg", "install", "git", "-y"])
    except subprocess.CalledProcessError as e:
        print(f"Error installing Git: {e}")
        sys.exit(1)

def clone_repo(repo_url, destination_folder):
    if os.path.exists(destination_folder):
        print(f"Repository already exists in {destination_folder}. Skipping cloning.")
        return

    try:
        subprocess.run(["git", "clone", repo_url, destination_folder], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository: {e}")
        sys.exit(1)

def install_requirements(requirements_file):
    try:
        subprocess.run(["pip", "install", "-r", requirements_file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error installing requirements: {e}")
        sys.exit(1)

def main():
    # Install Python if not already installed
    if shutil.which("python") is None:
        install_python()

    # Install Git if not already installed
    if shutil.which("git") is None:
        install_git()

    # Define the GitHub repository URL
    github_repo_url = "https://github.com/hoaan1995/ZxCDDoS.git"

    # Define the destination folder to clone the repository
    destination_folder = "ZxCDDoS"

    # Clone the GitHub repository or use an existing clone
    clone_repo(github_repo_url, destination_folder)

    # Change to the cloned repository directory
    os.chdir(destination_folder)

    # Check if requirements.txt exists
    requirements_file = "requirements.txt"
    if not os.path.isfile(requirements_file):
        print(f"Error: The file '{requirements_file}' does not exist in the repository.")
        sys.exit(1)

    # Install requirements.txt and any other requirements
    install_requirements(requirements_file)

    # Run c2.py
    c2_script = "c2.py"
    if not os.path.isfile(c2_script):
        print(f"Error: The file '{c2_script}' does not exist in the repository.")
        sys.exit(1)

    try:
        subprocess.run(["python", c2_script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing c2.py: {e}")

if __name__ == "__main__":
    main()
