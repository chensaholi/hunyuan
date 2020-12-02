# -*- coding: utf-8 -*-
import logging
import os
import re
from logging.handlers import TimedRotatingFileHandler


def get_logger(monitor_name):
    logger = logging.getLogger(monitor_name)
    logger.setLevel(logging.INFO)
    fmt = logging.Formatter(
        '%(asctime)s - %(module)s.%(funcName)s.%(lineno)d - %(levelname)-8s: %(message)s',
        '%Y-%m-%d %H:%M:%S'
    )
    log_path = "log"
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    file_path = os.path.join(log_path, monitor_name + ".txt")
    log_handler = TimedRotatingFileHandler(filename=file_path, when="MIDNIGHT",
                                           interval=1, backupCount=3)
    log_handler.suffix = "%Y-%m-%d.log"
    # log_handler.suffix = "%Y-%m-%d_%H-%M.log"
    log_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")
    log_handler.setLevel(logging.INFO)
    log_handler.setFormatter(fmt)
    logger.addHandler(log_handler)
    return logger


def console_logger():
    logger = logging.getLogger("factory6")
    logger.setLevel(logging.INFO)
    console_formatter = logging.Formatter(
        '%(asctime)s %(name)s: %(levelname)-8s: %(message)s',
        '%Y-%m-%d %H:%M:%S'
    )
    # file_path = os.path.join(log_path, 'ifactory6')
    log_handler = logging.StreamHandler()
    log_handler.setLevel(logging.INFO)
    log_handler.setFormatter(console_formatter)
    logger.addHandler(log_handler)
    return logger
