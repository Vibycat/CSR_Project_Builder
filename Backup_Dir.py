# Python script for creating automatic backups of the Vibytweaks minecraft server 

# imports:
import os 
import datetime 
import shutil 


# set path variables 
cwd = os.getcwd()
target_path = os.path.join(cwd,"Working_Dir")

# configure base bacup folder path (change this as needed.)
base_backup_path = os.path.join(cwd,"Backups_Dir")

# ensure the base backup folder exists.
os.makedirs(base_backup_path, exist_ok=True)


# Define a list of directories for the backup to ignore ( exampole: the Main backup folder; to avoid recursion of backups)
def ignore_directories(src, names):

    IGNORED_DIRECTORIES = [
        "Full_Project_Backup"
        "Ignore_This_Directory"

    ]

    return {name for name in names if name in IGNORED_DIRECTORIES}



def backup_world_folder():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    destination = os.path.join(base_backup_path, f"Backups_Dir_{timestamp}")

    try:
        shutil.copytree(
            target_path,
            destination,
            ignore=ignore_directories
        )
        print(f"Backup completed successfully:\n{destination}")

    except Exception as e:
        print(f"Backup failed: {e}")

# Create main fucntion
def main():
    # add a comment to server (backup started warning: using Rcon)
    print(f"Starting Project backup... \nSource: {target_path}\nBackup Directory: {base_backup_path}")
    backup_world_folder()


# start main script
if __name__=="__main__":
    main()
