"""Regularization proof of concept."""
import matplotlib.pyplot as plt
import numpy as np
import pandas


def set_up_point_matrix(axis_x: np.ndarray, degree: int) -> np.ndarray:
    """Set up a point matrix to fit a polynomial.

    The matrix should have to following form:
    [a_1**0       a_1**1      ...  a_1**(degree-1)
     a_2**0       a_2**1      ...  a_2**(degree-1)
     a_3**0       a_3**1      ...  a_3**(degree-1)
     ...          ...         ...  ...
     a_points**0  a_points**1 ...  a_points**(degree-1)]

    Where the entries in the matrix are from the axis_x vector.

    Args:
        axis_x (np.ndarray): The values of the time or x-axis.
        degree (int): The degree of the polynomial.

    Returns:
        np.ndarray: The polynomial point matrix A.
    """
    mat_a = np.zeros((len(axis_x), degree))
    # TODO implement me!
    return mat_a


if __name__ == "__main__":
    b_noise_p = pandas.read_csv("./data/noisy_signal.tab", header=None)
    b_noise = np.asarray(b_noise_p)

    x_axis = np.linspace(0, 1, num=len(b_noise))

    plt.plot(x_axis, b_noise, ".", label="b_noise")
    plt.show()

    # TODO put your code here!
