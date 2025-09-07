# src/ poisson.py

"""
Poisson distribution functions

Math:
    PMF: P(X = k) = e^{-lambda} lambda^k / k!  for k = 0,1,2,...
    mean = lambda, var = lambda
"""

from math import exp, factorial, lgamma
import numpy as np

# ---- basic pmf ----
def pmf(k: int, lam: float) -> float:
    """ Plain PMF using factorial """
    if k < 0 or int(k) != k:
        return 0.0
    return exp(-lam) * (lam ** k) / factorial(k)

# ---- cdf via summation -----
def cdf(k: int, lam: float) -> float:
    """CDF = sum_{i = 0}^k pmf(i)"""

    if k < 0:
        return 0.0
    i = np.arange(0, k + 1)

    return float(sum(pmf(int(j), lam) for j in i))

# ---- mean/var ----
def mean_var(lam: float) -> tuple[float, float]:
    """
    Expected value of random variable X

    E[X] = sum_{k = 0}^infinity k * pmf(k, lam)

    For Poisson(lam):
        The mean is E[X] = lam
        The variance is lam

    Hence, returning (lam,lam) is mathematically correct.

    """
    return lam, lam

