import logging
import os
import sys

class AppLogger:
    def __init__(self, log_file="app.log"):
        # Xác định đường dẫn log file
        if hasattr(sys, "_MEIPASS"):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")

        log_path = os.path.join(base_path, log_file)

        # Cấu hình logging
        logging.basicConfig(
            level=logging.DEBUG,  # mức log: DEBUG, INFO, WARNING, ERROR
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                logging.FileHandler(log_path, encoding="utf-8"),
                logging.StreamHandler()  # vẫn in ra console khi debug
            ]
        )
        self.logger = logging.getLogger("AppLogger")

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)
