import functools
import itertools
import os
import shutil


def absfiles(files):
    """ Maps all given relative paths to absolute paths.

    Args:
        files (iterable[str]): An iterable of relative paths.

    Returns:
        generator[str]: A generator of absolute paths.
    """
    return map(os.path.abspath, files)


def copy(src, dest):
    """ Copies a file to a given destination.

    Args:
        src (str): The path to the source file.
        dest (str): The path to the destination file.

    Returns:
        None
    """
    __copy(shutil.copy, src, dest)
    return None


def deepcopy(src, dest):
    """ Copies a file to a given destination. Keeps the file metadata.

    Args:
        src (str): The path to the source file.
        dest (str): The path to the destination file.

    Returns:
        None
    """
    __copy(shutil.copy2, src, dest)
    return None


def file_has_extensions(extensions, filename):
    """ Checks that the given filename has any of the given extensions.
    Args:
        extensions (iterable[str]): The extensions to check against (no '.' delimiter).
        filename (str): The filename.

    Returns:
        bool: Indicates if the filename has one of the given extensions.
    """
    _, filename = os.path.split(filename)
    _, file_extension = os.path.splitext(filename)
    return any(extension in file_extension for extension in extensions)



def get_filesize(path):
    """ Gets the size of the file at the given path.

    Args:
        path (str): The path of file.

    Returns:
        int: The filesize in bytes.
    """
    return os.stat(path).st_size


def pretty_filesize(bytes):
    """ Gives a human-readable filesize given a size in bytes.

    Args:
        bytes (int): A size in bytes.

    Returns:
        str: A human-readable filesize.
    """
    if bytes >= 1024**3:
        return "{:.2f}".format(bytes/1024**3) + "GB"
    elif bytes >= 1024**2:
        return "{:.2f}".format(bytes/1024**2) + "MB"
    elif bytes >= 1024:
        return "{:.2f}".format(bytes/1024) + "KB"
    else:
        return "{}B".format(bytes)


def walk(path):
    """ Gets all the files in the given directory and all its subdirectories.

    Args:
        path (str): The path where to walk.

    Returns:
        generator[str]: A generator of the relative paths of the files in the given
                        directory and all its subdirectories.
    """
    walk_iter = os.walk(path)
    files_by_dir = (__join_dirname_filenames(dirname, filenames) for dirname, _, filenames in walk_iter)
    files = itertools.chain.from_iterable(files_by_dir)
    return files


def walk_by_extensions(path, extensions):
    """ Gets all the files in the given directory and all its subdirectories matching the given extensions.

    Args:
        path (str): The path where to walk.
        extensions (iterable[str]): The extensions to check against (no '.' delimiter).

    Returns:
        generator[str]: A generator of the relative paths of the files in the given
                        directory and all its subdirectories filtered by extensions.
    """
    walk_iter = walk(path)
    return filter(functools.partial(file_has_extensions, extensions), walk_iter)


def __copy(copy_func, src, dest):
    dirname = os.path.dirname(dest)
    os.makedirs(dirname, exist_ok=True)
    copy_func(src, dest)


def __join_dirname_filenames(dirname, filenames):
    return (os.path.join(dirname, filename) for filename in filenames)
