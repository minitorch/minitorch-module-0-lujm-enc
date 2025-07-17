"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$

def mul(x: float, y: float) -> float:
    """Multiply two numbers."""
    return x * y

def id(x: float) -> float:
    return x

def add(x: float, y: float) -> float:
    return x + y

def neg(x: float) -> float:
    return -x

def lt(x: float, y: float) -> float:
    return x < y

def eq(x: float, y: float) -> float:
    return x == y

def max(x: float, y: float) -> float:
    return x if x > y else y

def is_close(x: float, y: float) -> float:
    return abs(x - y) < 1e-2

def sigmoid(x: float) -> float:
    return 1/(1+math.exp(-x)) if x >= 0 else math.exp(x)/(1+math.exp(x))

def relu(x: float) -> float:
    return max(0, x)

def log(x: float) -> float:
    return math.log(x)

def exp(x: float) -> float:
    return math.exp(x)

def inv(x: float) -> float:
    return 1/x

def log_back(x: float, d: float) -> float:
    return d/x

def inv_back(x: float, d: float) -> float:
    return -d / (x**2)

def relu_back(x: float, d: float) -> float:
    return d if x > 0 else 0

# TODO: Implement for Task 0.1.


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce

def map(fn: Callable[[float], float], li: Iterable[float]) -> Iterable[float]:
    return [fn(i) for i in li]

def zipWith(fn: Callable[[float, float], float], xs: Iterable[float], ys: Iterable[float]) -> Iterable[float]: 
    return [fn(x, y) for x, y in zip(xs, ys)]

def reduce(fn: Callable[[float, float], float], li: Iterable[float]):
    li = list(li)
    if not li: return 0
    result = li[0]
    for item in li[1:]:
        result = fn(result, item)
    return result

# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists
def negList(li: Iterable[float]):
    return map(neg, li)

def addLists(li1: Iterable[float], li2: Iterable[float]):
    return zipWith(add, li1, li2)

def sum(li: Iterable[float]):
    return reduce(add, li)

def prod(li: Iterable[float]):
    return reduce(mul, li)

# TODO: Implement for Task 0.3.
