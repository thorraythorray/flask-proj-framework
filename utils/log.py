import os
import logging
import logging.config

import yaml

from etc.config import ROOT, ENV


def init_log():
    logging.logThreads = 0
    logging.logProcesses = 0
    logging._srcfile = None  # pylint: disable=protected-access
    log_yaml = os.path.join(ROOT, "config/logging.yaml")
    with open(log_yaml) as log_file:
        logging_config = yaml.safe_load(log_file)
    logging.config.dictConfig(logging_config)
    _logger = logging.getLogger('app.{}'.format(ENV))
    _logger.name = ENV
    return _logger


logger = init_log()  # pylint: disable=invalid-name
