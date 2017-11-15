import pytest
import os

def env():
    assert os.environ["TEST_ENV"] == "Mars"
