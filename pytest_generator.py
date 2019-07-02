#!/usr/bin/env python3
from abc import ABCMeta, abstractmethod

import yaml


class Questioner:
    atcoder = "atcoder"
    # paiza = "paiza"


class PyTestGenerator(metaclass=ABCMeta):
    def __init__(self, is_test=False):
        if is_test:
            self.config_file = "./config_test.yml"
        else:
            self.config_file = "./config.yml"
        with open(self.config_file, encoding='utf-8') as file:
            self.config = yaml.load(file)

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def fetch_html(self):
        pass

    @abstractmethod
    def define_sample_set(self):
        pass

    @abstractmethod
    def build_codes(self):
        pass


class AtCoderTestGenerator(PyTestGenerator):

    def __init__(self, is_test=False):
        super().__init__(is_test)
        print(self.config["atcoder"])

    def login(self):
        pass

    def fetch_html(self):
        pass

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


