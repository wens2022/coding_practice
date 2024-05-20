import os
import argparse

def create_folders(chapter, topics):

    # Specify the directory you want to create the new folders
    parent_dir = "." # Current directory

    # Create the chapter folder
    chapter_path = os.path.join(parent_dir, chapter)
    os.makedirs(chapter_path, exist_ok=True)
    with open(os.path.join(chapter_path, "README.md"), 'w') as f:
            f.write(f"# {chapter}\nThis is the README for {chapter}")

    # Create the topic subfolders
    for topic in topics:
        topic_path = os.path.join(chapter_path, topic)
        os.makedirs(topic_path, exist_ok=True)

        # Create README.md in the new folder
        with open(os.path.join(topic_path, "README.md"), 'w') as f:
            f.write(f"# {topic}\nThis is the README for {topic} in {chapter}")

if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description="Create a chapter folder with topic subfolders.")

    # Add the arguments
    parser.add_argument('chapter', type=str, help='The name of the chapter')
    parser.add_argument('topics', type=str, nargs='+', help='The list of topics')

    # Parse the arguments
    args = parser.parse_args()
    
    create_folders(args.chapter, args.topics)
