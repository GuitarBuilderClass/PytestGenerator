import pytest

import pytest_generator
from pytest_generator import PyTestFactory

if __name__ == '__main__':
    questioner = PyTestFactory("atcoder").create(is_test=True)
    questioner.login()
    print(questioner.fetch_html("https://atcoder.jp/contests/abs/tasks/abc086_a"))

