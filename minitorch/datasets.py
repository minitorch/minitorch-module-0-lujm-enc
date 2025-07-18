import math
import random
from dataclasses import dataclass
from typing import List, Tuple


def make_pts(N):
    """
    Generate N random 2D points in the unit square.

    Args:
        N (int): Number of points to generate.

    Returns:
        List[Tuple[float, float]]: List of (x, y) points.
    """
    X = []
    for i in range(N):
        x_1 = random.random()
        x_2 = random.random()
        X.append((x_1, x_2))
    return X


@dataclass
class Graph:
    N: int
    X: List[Tuple[float, float]]
    y: List[int]


def simple(N):
    """
    Generate a simple dataset where the label is 1 if x < 0.5, else 0.

    Args:
        N (int): Number of samples.

    Returns:
        Graph: Dataset with features and labels.
    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def diag(N):
    """
    Generate a dataset where the label is 1 if x + y < 0.5, else 0.

    Args:
        N (int): Number of samples.

    Returns:
        Graph: Dataset with features and labels.
    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 + x_2 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def split(N):
    """
    Generate a dataset where the label is 1 if x < 0.2 or x > 0.8, else 0.

    Args:
        N (int): Number of samples.

    Returns:
        Graph: Dataset with features and labels.
    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.2 or x_1 > 0.8 else 0
        y.append(y1)
    return Graph(N, X, y)


def xor(N):
    """
    Generate a dataset where the label is 1 if (x < 0.5 and y > 0.5) or (x > 0.5 and y < 0.5), else 0.

    Args:
        N (int): Number of samples.

    Returns:
        Graph: Dataset with features and labels.
    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.5 and x_2 > 0.5 or x_1 > 0.5 and x_2 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def circle(N):
    """
    Generate a dataset where the label is 1 if the point is outside a circle of radius sqrt(0.1) centered at (0.5, 0.5), else 0.

    Args:
        N (int): Number of samples.

    Returns:
        Graph: Dataset with features and labels.
    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        x1, x2 = x_1 - 0.5, x_2 - 0.5
        y1 = 1 if x1 * x1 + x2 * x2 > 0.1 else 0
        y.append(y1)
    return Graph(N, X, y)


def spiral(N):
    """
    Generate a spiral dataset with two classes in a spiral pattern.

    Args:
        N (int): Number of samples (should be even).

    Returns:
        Graph: Dataset with features and labels.
    """

    def x(t):
        return t * math.cos(t) / 20.0

    def y(t):
        return t * math.sin(t) / 20.0
    X = [(x(10.0 * (float(i) / (N // 2))) + 0.5, y(10.0 * (float(i) / (N //
        2))) + 0.5) for i in range(5 + 0, 5 + N // 2)]
    X = X + [(y(-10.0 * (float(i) / (N // 2))) + 0.5, x(-10.0 * (float(i) /
        (N // 2))) + 0.5) for i in range(5 + 0, 5 + N // 2)]
    y2 = [0] * (N // 2) + [1] * (N // 2)
    return Graph(N, X, y2)


datasets = {'Simple': simple, 'Diag': diag, 'Split': split, 'Xor': xor,
    'Circle': circle, 'Spiral': spiral}
