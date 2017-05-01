"""
Config module to parse and read values from `config.yaml`.
"""

import os
import yaml

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
CONFIG_PATH = os.path.join(DIR_PATH, "config.yaml")


def get(key):
    """Return value for `key`."""
    config = yaml.safe_load(open(CONFIG_PATH))
    return config.get(key, None)
