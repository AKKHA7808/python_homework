#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Create migration files (if any models are added later)
python manage.py makemigrations

# Apply migrations
python manage.py migrate