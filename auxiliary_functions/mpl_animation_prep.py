from typing import List, Optional, Union, Dict
from math import sqrt, pow, log
from copy import deepcopy

import numpy
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.animation import FuncAnimation, PillowWriter    # noqa
from matplotlib.axes import Axes
from matplotlib.artist import Artist
from matplotlib.figure import Figure, SubFigure
from matplotlib.lines import Line2D
from matplotlib.spines import Spine


def rgb_to_matlab(r, g, b):
    return r/255., g/255., b/255.


class SimpleAnimation:
    """
    first animation class, requires external Figure instance to draw animation into.

    it doesn't offer any customisation options at the moment of object creation, and
    renders animation frames by clearing and redrawing entire figure space

    presents adding data point to the chart each frame
    """
    # each frame and re-drawing it afterwords
    def __init__(self, figure_: Figure):
        self.animation_figure = figure_
        self.animation_figure.suptitle('ANIMATED FIGURE')
        self.ax1: Axes = self.animation_figure.add_axes((0.1, 0.05, 0.8, 0.7))

    def init_moving_dots(self):
        """
        initial state of the figure
        """
        self.animation_figure.clear()
        self.animation_figure.suptitle('ANIMATED FIGURE')
        self.ax1: Axes = self.animation_figure.add_axes((0.1, 0.05, 0.8, 0.7))
        frame = 0
        value_x = [0]
        value_y = [(value_x[0]+1)*(value_x[0]*0.2*frame)]
        self.ax1.set_xlim(-0.05, 1.05)
        self.ax1.set_ylim(-0.05, 1.05)
        self.ax1.margins(0.02)
        __ = self.ax1.plot(value_x, value_y, color=rgb_to_matlab(200, 120, 250), marker='o')
        print('no \'comma-equals\' line', __)
        self.animation_figure.show()

    def moving_dots(self, frame: Optional[int]) -> List[Artist]:
        """
        draws figure state for the given frame of animation
        :param frame: int number of frame to be drawn
        """
        self.animation_figure.clear()
        self.animation_figure.suptitle('ANIMATED FIGURE')
        self.ax1: Axes = self.animation_figure.add_axes((0.1, 0.05, 0.8, 0.7))
        # ax1: Axes = args[0]
        if frame:
            if isinstance(frame, int):
                values_x = list(range(frame))
            else:
                raise ValueError
        else:
            values_x = list(range(5))
        values_y = [(i+1)*(i*0.2*frame) for i in values_x]
        # [left, bottom, width, height]
        self.ax1.plot(values_x, values_y, color=rgb_to_matlab(200, 120, 250), marker='o')
        self.animation_figure.show()
        return [self.animation_figure, self.ax1]

    def create_animation(self):
        anim = animation.FuncAnimation(
            fig=self.animation_figure, func=self.moving_dots,
            frames=[_ for _ in range(10)][2:], init_func=self.init_moving_dots,   # noqa
            interval=250, repeat_delay=500
        )
        # fargs=(,),
        # print(anim)
        plt.show()


class SimpleAnimation2:
    """
    another animation, now based on the idea of replacing
    data points in the chart after each frame, with static subplots already drawn
    """
    def __init__(self, figure_: Figure, point_amount: int = 120, fps: int = 60,
                 placement: Optional[List[float]] = None):
        if placement is None:
            placement = [0.07, 0.07, 0.90, 0.85]
        self.animation_figure = figure_
        self.animation_figure.suptitle('ANIMATED CHART')
        self.fps = fps
        self.points = point_amount
        # order: [left, bottom, width, height]
        self.chart_placement = placement
        self.ax1: Axes = self.animation_figure.add_axes(placement)
        self.lines, = self.ax1.plot(
            [], [], color=rgb_to_matlab(200, 120, 250), marker='o')
        self.lines: List[Line2D]
        self.animation_figure.suptitle('ANIMATED FIGURE')
        self.anim: Optional[FuncAnimation] = None
        self.interval = int(1000. / self.fps)
        print('\'comma-equals\' line', self.lines)

    def init_moving_dots(self):
        """
        generate the initial frame of the animation
        """
        values_x = [0]
        # self.lines[:].set_data(numpy.array(values_x),
        #                        numpy.array([(i + 1) * (i * 0.2) for i in values_x]))
        self.lines.set_data(numpy.array(values_x),
                            numpy.array([(i + 1) * (i * 0.2) for i in values_x]))
        self.ax1.set_xlim(-0.05, 1.05)
        self.ax1.set_ylim(-0.05, 1.05)
        # self.lines.set_xdata = numpy.array(values_x)
        # self.lines.set_ydata = numpy.array([(i + 1) * (i * 0.2) for i in values_x])

    def moving_dots(self, frame: Optional[int]):
        """
        generate subsequent frames of the animation, based on the
        :param frame: int representing which frame of the animation is this
        """
        values_x = numpy.array([_ for _ in range(frame)])
        values_y = numpy.array([(i + 1) * (i * 0.2) for i in values_x])
        # self.lines[:].set_data(numpy.array(values_x),
        #                        numpy.array([(i + 1) * (i * 0.2) for i in values_x]))
        self.lines.set_data(values_x, values_y)
        self.ax1.set_xlim(-0.05, values_x[-1]+0.05)
        self.ax1.set_ylim(-0.05, values_y[-1]+0.05)
        # self.lines.set_xdata(numpy.array(values_x))
        # self.lines.set_ydata(numpy.array([(i+1)*(i*0.2) for i in values_x]))

    def create_animation(self):
        self.anim: FuncAnimation = animation.FuncAnimation(
            fig=self.animation_figure, func=self.moving_dots,
            frames=[_ for _ in range(self.points+1)][2:],  # noqa
            init_func=self.init_moving_dots,
            interval=self.interval, repeat_delay=1000
        )
        movie_writer = PillowWriter(fps=self.fps)
        simple_anim2.anim.save('my_movie2.gif', dpi=125, writer=movie_writer)  # noqa


if __name__ == '__main__':
    # first simple animation
    moving_figure: Figure = plt.figure(num=10, constrained_layout=True)  # figsize=[10, 6]
    simple_anim = SimpleAnimation(moving_figure)
    simple_anim.create_animation()

    # simple animation with data substitution and a bit of customisation,
    # for example choosing fps, point amount and such
    # moving_figure2: Figure = plt.figure(num=11, constrained_layout=True, figsize=[10, 6])
    # simple_anim2 = SimpleAnimation2(moving_figure2, fps=24)
    # simple_anim2.create_animation()
    # plt.show()
