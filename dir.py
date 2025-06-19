from pathlib import Path

def find_files_with_suffix(root:str, suffix:str)-> list[Path]:
    """
    Recursively find all files with a specific suffix in a directory.

    :param root: The root directory to start the search.
    :param suffix: The file suffix to look for (e.g., '.txt').
    :return: A list of file paths that match the suffix.
    """
    root_path = Path(root)
    return list(root_path.rglob(f'*{suffix}'))

def find_files_with_ancestor_and_suffix(root:str, ancestor_name:str, suffix:str)-> list[Path]:
    """
    Find all files with a specific suffix that have an ancestor directory with a specific name.

    :param root: The root directory to start the search.
    :param ancestor_name: The name of the ancestor directory to look for.
    :param suffix: The file suffix to look for (e.g., '.txt').
    :return: A list of file paths that match the criteria.
    """
    root_path = Path(root)
    return [file for file in root_path.rglob(f'*{suffix}') if has_ancestor(file, ancestor_name)]

def has_ancestor(file:Path, ancestor_name:str)-> bool:
    """
    Check if a file has an ancestor directory with a specific name.

    :param file: The file path to check.
    :param ancestor_name: The name of the ancestor directory to look for.
    :return: True if the ancestor exists, False otherwise.
    """
    return any(ancestor.name == ancestor_name for ancestor in file.parents)

def get_ancestor(file:Path, ancestor_name:str)-> Path | None:
    """
    Get the ancestor directory with a specific name for a given file.

    :param file: The file path to check.
    :param ancestor_name: The name of the ancestor directory to look for.
    :return: The path of the ancestor directory if found, None otherwise.
    """
    for ancestor in file.parents:
        if ancestor.name == ancestor_name:
            return ancestor
    return None

def has_child(directory:Path, child:str)-> bool:
    """
    Check if a directory has a child with a specific name.

    :param directory: The directory path to check.
    :param child: The name of the child to look for.
    :return: True if the child exists, False otherwise.
    """
    return (directory / child).exists()

def get_children(directory:Path)-> list[Path]:
    """
    Get all children of a directory.

    :param directory: The directory path to check.
    :return: A list of paths of the children in the directory.
    """
    if not directory.is_dir():
        return []
    return list(directory.iterdir())

def get_parent(file:Path)-> Path | None:
    """
    Get the parent directory of a file.

    :param file: The file path to check.
    :return: The parent directory path if it exists, None otherwise.
    """
    return file.parent if file.parent.exists() else None