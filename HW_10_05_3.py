import threading
import shutil
import os

def copy_directory_contents(source_dir, dest_dir):
    try:
        shutil.copytree(source_dir, dest_dir)
        print(f"Directory contents copied from '{source_dir}' to '{dest_dir}' successfully.")
    except Exception as e:
        print(f"Error copying directory contents: {e}")

def main():
    source_dir = input("Enter the path to the existing directory: ")
    dest_dir = input("Enter the path to the new directory: ")

    t = threading.Thread(target=copy_directory_contents, args=(source_dir, dest_dir))
    t.start()
    t.join()

if __name__ == "__main__":
    main()