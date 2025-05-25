# Py-cleaner

## Description

This project is a folder cleaning utility designed to automate
a common task I frequently use in other projects.

### Configuration

To configure which folders to clean, modify the
[default.json](src/py_cleaner/res/default.json) file in the `py_cleaner.res` folder.

The `clear_dirs` list specifies directories whose contents should be
deleted while preserving the directory itself.

The `delete_dirs` list specifies directories to be completely removed,
including their contents.

## Development

Technologies used in this project:

- Python 3.13.3
- Poetry 2.1.3
- Pytest 8.3.5
- Pylint 3.3.7
