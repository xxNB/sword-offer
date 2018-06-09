def func1(func):
    c = 1
    def func2():
        print("=======")
        c = 10*100
        return c
    return func2

@func1
def b():
    pass

b()

import _threading_local