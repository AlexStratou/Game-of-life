# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 16:13:21 2024
Author: Alexandros Stratoudakis
e-mail: alexstrat4@gmail.com

"""

import numpy as np


def is_iter(a: object):
    try:
        iter(a)
    except:
        return False
    else:
        return True


def pad_to_shape(arr: np.ndarray, new_shape: tuple):

    pad_height_1 = int(np.ceil((new_shape[0] - arr.shape[0]) / 2))
    pad_height_2 = int(np.floor((new_shape[0] - arr.shape[0]) / 2))
    pad_width_1 = int(np.ceil((new_shape[1] - arr.shape[1]) / 2))
    pad_width_2 = int(np.floor((new_shape[1] - arr.shape[1]) / 2))
    padded_arr = np.pad(arr, pad_width=((pad_height_1, pad_height_2),
                        (pad_width_1, pad_width_2)), mode='constant', constant_values=0)

    return padded_arr


