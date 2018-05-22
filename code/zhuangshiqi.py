# -*- coding: utf-8 -*-
class Foo:
    """类装饰器
    """
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print("class decorator running")
        self._func()
        print("clss decorator ending")


@Foo
def bar():
    print("bar")


bar()

