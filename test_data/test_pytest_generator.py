import pytest

import pytest_generator
from pytest_generator import PyTestFactory

if __name__ == '__main__':
    questioner = PyTestFactory("atcoder").create(is_test=True)