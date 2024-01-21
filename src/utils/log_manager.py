import logging


class LogManager:
    loggers = {}

    @classmethod
    def get_logger(cls, name, level=logging.INFO, log_file="app.log"):
        if name not in cls.loggers:
            logger = logging.getLogger(name)
            logger.setLevel(level)

            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )

            ch = logging.StreamHandler()
            ch.setFormatter(formatter)
            logger.addHandler(ch)

            if log_file:
                fh = logging.FileHandler(log_file)
                fh.setFormatter(formatter)
                logger.addHandler(fh)

            cls.loggers[name] = logger

        return cls.loggers[name]
