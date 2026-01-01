"""
**********************************************
*            Script Information             *
**********************************************
Script Name: Setup_New_Project_Dictionary
Author: [Vibycat]
Date: [01/01/2026]
Description:
    Simple project folder creator that:
      1) Asks for a project identifier string (ProjectNumber/Name)
      2) Creates the project root folder inside a chosen main directory
      3) Uses a dictionary to map and create subdirectories (no templates, no file copying)
Version: [1.0.1]
**********************************************
"""

# **********************************************
# *                 Imports                    *
# **********************************************
from pathlib import Path


# **********************************************
# *            Project Folder Map              *
# **********************************************
PROJECT_TREE = {
    "PLC": [
        "Working_Dir",
        "Backups_Dir",
        "Archive",
    ],
    "HMI": [
        "Working_Dir",
        "Backups_Dir",
        "Archive",
    ],
    "Robot_Program": [
        "Working_Dir",
        "Backups_Dir",
        "Archive",
    ],
    "Safety_Controller": [
        "Working_Dir",
        "Backups_Dir",
        "Archive",
    ],
    "Robot_SIM": [
        "Working_Dir",
        "Backups_Dir",
        "Archive",
    ],

    "Full_Project_Backup": [
        "Backups_Dir",
        "Archive",
    ],

}


# **********************************************
# *            Helper Functions               *
# **********************************************
def sanitize_name(name: str) -> str:
    """Remove characters that can break folder creation on Windows/Linux."""
    if not name:
        return ""
    bad_chars = '<>:"/\\|?*'
    cleaned = name.strip()
    for ch in bad_chars:
        cleaned = cleaned.replace(ch, "_")
    return cleaned.rstrip(". ").strip()


def get_main_directory_from_user() -> Path:
    """Ask user where to create the project. Enter = current working directory."""
    print("\nWhere should the project be created?")
    print("Example: D:/Projects/Controls  (or press Enter for current folder)\n")
    user_input = input("Main directory path: ").strip()
    return Path.cwd() if not user_input else Path(user_input).expanduser().resolve()


def print_tree_preview(tree: dict) -> None:
    """Show what will be created, grouped by dictionary keys."""
    print("\nPlanned folder map:")
    for group, folders in tree.items():
        print(f"  [{group}]")
        for f in folders:
            print(f"    - {f}")


def create_project_structure(main_dir: Path, project_id: str, tree: dict) -> Path:
    """
    Create:
      <main_dir>/<project_id>/<group>/<subfolder>
    Returns the created project path.
    """
    project_id = sanitize_name(project_id)
    if not project_id:
        raise ValueError("Project identifier cannot be empty.")

    if not main_dir.exists():
        raise FileNotFoundError(f"Main directory does not exist: {main_dir}")

    project_dir = main_dir / project_id
    if project_dir.exists():
        raise FileExistsError(f"Project directory already exists: {project_dir}")

    # Create project root
    project_dir.mkdir(parents=True, exist_ok=False)

    # Create group folders + their subfolders
    for group, subfolders in tree.items():
        group_dir = project_dir / sanitize_name(group)
        group_dir.mkdir(parents=True, exist_ok=True)

        for sub in subfolders:
            (group_dir / sanitize_name(sub)).mkdir(parents=True, exist_ok=True)

    return project_dir


# **********************************************
# *                Main Logic                  *
# **********************************************
def main():
    print("============================================")
    print("  Simple Project Creator (Dictionary Tree)  ")
    print("============================================")

    print_tree_preview(PROJECT_TREE)

    main_dir = get_main_directory_from_user()
    print(f"\nMain directory: {main_dir}")

    project_id = input("\nEnter project identifier (ProjectNumber/Name): ").strip()

    try:
        project_path = create_project_structure(main_dir, project_id, PROJECT_TREE)
        print("\nProject created successfully!")
        print(f"Project path: {project_path}")

        print("\nCreated folders:")
        for group, subfolders in PROJECT_TREE.items():
            for sub in subfolders:
                print(f"  - {project_path / group / sub}")

    except Exception as e:
        print("\nError:")
        print(e)


if __name__ == "__main__":
    main()
