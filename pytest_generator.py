#!/usr/bin/env python3
from abc import ABCMeta, abstractmethod

import requests
import yaml
from bs4 import BeautifulSoup


class Questioner:
    atcoder = "atcoder"
    # paiza = "paiza"


class PyTestGenerator(metaclass=ABCMeta):
    def __init__(self, is_test=False):
        """
        Args:
            is_test: (bool) Are you testing?
        """
        if is_test:
            self.config_file = "./config_test.yml"
        else:
            self.config_file = "./config.yml"
        with open(self.config_file, encoding='utf-8') as file:
            self.config = yaml.safe_load(file)

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def fetch_html(self, url):
        pass

    @abstractmethod
    def define_sample_set(self):
        pass

    @abstractmethod
    def build_codes(self):
        pass


class AtCoderTestGenerator(PyTestGenerator):
    """For AtCoder's Pytest Generator"""

    def __init__(self, is_test=False):
        """
        Args:
            is_test: (bool) Are you testing?


        `self.config`: (dict<str, str>)
            'login': login method; AtCoder only uses a password.
            'login_url': The `lang=en` argument is meaningless and gives the same result whether or not it is used.
            'id': login ID
            'password': login password
            'csrf_token': Learn not only about algorithms, but also how the Web works (c.f., https://en.wikipedia.org/wiki/Cross-site_request_forgery)
        """
        super().__init__(is_test)
        self.config = self.config["AtCoder"]

        self.session = requests.Session()
        request = self.session.get(self.config["login_url"])
        soup = BeautifulSoup(request.text, features="html.parser")
        self.config["csrf_token"] = soup.find(attrs={
            'name': 'csrf_token'
        }).get('value')

    def login(self):
        """
        Give AtCoder login information to session.

        Returns:
            None
        """
        self.session.post(self.config["login_url"], data=self.config)

    def fetch_html(self, url):
        """
        Fetch a HTML source from the URL of the problem statement.

        Args:
            url: URL of the problem statement page.

        Returns:
            HTML source
        """
        request = self.session.get(url)
        html = BeautifulSoup(request.text, features="html.parser")
        return html

    def define_sample_set(self):
        pass

    def build_codes(self):
        pass


# class PaizaTestGenerator(PyTestGenerator):
#     def __init__(self, is_test=False):
#         super().__init__(is_test)
#         print(self.config["Paiza"])
#
#     def login(self):
#         super().login()
#
#     def fetch_html(self):
#         super().fetch_html()
#
#     def define_sample_set(self):
#         super().define_sample_set()
#
#     def build_codes(self):
#         super().build_codes()


class PyTestFactory:
    def __init__(self, questioner):
        # To avoid spelling variants.
        self.questioner = questioner.lower()

    def create(self, is_test=False):
        if self.questioner == Questioner.atcoder:
            return AtCoderTestGenerator(is_test)
        # elif self.questioner == Questioner.paiza:
        #     return PaizaTestGenerator(is_test)
