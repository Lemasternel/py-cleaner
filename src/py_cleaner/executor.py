"""
Process the deletion and clearing listed in the JSON content.
"""

from shutil import rmtree
from os.path import expandvars
from pathlib import Path

from py_cleaner.content import Content
from py_cleaner.infra.log import logger


def execute(*contents: Content) -> None:
    """
    Executes a series of operations on the provided `Content` objects. It performs
    actions like deleting or emptiyng directories for each `Content` instance provided as input.

    :param contents: Sequence of `Content` objects on which
    operations are to be performed.
    :type contents: *Content

    :return: None
    """

    for c in contents:
        __del_dirs(c.delete_dirs)
        __emp_dirs(c.clear_dirs)

def __del_dirs(dirs: list[str]) -> None:
    """
    Performs and delete operation on the directory (itself and its contents).

    :param dirs: List of directories to delete
    :type dirs: list[str]

    :raises FileNotFoundError: If the specified directory does not exist.
    :raises PermissionError: If there are not enough permissions to delete the directory.
    :raises OSError: For other errors encountered while deleting the directory.

    :return: None
    """

    logger.info("Deleting directories: %s", dirs)
    for d in dirs:
        try:
            rmtree(expandvars(d))
        # no problem if the directory was not found
        except FileNotFoundError:
            logger.info("Directory %s not found.", d)
        except PermissionError as ex:
            logger.error("Permission denied to delete directory %s: %s", d, ex)
            raise
        except OSError as ex:
            logger.error("An error occurred while deleting directory %s: %s", d, ex)
            raise

def __emp_dirs(dirs: list[str]) -> None:
    """
    Performs a deletion operation on the subitoms of the directory (contents only).

    :param dirs: List of directories to empty
    :type dirs: list[str]

    :raises FileNotFoundError: If the specified directory does not exist.
    :raises PermissionError: If there are not enough permissions to delete the directory.
    :raises OSError: For other errors encountered while deleting the directory.

    :return: None
    """

    logger.info("Emptying directories: %s", dirs)
    for d in dirs:
        try:
            # delete all files and subdirectories
            for sitem in Path(expandvars(d)).iterdir():
                if sitem.is_dir():
                    rmtree(sitem)
                else:
                    sitem.unlink()
        # no problem if the directory was not found
        except FileNotFoundError:
            logger.info("Directory %s not found.", d)
        except PermissionError as ex:
            logger.error("Permission denied to empty directory %s: %s", d, ex)
            raise
        except OSError as ex:
            logger.error("An error occurred while emptying directory %s: %s", d, ex)
            raise
