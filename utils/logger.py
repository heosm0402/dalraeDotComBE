import logging

def get_initialized_logger(name, level, file_path):
    # create logger and set level
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # add handler
    handler = logging.FileHandler(file_path)
    stream_handler = logging.StreamHandler()

    logger.addHandler(handler)
    logger.addHandler(stream_handler)

    # add formatter to handler
    formatter = logging.Formatter("%(asctime)s %(relativeCreated)6d %("
                                  "threadName)s %(funcName)s %(levelname)s %("
                                  "message)s")
    handler.setFormatter(formatter)

    return logger
