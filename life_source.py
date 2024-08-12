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

mpl.rc('font', **{'family': 'serif', 'serif': ['Times New Roman']})
mpl.rcParams['font.size'] = 18


class Life:
    """
    Class implementation of the Life game with the classic rules.
    """

    def __init__(self, n_grid: int = 100, seed: int | list | np.ndarray = 42):
        """
        Initializer function of the Life class.

        Args:
            n_grid (int, optional): Grid parameter. The grid will be n_grid**2 in size. Defaults to 100.
            seed (int | list | np.ndarray, optional): Initial condition. If provided with a specific array, the array
            will be resized and used as the IC. Defaults to 42.

        Raises:
            ValueError: If the input is not an n_grid x n_grid array or an integer.

        Returns:
            None.

        """
        self.generation = 0
        self.N_grid = n_grid

        if utils.is_iter(seed):
            seed = np.array(seed)
            self.current_gen = utils.pad_to_shape(
                arr=seed, new_shape=(self.N_grid, self.N_grid))

        elif isinstance(seed, int) and seed >= 0:
            # if seed is an int make a np.random array from that seed
            np.random.seed(seed)
            self.current_gen = np.random.randint(0, 2, size=(n_grid, n_grid))
        else:
            # else raise an error
            raise ValueError(
                'The seed must be a n_grid x n_grid array or a non-negative integer')

        self.population = self.current_gen.sum()
        self.history = [
            [np.copy(self.current_gen), self.generation, self.population]]
        self.p = lambda idx: utils.pidx(
            idx=idx, max_idx=self.N_grid - 1)  # periodic BC index function

    def plot_gen(self):
        """
        Plot the current state of the simulation.

        Returns:
            None.

        """

        plt.imshow(self.current_gen.T, cmap='binary')
        plt.title('Generation: ' + str(self.generation) +
                  ' ,      Population: ' + str(self.population))

    def next_generation(self):
        """
        Evolve the simulation by one generation

        Returns:
            None.

        """
        tmp = np.copy(self.current_gen)
        # note that there are periodic BC
        for i in range(self.current_gen.shape[0]):
            for j in range(self.current_gen.shape[1]):
                NN = tmp[self.p(i - 1), self.p(j - 1)] + tmp[self.p(i - 1), self.p(j)] + tmp[
                    self.p(i - 1), self.p(j + 1)] \
                     + tmp[self.p(i), self.p(j + 1)] + tmp[self.p(i), self.p(j - 1)] \
                     + tmp[self.p(i + 1), self.p(j - 1)] + tmp[self.p(i + 1), self.p(j)] + tmp[
                         self.p(i + 1), self.p(j + 1)]
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

        self.population = self.current_gen.sum(dtype=int)
        self.generation += 1
        self.history.append(
            [np.copy(self.current_gen), self.generation, self.population])

    def n_generations(self, n: int = 100):
        """
        Evolve n generations.

        Args:
            n (int, optional): How many generations to advance. Defaults to 100.

        Returns:
            None.

        """
        print('Running for ' + str(n) + ' generations...', end='')
        for i in range(n):
            self.next_generation()
        print('Done!')

    def animate(self, save: bool = False, name: str = None, **kwargs) -> animation.FuncAnimation:
        """
        Animate the history of the simulation.

        Args:
            save (bool, optional): Save option for the animation. Defaults to False.
            name (str, optional): Name of the saved animation. Defaults to None.
            **kwargs: Keyword arguments for animation.FFMpegWriter

        Returns:
           animation.FuncAnimation: The resulting animation.

        """
        print('Animating...', end='')
        fig, ax = plt.subplots()
        # Set up the formatting for the movie files
        lines = ax.imshow(self.history[0][0], cmap='binary')

        # Set up the function that will be called on each frame
        def update(num: int) -> lines:
            # Update the data being plotted
            ax.set_title(
                'Generation: ' + str(self.history[num][1]) + ' ,      Population: ' + str(self.history[num][2]))
            lines.set_data(self.history[num][0])

            return lines

        ani = animation.FuncAnimation(fig, update, frames=range(
            len(self.history) - 1), interval=20)
        print('Done!')
        if save:
            print('Saving...', end='')
            writervideo = animation.FFMpegWriter(**kwargs)
            ani.save(name + '.mp4', writer=writervideo)
            print('Done!')
        return ani
