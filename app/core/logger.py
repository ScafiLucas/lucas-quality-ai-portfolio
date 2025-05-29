import json
import logging
import sys


class JsonFormatter(logging.Formatter):
    def format(self, record):
        record_dict = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "funcName": record.funcName,
            "lineNo": record.lineno,
        }
        if record.args:
            record_dict.update(record.args)
        return json.dumps(record_dict, ensure_ascii=False)


def get_logger(name: str = "app"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)

        try:
            handler.stream.reconfigure(encoding="utf-8")
        except Exception:
            pass

        formatter = JsonFormatter()
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
