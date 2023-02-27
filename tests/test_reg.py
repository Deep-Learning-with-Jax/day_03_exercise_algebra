"""Test the polynomial matrix."""

import numpy as np

from src.regularization import set_up_point_matrix

# import pytest


def test_point_matrix():
    """Test the polynomial point-matrix."""
    points = 3
    len_b = 3
    axis = np.linspace(0, 1, points)
    mat_a = set_up_point_matrix(axis, len_b)
    assert np.allclose(
        mat_a, np.array([[1.0, 0.0, 0.0], [1.0, 0.5, 0.25], [1.0, 1.0, 1.0]])
    )
