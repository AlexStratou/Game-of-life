# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 15:38:52 2024
Author: Alexandros Stratoudakis
e-mail: alexstrat4@gmail.com

"""
import numpy as np
import utils
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation

mpl.rc('font',**{'family':'serif','serif':['Times New Roman']})
mpl.rcParams['font.size']=18


class Life:
    def __init__(self, N_grid: int = 100, seed: int | list | np.ndarray = 42):
        self.generation = 0
        self.N_grid = N_grid

        if utils.is_iter(seed):
            seed = np.array(seed)
            self.current_gen = utils.pad_to_shape(
                arr=seed, new_shape=(self.N_grid, self.N_grid))
            pass
        elif isinstance(seed, int) and seed >= 0:
            # if seed is an int make a np.random array from that seed
            np.random.seed(seed)
            self.current_gen = np.random.randint(0, 2, size=(N_grid, N_grid))
        else:
            # else raise an error
            raise ValueError(
                'The seed must be a N_grid x N_grid array or a non-negative integer')

        self.population = self.current_gen.sum()
        self.history = [[np.copy(self.current_gen),self.generation,self.population]]

    def plot_gen(self):
        
        plt.imshow(self.current_gen.T, cmap='binary')
        plt.set_title('Generation: '+ str(self.generation) + ' ,      Population: ' + str(self.population))

        # TODO add graph options

    def next_generation(self ):
        tmp = np.copy(self.current_gen)
        # note that there are periodic BC
        for i in range(self.current_gen.shape[0] - 1):
            for j in range(self.current_gen.shape[1] - 1):

                NN = tmp[i-1, j-1] + tmp[i-1, j] + tmp[i-1, j+1] + tmp[i, j+1] + tmp[i, j-1] \
                    + tmp[i+1, j-1] + tmp[i+1, j] + tmp[i+1, j+1]
                if NN < 2 and tmp[i, j] == 1:
                    self.current_gen[i, j] = 0
                elif NN <= 3 and tmp[i, j] == 1:
                    # and NN>=2
                    continue
                elif NN > 3 and tmp[i, j] == 1:
                    self.current_gen[i, j] = 0
                elif NN == 3 and tmp[i, j] == 0:
                    self.current_gen[i, j] = 1
                else:
                    continue
        
        self.population = self.current_gen.sum()
        self.generation += 1
        self.history.append([np.copy(self.current_gen), self.generation, self.population])
        
    def N_generations(self, N = 100):
        for i in range(N):
            self.next_generation()
    
    def animate(self, save:bool = False, name:str = None ):
        fig, ax = plt.subplots()
        # Set up the formatting for the movie files
       # Writer = animation.writers['ffmpeg']
        #writer = Writer(fps=60, metadata=dict(artist='Me'))
        lines = ax.imshow(self.history[0][0], cmap = 'binary')
        
        # Set up the function that will be called on each frame
        def update(num):
            # Update the data being plotted
            ax.set_title('Generation: '+ str(self.history[num][1]) + ' ,      Population: ' + str(self.history[num][2]))
            lines.set_data(self.history[num][0])
            
            return lines
        
        ani = animation.FuncAnimation(fig, update, frames=range(len(self.history)-1), interval = 1, repeat=True,)
        if save ==True:
            writervideo = animation.FFMpegWriter(fps=10, bitrate=320) 
            ani.save(name+'.mp4', writer=writervideo) 
        return ani
        


    

