# -*- coding: utf-8 -*-
"""
Found on GitHub from user deshipu. Used as a driver for BNO055 with the 
micropython language we have been using.

@author: deshipu
"""


def partial(func, *args, **kwargs):
    def _partial(*more_args, **more_kwargs):
        kw = kwargs.copy()
        kw.update(more_kwargs)
        return func(*(args + more_args), **kw)
    return _partial


def update_wrapper(wrapper, wrapped):
    # Dummy impl
    return wrapper


def wraps(wrapped):
    # Dummy impl
    return lambda x: x

def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value