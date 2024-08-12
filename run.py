# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 09:22:32 2024
Author: Alexandros Stratoudakis
e-mail: alexstrat4@gmail.com

"""

from life_source import Life
import utils

# -------Parameters--------------
N_grid = 30
N_generations = 100
init_seed = utils.Seeds.glider
# -------Save-options------------
save = False
save_name = 'animations\\glider'   # do not add file extension
fps = 24
# -------------------------------

if __name__ == '__main__':
    L = Life(n_grid=N_grid, seed=init_seed)
    L.n_generations(n=N_generations)
    anim = L.animate(save=save, name=save_name, fps=fps)
