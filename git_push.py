import argparse
import subprocess

# Create the parser
parser = argparse.ArgumentParser(description="Add all changes, commit, and push to main.")

# Add the arguments
parser.add_argument('message', type=str, help='The commit message')

# Parse the arguments
args = parser.parse_args()

# Run the Git commands
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", args.message])
subprocess.run(["git", "push", "origin", "main"])