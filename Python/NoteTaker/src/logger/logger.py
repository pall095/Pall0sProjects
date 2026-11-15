import logging


class AppLogger:

    _logger = None

    @classmethod
    def get_logger(cls) -> logging.Logger:

        if cls._logger is None:

            logger = logging.getLogger("NoteTaker")
            logger.setLevel(logging.INFO)
            logger.propagate = False

            formatter = logging.Formatter(
                fmt="[%(levelname)s][%(asctime)s] %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)

            logger.addHandler(console_handler)

            cls._logger = logger

        return cls._logger

    @classmethod
    def configure(cls, verbosity_level: str) -> None:

        logger = cls.get_logger()

        level = getattr(logging, verbosity_level.upper(), None)

        if not isinstance(level, int):
            raise ValueError(
                f"Invalid logging level: {verbosity_level}"
            )

        logger.setLevel(level)