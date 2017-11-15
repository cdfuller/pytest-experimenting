import pytest
import os

def test_env():
    assert os.environ["TEST_ENV"] == "Mars"
