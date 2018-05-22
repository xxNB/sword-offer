# -*- coding: utf-8 -*-


class typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(
                "{} should be {}".format(self.name, str(self.expected_type)))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


def type_assert(**kwargs):
    def warped(cls):
        for name, typedd in kwargs.items():
            setattr(cls, name, typed(name, typedd))
        return cls

    return warped


@type_assert(name=str, age=int, chengji=float)
class Student:
    def __init__(self, name, age, chengji):
        self.name = name
        self.age = age
        self.chengji = chengji


c = Student(name="linzhaoyu", age=24, chengji=9.8)
