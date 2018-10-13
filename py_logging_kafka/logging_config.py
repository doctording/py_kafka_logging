# -*- coding: utf-8 -*-
import logging.config


# DEV / TEST
DEV = "TEST"
if DEV == "TEST":
    logging.config.fileConfig("logger_test.conf")
if DEV == "DEV":
    logging.config.fileConfig("logger_dev.conf")
logger = logging.getLogger("root")

