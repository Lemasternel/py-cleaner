"""
This module serves as the main entry point for the Py Cleaner application.
It initializes the application, executes the cleaning process based on the configured
JSON content. The cleaning process involves deleting and emptying specified
directories based on the JSON configuration.
"""

from time import perf_counter

from py_cleaner.executor import execute
from py_cleaner.content import deserialize
from py_cleaner.env_vars import RES_CONTENT_JSON
from py_cleaner.infra.log import logger


def main() -> None:
    """
    The main entry point.

    :return: None
    """

    logger.info("===== Starting Py Cleaner =====")

    init = perf_counter()
    execute(deserialize(RES_CONTENT_JSON))
    end = perf_counter()

    logger.info("===== Py Cleaner finished in %s seconds =====", format(end - init, ".6f"))

if __name__ == "__main__":
    main()
