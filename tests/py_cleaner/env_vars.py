"""
Environment variables used in the test cases.
"""

from os.path import join
from importlib.resources import files


# Resource path, subfolders and files
RESOURCES_PATH = str(files("tests.py_cleaner.res"))
RES_CONTENT_JSON = join(RESOURCES_PATH, "default.json")
