import os
import glob
import shutil

# Define the base directory as the script's parent directory
base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the script

# Define absolute paths
db_dir = os.path.join(base_dir, "..", "Data", "db")  # Absolute path to Data/db
log_file = os.path.join(base_dir, "..", "Logs", "mongod.log")  # Absolute path to Logs/mongod.log

# Debugging: print paths
print(f"DB Directory: {db_dir}")
print(f"Log File: {log_file}")

def reset_db_directory(db_path):
    """Delete all files and directories in the db directory except README.md"""
    try:
        # Get all files and directories in the directory
        files = glob.glob(os.path.join(db_path, "*"))
        
        for file in files:
            # Keep README.md, delete others
            if os.path.basename(file) != "README.md":
                if os.path.isfile(file):
                    os.remove(file)
                    print(f"Deleted file: {file}")
                elif os.path.isdir(file):
                    # Recursively delete non-empty directories
                    shutil.rmtree(file)
                    print(f"Deleted directory: {file}")
                    
    except Exception as e:
        print(f"Error resetting db directory: {e}")

def reset_log_file(log_path):
    """Truncate (empty) the mongod.log file if it exists"""
    try:
        print(f"Checking if log file exists: {log_path}")
        if os.path.exists(log_path):
            print(f"Log file found. Truncating: {log_path}")
            # Open log file in write mode to truncate it
            with open(log_path, 'w'):
                pass
            print(f"Truncated log file: {log_path}")
        else:
            print(f"Log file does not exist: {log_path}. No action taken.")
    except Exception as e:
        print(f"Error truncating log file: {e}")

if __name__ == "__main__":
    # Reset the Data/db directory and Logs/mongod.log
    reset_db_directory(db_dir)
    reset_log_file(log_file)
