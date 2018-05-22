from logzero import logger


def use_logging(func):
    def wrapper():
        logger.info("%s is running" % func.__name__)
        return func()

    return wrapper


@use_logging
def foo():
    return 1+2


if __name__ == '__main__':
    a = foo()
    print(a)