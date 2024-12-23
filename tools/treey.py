import os
import argparse

def print_tree(directory, exclude_dirs=None, prefix=""):
    """
    Recursively prints a directory tree.

    Args:
        directory (str): Path to the directory to start the tree.
        exclude_dirs (list): List of directory names to exclude.
        prefix (str): Prefix string for tree formatting.
    """
    if exclude_dirs is None:
        exclude_dirs = []

    try:
        entries = sorted(os.listdir(directory))
    except PermissionError:
        print(f"{prefix}[Permission Denied]")
        return

    entries = [e for e in entries if e not in exclude_dirs]

    for i, entry in enumerate(entries):
        entry_path = os.path.join(directory, entry)
        connector = "└── " if i == len(entries) - 1 else "├── "
        print(f"{prefix}{connector}{entry}")

        if os.path.isdir(entry_path):
            new_prefix = f"{prefix}{'    ' if i == len(entries) - 1 else '│   '}"
            print_tree(entry_path, exclude_dirs, new_prefix)

def main():
    parser = argparse.ArgumentParser(
        description="Display a directory tree with optional exclusions.",
        epilog="Example usage: python script.py /path/to/dir --exclude dir1 dir2",
    )
    parser.add_argument(
        "path", 
        type=str, 
        help="The root directory to display the tree. Provide the full path."
    )
    parser.add_argument(
        "--exclude",
        type=str,
        nargs="*",
        default=[],
        help="Space-separated list of directory names to exclude from the tree.",
    )

    args = parser.parse_args()
    
    root_directory = args.path
    exclude_directories = args.exclude

    print(f"Tree for {root_directory} (excluding: {', '.join(exclude_directories) if exclude_directories else 'None'})")
    print_tree(root_directory, exclude_directories)

if __name__ == "__main__":
    main()
