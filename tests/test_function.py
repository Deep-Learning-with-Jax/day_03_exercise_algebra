"""Test the python function from src."""
import numpy as np

from src.matrix_multiply import my_multiply


def test_function() -> None:
    """See if the implementation produces the same result as np.matmul ."""
    matrix1 = np.random.randint(0, 10, (9, 10))
    matrix2 = np.random.randint(0, 10, (10, 9))
    assert np.allclose(matrix1 @ matrix2, my_multiply(matrix1, matrix2))
