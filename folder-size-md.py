# python program to print a hierarchical list of folders and their size. start with the pwd and go deeper until done
# Usage: cd /Users/gy/anaconda3/envs/mlx && python /Users/gy/dl/mlx-examples/folder-size-md.py
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

def print_dir_sizes(start_path = '.', level = 0, file_handle = None):
    """Prints the sizes of directories starting from a given path to a file."""
    for entry in os.listdir(start_path):
        entry_path = os.path.join(start_path, entry)
        if os.path.isdir(entry_path):
            size = get_size(entry_path)
            if size > (100 * 1024 * 1024):  # Greater than 100 MB
                line = f"{'  ' * level}**{entry}/ ({size} bytes)**\n"
            else:
                line = f"{'  ' * level}{entry}/ ({size} bytes)\n"
            file_handle.write(line)
            print_dir_sizes(entry_path, level + 1, file_handle)
        else:
            size = os.path.getsize(entry_path)
            line = f"{'  ' * level}{entry} ({size} bytes)\n"
            file_handle.write(line)

if __name__ == "__main__":
    with open('file-sizes.md', 'w') as file_out:
        file_out.write(f"Starting directory: {os.getcwd()}\n")
        print_dir_sizes('.', file_handle=file_out)
