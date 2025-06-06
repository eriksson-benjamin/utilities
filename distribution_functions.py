# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:36:19 2024

@author: benjer
"""

import numpy as np
import scipy.optimize as optimize


def branin(x1, x2):
    """
    Computes the value of the Branin function, a standard benchmark function
    for optimization problems.

    The Branin function is a two-dimensional function defined by:
    f(x1, x2) = a * (x2 - b * x1**2 + c * x1 - r)**2 + s * (1 - t) * cos(x1) + s

    Parameters
    ----------
    x1 : float
        The first input variable.
    x2 : float
        The second input variable.

    Returns
    -------
    float
        The computed value of the Branin function for the given inputs.

    Notes
    -----
    The Branin function has three global minima:
        - At approximately (x1, x2) = (-π, 12.275), (π, 2.275), and
          (9.42478, 2.475).
        - with a function value of 0.3979
    The function is commonly used for testing optimization algorithms and is
    typically evaluated for x1 = [-5.0, 10.0], and x2 = [0.0, 15.0].
    """    
    a = 1
    b = 5.1 / (4 * np.pi**2)
    c = 5 / np.pi
    r = 6
    s = 10
    t = 1 / (8 * np.pi)
    
    f = a * (x2 - b * x1**2 + c * x1 - r)**2 + s * (1 - t) * np.cos(x1) + s

    return f


def goldstein_price(x1, x2):
    """
    Computes the value of the Goldstein-Price function, a standard benchmark
    function for optimization problems.

    The Goldstein-Price function is a two-dimensional function defined by:
    f(x1, x2) = (1 + (a^2) * b) * (30 + (c^2) * d)

    where:
        a = x1 + x2 + 1.0
        b = 19.0 - 14.0 * x1 + 3.0 * x1^2 - 14.0 * x2 + 6.0 * x1 * x2 + 3.0 * x2^2
        c = 2.0 * x1 - 3.0 * x2
        d = 18.0 - 32.0 * x1 + 12.0 * x1^2 + 48.0 * x2 - 36.0 * x1 * x2 + 27.0 * x2^2

    Parameters
    ----------
    x1 : float
        The first input variable.
    x2 : float
        The second input variable.

    Returns
    -------
    float
        The computed value of the Goldstein-Price function for the given inputs.

    Notes
    -----
    The Goldstein-Price function has a global minimum with a value of 3.0 at
    (x1, x2) = (0, -1). The function is typically evaluated for x1, x2 in the
    range [-2, 2].
    """
    a = x1 + x2 + 1.0
    b = (19.0 - 14.0 * x1 + 3.0 * x1 * x1 - 14.0 * x2
         + 6.0 * x1 * x2 + 3.0 * x2 * x2)
    c = 2.0 * x1 - 3.0 * x2
    d = (18.0 - 32.0 * x1 + 12.0 * x1 * x1 + 48.0 * x2
         - 36.0 * x1 * x2 + 27.0 * x2 * x2)
      
    f = (1.0 + a * a * b) * (30.0 + c * c * d)
    
    return f


def sphere(x):
    """
    Computes the value of the Sphere function, a standard benchmark function
    for optimization problems.

    The Sphere function is a multidimensional function defined by:
    f(x) = sum(x_i^2) for i = 1, ..., n

    where 'x' is a vector of inputs, and 'n' is the dimensionality of the
    input space.

    Parameters
    ----------
    x : array-like
        An array of input variables. Can be of any dimension.

    Returns
    -------
    float
        The computed value of the Sphere function for the given inputs.

    Notes
    -----
        - The Sphere function has a global minimum at x = [0, ..., 0], where
          f(x) = 0.
        - It is a convex function, making it simple and commonly used for
          testing optimization algorithms.
        - The function is typically evaluated in the range [-5.12, 5.12] for
          all dimensions of 'x'.

    """
    f = np.sum(np.power(x, 2))
    
    return f


def eggbox_loglikelihood(theta_1, theta_2):
    """
    Computes the log value of the Eggbox likelihood function, often used in 
    Bayesian analysis and optimization problems.

    The Eggbox likelihood function is defined as:
    f(theta_1, theta_2) = [exp(2 + cos(theta_1 / 2) * cos(theta_2 / 2))]^5

    Parameters
    ----------
    theta_1 : float
        The first input parameter. Typically sampled in the range [0, 10π].
    theta_2 : float
        The second input parameter. Typically sampled in the range [0, 10π].

    Returns
    -------
    float
        The computed log value of the Eggbox likelihood function for the given inputs.

    Notes
    -----
    - The Eggbox likelihood function exhibits a highly oscillatory surface with
      multiple peaks and troughs.
    - It is often used to test the performance of Bayesian inference methods 
      and optimization algorithms in challenging landscapes.
    """
    f = np.exp(2 + np.cos(theta_1 / 2) * np.cos(theta_2 / 2))**5
    
    return np.log(f)
    
    

    