import logging
import os

class LogManager:
    loggers = {}

    @classmethod
    def get_logger(cls, name, level=logging.DEBUG, log_file="log/app.log"):
        if name not in cls.loggers:
            logger = logging.getLogger(name)
            logger.setLevel(level)
            formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

            if not logger.handlers:
                stream_handler = logging.StreamHandler()
                stream_handler.setFormatter(formatter)
                logger.addHandler(stream_handler)

                if log_file:
                    os.makedirs(os.path.dirname(log_file), exist_ok=True)

                    file_handler = logging.FileHandler(log_file)
                    file_handler.setFormatter(formatter)
                    logger.addHandler(file_handler)

            cls.loggers[name] = logger

        return cls.loggers[name]
