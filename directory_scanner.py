import os
import sys 

def get_subdirectory_names(main_directory):
    try:
        
        subdirectories = [
            name for name in os.listdir(main_directory)
            if os.path.isdir(os.path.join(main_directory, name))
        ]
        return subdirectories
    except FileNotFoundError:
        print("Error: The specified directory does not exist.")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main_dir_path = sys.argv[1]
    else:
        main_dir_path = os.getcwd()
    folders = get_subdirectory_names(main_dir_path)
    print("Subdirectories found:")
    for folder in folders:
        print("-", folder)
