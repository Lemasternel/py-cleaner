"""
This module configures and sets up logging for the entire application.
It uses a rotating file logger with console output, setting up formatted
log messages that include timestamp, log level, module name, function name, and
line number. The logger is configured to create backup files when size limits
are reached, maintaining up to 5 backup files of 1MB each.
"""

from logging import INFO, StreamHandler, getLogger, Formatter
from logging.handlers import RotatingFileHandler

from py_cleaner.infra.env_vars import LOG_FILE


# config the log file max size and the maximum number of log files
__handler = RotatingFileHandler(
    filename=LOG_FILE,
    maxBytes=1024*1024, #1MB per file
    backupCount=2) #Max file counts
__handler.setLevel(INFO)

# set how logs are displayed
__handler.setFormatter(Formatter("%(asctime)s->"
                                 "%(levelname)s->"
                                 "%(module)s->"
                                 "%(funcName)s->"
                                 "%(lineno)d->"
                                 "%(message)s"))

# config log output in the console alongside the .txt
__console = StreamHandler()
__console.setLevel(INFO)

# the propper log to be used
logger = getLogger()
logger.setLevel(INFO)

# atach the console and handler configs
logger.handlers.clear()
logger.addHandler(__handler)
logger.addHandler(__console)
