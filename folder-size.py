# python program to print a hierarchical list of folders and their size. start with the pwd and go deeper until done
# Usage: cd /Users/gy/anaconda3/envs/mlx && /Users/gy/dl/mlx-examples/python folder-size.py
import os

def get_size(start_path = '.'):
    """Returns the size of a directory and its subdirectories in bytes."""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

def print_dir_sizes(start_path = '.', level = 0):
    """Prints the sizes of directories starting from a given path."""
    # Get immediate subdirectories and files
    for entry in os.listdir(start_path):
        entry_path = os.path.join(start_path, entry)
        if os.path.isdir(entry_path):
            print("  " * level + f"{entry}/ ({get_size(entry_path)} bytes)")
            print_dir_sizes(entry_path, level + 1)
        else:
            print("  " * level + f"{entry} ({os.path.getsize(entry_path)} bytes)")

if __name__ == "__main__":
    print(f"Starting directory: {os.getcwd()}")
    print_dir_sizes('.')
