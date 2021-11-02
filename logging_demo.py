"""
Examples of using Python's logging facility.

Run the file in Python and observe:
Which messages are actually printed on the console or to a file?
What information is in the message?

For details, see: https://docs.python.org/3/library/logging.html
"""
import logging


def logging_test(logger):
    """Log messages using each of the standard logging levels 
       plus 1 custom log level.
    """
    level = logging.WARN + 5  # custom log level
    logging.addLevelName(level, 'LEVEL')
    assert logging.getLevelName(level) == 'LEVEL'

    logger.debug(logging.DEBUG)
    logger.info(logging.INFO)
    logger.warning(logging.WARN)
    logger.log(level=level, msg=level)
    logger.error(logging.ERROR)
    logger.critical(logging.CRITICAL)


def simple_config():
    """Configure logging using basicConfig for simple configuration.

    You should call this before creating any logging objects.
    You can call basicConfig only once. 

    Some named attributes you can set using basicConfig are:

        filename = "name of a file to send log messages to"
        filemode = 'a' (append), 'w' (truncate & open for writing)
        format = a string describing format of log messages
        stream = name of a StreamHandler to use, cannot use with filename attribute
        level = the root logger level (threshold level for log msgs)

    See:  help(logging.basicConfig)
    https://docs.python.org/3/library/logging.html#logging.basicConfig
    """
    # use a custom format for log messages
    FORMAT = '%(asctime)s %(name)s %(levelname)s: %(message)s'
    logging.basicConfig(format=FORMAT)


def my_config():
    """Write your own logging configuration."""
    # TODO write your own logging configuration
    #      specify a log file, threshold level, format, and append mode
    pass


if __name__ == "__main__":
    #
    # TODO Configure logging using one of these choices:

    # 1. Call basicConfig with the default settings
    logging.basicConfig()

    # 2. Call simple_config to set the format of log messages.
    #    Comment out the above call (#1) to basicConfig for this.
    # simple_config()

    # 3. my_config() write your own logging configuration as
    #    described in the assignment. 
    #    Comment out the above calls to simple_config and basicConfig.
    # my_config() 

    # Log some messages to the root logger using different logging levels.
    logger = logging.getLogger()
    print("Logging to ", str(logger))
    logging_test(logger)

    # TODO create a named logger, set a a custom log threshold,
    #       and call logging_test again with your named logger.
