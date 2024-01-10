#!/usr/bin/python3
"""Defines a function for multiplying matrix using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the matrix multiplication for the m_a and m_b

    Args:
        m_a (list of lists of ints/floats): The first matrix to be multiplied
        m_b (list of lists of ints/floats): The second matrix to be multiplied
    """

    return (np.matmul(m_a, m_b))
