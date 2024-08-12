# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 09:22:32 2024
Author: Alexandros Stratoudakis
e-mail: alexstrat4@gmail.com

"""

from life_source import Life
import utils

if __name__ == '__main__':
    L = Life(n_grid=20, seed=utils.glider)
    L.n_generations(100)
    anim = L.animate(save=False, name='animations\\glider')
