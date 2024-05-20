#!/bin/bash

# Check if commit message was supplied
if [ $# -eq 0 ]
  then
    echo "No commit message supplied"
    exit 1
fi

# Add all changes
git add .

# Commit with supplied message
git commit -m "$1"

# Push to main branch
git push origin main