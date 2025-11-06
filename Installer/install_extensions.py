import json
import subprocess
import sys
import shutil
import argparse
import os

# -------------------------------
# Parse command-line arguments
# -------------------------------
parser = argparse.ArgumentParser(
    description="Install VS Code or Cursor IDE extensions from JSON")
parser.add_argument(
    "target_ide",
    choices=["vscode", "cursor"],
    help="Target IDE to install extensions for"
)
args = parser.parse_args()
target_ide = args.target_ide

# -------------------------------
# Check if VS Code CLI is installed
# -------------------------------
install_cmd = "code"  # VS Code CLI
if shutil.which(install_cmd) is None:
    print(
        "VS Code CLI 'code' not found.\n"
        "Please open VS Code, press Cmd+Shift+P and run:\n"
        "'Shell Command: Install 'code' command in PATH'"
    )
    sys.exit(1)

# -------------------------------
# Load JSON
# -------------------------------
JSON_FILE = "extensions.json"

try:
    with open(JSON_FILE, "r") as f:
        config = json.load(f)
except FileNotFoundError:
    print(f"File {JSON_FILE} not found.")
    sys.exit(1)
except json.JSONDecodeError as e:
    print(f"JSON decode error: {e}")
    sys.exit(1)

extensions = config.get("extensions", {}).get(target_ide)
if not extensions:
    print(f"No extensions found for target IDE: {target_ide}")
    sys.exit(1)

# -------------------------------
# Get already installed extensions
# -------------------------------
try:
    result = subprocess.run(
        [install_cmd, "--list-extensions"],
        capture_output=True,
        text=True,
        check=True
    )
    installed_extensions = set(result.stdout.splitlines())
except subprocess.CalledProcessError:
    print("Failed to get installed extensions.")
    sys.exit(1)

# -------------------------------
# Install missing extensions
# -------------------------------
for ext in extensions:
    if ext in installed_extensions:
        print(f"Skipped (already installed): {ext}")
        continue

    print(f"Installing {ext}...")
    try:
        subprocess.run(
            [install_cmd, "--install-extension", ext],
            check=True,
            stdout=subprocess.DEVNULL,  # suppress CLI output
            stderr=subprocess.DEVNULL
        )
    except subprocess.CalledProcessError:
        print(f"Failed to install {ext}")


# Source file in the same folder as the script
source_file = os.path.join(os.path.dirname(__file__), "settings.json")

# Destination folder: one level up from script folder, then .vscode
parent_folder = os.path.dirname(os.path.dirname(__file__))  # go one level up
destination_folder = os.path.join(parent_folder, ".vscode")
destination_file = os.path.join(destination_folder, "settings.json")

# Copy the file
shutil.copy2(source_file, destination_file)

print(f"Copied {source_file} to {destination_file}")
