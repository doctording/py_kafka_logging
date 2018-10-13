# -*- coding: utf-8 -*-
"""Module to test out logging to kafka."""

from py_logging_kafka.logging_config import logger


def test_log():
    logger.info("test info")
    logger.debug("test debug")

if __name__ == "__main__":
    test_log()
