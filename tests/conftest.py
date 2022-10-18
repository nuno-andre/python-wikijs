from pathlib import Path
import logging
import sys
import os

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1].joinpath('src')))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture(scope='session')
def client():
    from wikijs import WikiJs

    try:
        endpoint = os.environ['WIKIJS_ENDPOINT']
        api_key = os.environ['WIKIJS_API_KEY']
    except KeyError:
        raise RuntimeError('You need to set WIKIJS_ENDPOINT and WIKIJS_API_KEY '
                           'environment variables to run the tests.')

    return WikiJs(endpoint, api_key)


@pytest.fixture(scope='session')
def log():
    return logger


@pytest.fixture(scope='session')
def camel():

    def camel_case(string):
        first, *rest = string.split('_')
        return first + ''.join(map(str.capitalize, rest))

    return camel_case
