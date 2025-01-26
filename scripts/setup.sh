#!/bin/bash

# Exit on any error
set -e

# Determine the script's directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Create virtual environment
python3 -m venv "$PROJECT_ROOT/venv"

# Activate virtual environment
source "$PROJECT_ROOT/venv/bin/activate"

# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r "$PROJECT_ROOT/requirements.txt"

# Initialize database
python "$PROJECT_ROOT/src/database/connection.py"

echo "Project setup complete! Activate the virtual environment with 'source venv/bin/activate'" 