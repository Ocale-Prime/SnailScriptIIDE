#!/bin/bash
# Download SnailScriptIIDE from GitHub

# Exit if any command fails
set -e

echo "Cloning SnailScriptIIDE..."
git clone https://github.com/Ocale-Prime/SnailScriptIIDE.git

echo "Entering project folder..."
cd SnailScriptIIDE

# Optional: switch to a specific branch or tag
# git checkout <branch-or-tag>

echo "Listing files..."
ls -la

echo "Done! You can now open SnailScriptIIDE in your editor."

