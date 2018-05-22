# -*- coding: utf-8 -*-


# 传函数名
# from functools import wraps
# 传说中的单例模式
def single(func):
    ins = {}
    # 函数参数
    # @wraps(func)
    def wraper(*args, **kwargs):
        if func not in ins:
            ins[func] = func(*args, **kwargs)
        return ins[func]

    return wraper


@single
def foo():
    pass

#装饰器*****1.传装饰器参数 2。传闭包的函数名 3. 传闭包函数的参数

a = foo()
b = foo()
print(a is b)
