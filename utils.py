# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 16:13:21 2024
Author: Alexandros Stratoudakis
e-mail: alexstrat4@gmail.com

"""

import numpy as np


def is_iter(arr: object) -> bool:
    """
    Function that returns True if the input is an iterable and false otherwise.

    Args:
        arr (object): Input array

    Returns:
        bool: True if arr is iterable, False if not.

    """

    try:
        iter(arr)
    except:
        return False
    else:
        return True


def pad_to_shape(arr: np.ndarray, new_shape: tuple) -> np.ndarray:
    """
    Function that uses numpy.pad to pad with zeros around the input arr to a given shape.

    Args:
        arr (np.ndarray): Input numpy.ndarray.
        new_shape (tuple): The input array will be padded to this shape.

    Returns:
        padded_arr (np.ndarray): The reshaped, padded array.

    """

    pad_height_1 = int(np.ceil((new_shape[0] - arr.shape[0]) / 2))
    pad_height_2 = int(np.floor((new_shape[0] - arr.shape[0]) / 2))
    pad_width_1 = int(np.ceil((new_shape[1] - arr.shape[1]) / 2))
    pad_width_2 = int(np.floor((new_shape[1] - arr.shape[1]) / 2))
    padded_arr = np.pad(arr, pad_width=((pad_height_1, pad_height_2),
                                        (pad_width_1, pad_width_2)), mode='constant', constant_values=0)

    return padded_arr


def pidx(idx: int, max_idx: int) -> int:
    """
    Function that treats periodic indices. When the  input index exceeds the maximum,
    it is mapped to the appropriate value, starting from the beginning.

    Args:
        idx (int): Input index.
        max_idx (int): Maximum allowed index.

    Returns:
        int: Index, respecting periodicity.

    """

    if idx <= max_idx:
        return idx
    else:
        return idx - max_idx - 1


glider = np.array([
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1]
])

blinker = [[1, 1, 1]]

toad = np.array([[0, 1, 1, 1],
                 [1, 1, 1, 0]])

beacon = np.array([[1, 1, 0, 0],
                   [1, 1, 0, 0],
                   [0, 0, 1, 1],
                   [0, 0, 1, 1]])

lwss = np.array([[1, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 1],
                 [0, 1, 1, 1, 1]
                 ]
                )

r_pentomino = np.array([[0, 1, 1],
                        [1, 1, 0],
                        [0, 1, 0]])
