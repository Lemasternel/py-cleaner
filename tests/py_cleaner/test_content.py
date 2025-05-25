"""
This module tests if the JSON content is being deserialized correctly
to the Content type.
"""

from os import makedirs, listdir
from os.path import exists, expandvars, join
from json import dump

from src.py_cleaner.content import Content, deserialize
from src.py_cleaner.executor import __del_dirs, __emp_dirs
from tests.py_cleaner import env_vars


__DELETE_DIRS = ["${appdata}\\py-cleaner\\Test", "${appdata}\\py-cleaner\\Test2"]
__CLEAR_DIRS = ["$appdata}\\py-cleaner\\Test3", "${appdata}\\py-cleaner\\Test4"]

def test_emp_dirs():
    """
    Tests if the __emp_dirs() function from src.py_cleaner.executor.py
    is emptying the given Content.clear_dirs directories.
    """

    __prepare()
    content = deserialize(env_vars.RES_CONTENT_JSON)

    __emp_dirs(content.clear_dirs)

    # Verify directories were emptied
    for d in content.clear_dirs:
        d = expandvars(d)
        assert not listdir(d), f'Directory {d} should be empty'

def test_del_dirs():
    """
    Tests if the __del_dirs() function from src.py_cleaner.executor.py
    is deleting the given Content.delete_dirs directories.
    """

    __prepare()
    content = deserialize(env_vars.RES_CONTENT_JSON)

    __del_dirs(content.delete_dirs)

    # Verify directories were deleted
    for d in content.delete_dirs:
        d = expandvars(d)
        assert not exists(d), f'Directory {d} should be deleted'

def test_deserialize():
    """
    Tests if the Content.deserialize() function is returning exactly
    the same JSON configured in the __prepare() method.
    """
    __prepare()
    c = deserialize(env_vars.RES_CONTENT_JSON)

    assert isinstance(c, Content), f'Expected {Content}, got {type(c)}'

    # the Content data must be the same defined in __DELETE_DIRS and __CLEAR_DIRS
    assert c.delete_dirs == __DELETE_DIRS, f'Expected {__DELETE_DIRS}, got {c.delete_dirs}'
    assert c.clear_dirs == __CLEAR_DIRS, f'Expected {__CLEAR_DIRS}, got {c.clear_dirs}'

def __prepare():
    """
    Configure the required environment for this test module.
    """
    # configuring the JSON file with itens to be deleted and others to be emptied
    c = Content(__DELETE_DIRS, __CLEAR_DIRS)
    with open(env_vars.RES_CONTENT_JSON, 'w', encoding='utf-8') as f:
        dump(c.__dict__, f)

    # creating the required directories
    for d in *__DELETE_DIRS, *__CLEAR_DIRS:
        d = expandvars(d)
        if not exists(d):
            makedirs(d, exist_ok=True)

    # creating subdirectories and files inside __CLEAR_DIRS paths
    for d in __CLEAR_DIRS:
        d = expandvars(d)
        makedirs(join(d, 'sub_test'), exist_ok=True)
        with open(join(d, 'test.txt'), 'w', encoding='utf-8'):
            pass
