# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 16:09:45 2024
Author: Alexandros Stratoudakis
e-mail: alexstrat4@gmail.com

"""
from life_source import Life
if __name__ == '__main__':

    L = Life(N_grid=100, seed=42)
    L.N_generations(2000)
    anim = L.animate(save = True, name = 'test')