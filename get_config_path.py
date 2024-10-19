import os

def get_full_path(relative_path):
    # Get the absolute path from the relative path
    full_path = os.path.abspath(relative_path)
    return full_path

if __name__ == "__main__":
    # Specify the relative path to the config file
    config_file_path = "Config/mongod.conf"

    # Get the full path
    full_path = get_full_path(config_file_path)

    # Print the full path
    print(f"Full path to the config file: {full_path}")
