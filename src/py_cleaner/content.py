"""
This module provides a data structure used in the JSON file.
Also provides a function to deserialize the JSON content.
"""

from json import load, JSONDecodeError
from dataclasses import dataclass

from py_cleaner.infra.log import logger


@dataclass
class Content:
    """
    Represents the JSON content configuration.

    This class is designed to store lists of directory paths that are intended
    for deletion or content clearance.

    :ivar delete_dirs: List of directory paths to be deleted.
    :type delete_dirs: list[str]

    :ivar clear_dirs: List of directory paths where content should be cleared.
    :type clear_dirs: list[str]
    """

    delete_dirs: list[str]
    clear_dirs: list[str]

def deserialize(json_file: str) -> Content:
    """
    Deserializes a JSON file into a `Content` object.

    :param json_file: Path to the JSON file.
    :type json_file: str

    :return: An instance of the `Content` class populated with data obtained from the JSON file.
    :rtype: Content

    :raises FileNotFoundError: If the specified JSON file does not exist.
    :raises PermissionError: If there are not enough permissions to read the file.
    :raises JSONDecodeError: If the file cannot be decoded as a valid JSON format.
    :raises UnicodeDecodeError: If the file cannot be decoded as a valid UTF-8 format.
    :raises OSError: For other OS-level errors encountered while processing the file.
    """

    logger.info("Deserializing %s", json_file)
    try:
        with open(json_file, 'r', encoding="utf-8") as f:
            return Content(**load(f))
    except FileNotFoundError as ex:
        logger.critical("File %s not found: %s", json_file, ex)
        raise
    except PermissionError as ex:
        logger.critical("Permission denied to read file %s: %s", json_file, ex)
        raise
    except JSONDecodeError as ex:
        logger.critical("Error while parsing JSON file %s: %s", json_file, ex)
        raise
    except UnicodeDecodeError as ex:
        logger.critical("Error while decoding file %s: %s", json_file, ex)
        raise
    except OSError as ex:
        logger.critical("An error occurs while processing file %s: %s", json_file, ex)
        raise
