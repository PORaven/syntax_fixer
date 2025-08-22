from abc import ABC, abstractstaticmethod, abstractproperty
from random import randint
import math
from pprint import pprint
from typing import Collection, List, Dict


class Test(Exception):
    def __init__(
        self, *args: object, description: str = "Hello, test pre-commit"
    ) -> None:
        super().__init__(*args)
        self.description = description

    def __repr__(self) -> str:
        return f"{self.description}"

    def add_object_property(
        self, option: dict[str | int, str | int]
    ) -> "Test":  # возвращаем self, исправлена аннотация
        self.properties = option
        return self

    @staticmethod
    def convert_abs(num: int) -> None:  # исправлен метод на статический
        print(abs(num))


def h() -> None:
    print("Hello")


def ppr() -> None:
    pprint(randint(1, 10))  # исправлено использование math
