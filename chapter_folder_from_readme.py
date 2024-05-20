import os
import argparse

def create_folders_from_readme(readme_path):
    with open(readme_path, 'r') as f:
        lines = f.readlines()

    parent_dir = os.path.dirname(readme_path)
    toc_start = False

    for line in lines:
        if "Table of Contents" in line:  # Start of TOC
            toc_line_number = lines.index(line) + 1
            toc_start = True
            continue
        if toc_start:
            if line.strip() == '':
                break  # End of TOC
            else:
                # Assuming each bullet point is a folder to be created
                folder_number = str(lines.index(line) - toc_line_number + 1).zfill(2)
                folder = f"{folder_number}_{line.strip().replace('-', '').strip()}"
                folder_path = os.path.join(parent_dir, folder)
                os.makedirs(folder_path, exist_ok=True)
                with open(os.path.join(folder_path, "README.md"), 'w') as f:
                    f.write(f"# {folder}\nThis is the README for {folder}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create folders from README.md TOC.")
    parser.add_argument('--readme', '-r', type=str, help='The path of the README.md file')
    args = parser.parse_args()
    create_folders_from_readme(args.readme)