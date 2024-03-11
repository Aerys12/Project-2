#!/bin/bash
# Create and activate a virtual environment
python3.9 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python3.9 manage.py migrate