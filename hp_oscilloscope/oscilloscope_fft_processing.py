from typing import List, Optional, Union, Dict
from math import sqrt, pow, log

import numpy
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.animation import FuncAnimation, PillowWriter    # noqa
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.lines import Line2D
from matplotlib.spines import Spine

from .bin_data_file_2 import bin_data


def norm(z: complex):
    return sqrt(pow(z.real, 2) + pow(z.imag, 2))


def select_waveform_from_txt():
    import ast
    with open('digitized_and_aquired.txt', 'r') as bytestream_:
        l = bytestream_.readline()
        pseudo_pointlist: bytearray = ast.literal_eval(l)
        pseudo_pointlist = pseudo_pointlist[10:-2]
        # waveform = numpy.ndarray([len(ll)], numpy.int, , 120)


# 5 lines of documentation for single line of code...
def rgb_to_matlab(r, g, b) -> list | tuple:
    """
    converts regular intensity representation to MATLAB-like format, handled by matplotlib
    :param r: 0-255 red color intensity representation
    :param g: 0-255 green color intensity representation
    :param b: 0-255 blue color intensity representation
    :return: fraction format according to MATLAB format
    """
    return r/255., g/255., b/255.


# final animation, the animation that displays FFT transform as a function of time itself
# FFT is performed on data captured in a specific time-window that advances frame-by-frame
plt.rcParams['font.family'] = 'monospace'


class FFTAnimation:
    """
    Animates the FFT of the oscilloscope signal, with respect to moving time interval
    """
    OSCILLOSCOPE_GREEN = rgb_to_matlab(4, 222, 14)
    OSCILLOSCOPE_DIM = rgb_to_matlab(4, 147, 14)
    OSCILLOSCOPE_NEARBLACK = rgb_to_matlab(3, 9, 3)
    WINDOW_RED = rgb_to_matlab(252, 43, 43)

    def __init__(
        self, data_x: Union[list, np.ndarray], data_y: Union[list, np.ndarray], fps: int = 60,
        total_time: int = 10, split_factor: int = 2, autoscale_limits=False
    ):
        if len(data_x) != len(data_y):
            raise ValueError('size of data lists is mismatched')
        self.animation_figure: Figure = plt.figure(
            num=99, constrained_layout=True, figsize=(15., 9.), edgecolor=self.OSCILLOSCOPE_GREEN,
            facecolor=self.OSCILLOSCOPE_NEARBLACK,
        )
        # adjust the layout of the "master subplot" that will then be the host for the mosaic
        # this generates userwarning with disabling constraint layout
        self.animation_figure.subplots_adjust(
            left=0.05, right=0.943, bottom=0.063, top=0.904
        )

        self.split_factor = split_factor
        self.autoscale_limits = autoscale_limits
        self.animation_figure.suptitle('ANIMATED FFT', color=self.OSCILLOSCOPE_GREEN)
        self.fps = fps
        self.X = np.array(data_x)
        self.Y = np.array(data_y)
        self.d_t = self.X[1] - self.X[0]
        self.fft_data: List[np.ndarray] = []
        self.frequency_data: List[list] = []
        self.time_window_data: List[dict] = []
        self.chart_scales: List[List[float]] = []
        self.time_window_span = int(len(self.X)/self.split_factor)
        self.time_window_step = (len(self.X)-self.time_window_span)/(fps*total_time)
        self.frame_info = [
            [i, int(i*self.time_window_step)] for i in range(fps*total_time)
        ]
        self.fft_freq_bounds = np.fft.fftfreq(self.time_window_span, d=self.d_t)
        self.anim: Optional[FuncAnimation] = None
        self.axes_dict: Optional[Dict[str, Axes]] = None
        # typehint to Dict has to cover the type of the key (in this case "str")
        # and the type of the item (in this case it is list of lists of Line2D's)
        self.lines: Optional[Dict[str, List[List[Line2D]]]] = {}
        self.interval = int(1000. / self.fps)

    def prepare_interval(self, frame: List[int]):
        """
        limit data to certain interval and save the points to be
        represented as bound on the main chart
        :param frame: set of pointers that is used for each frame to get specific data from
            either X/Y tables or to access other records
        """
        # calculate the points of red bars representing time-window that is being
        # processed in the given frame

        frame_index, data_index = frame
        vert_line_offset = 0.1
        x_start_index = data_index
        x_end_index = x_start_index + self.time_window_span
        # print(frame, x_start_index, x_end_index, self.time_window_step, self.time_window_span)
        x_end = self.X[x_end_index]
        x_start = self.X[x_start_index]
        # guard case, in case we will land out of bounds
        if x_end >= len(self.X):
            return

        # here we take 'plot()'s argument order to zip arguments of 'left' and 'right'
        # into points that will form window lines
        interval_on_frame = {
            'left': [[x_start, x_start],
                     [max(self.Y)+vert_line_offset*max(self.Y),
                      min(self.Y)-abs(vert_line_offset*min(self.Y))]],
            'right': [[x_end, x_end],
                      [max(self.Y)+vert_line_offset*max(self.Y),
                       min(self.Y)-abs(vert_line_offset*min(self.Y))]],
            'first': x_start_index,
            'last': x_end_index,
        }
        self.time_window_data.append(interval_on_frame)

    def calculate_fft(self):
        """
        calculate fft component, and it's freq representation to be displayed on one of the charts
        do it for single frame of animation
        """
        # as we step through the time, we create the sample in the previous function,
        # thus we can always take the last appended element from time_window_data as current frame
        frame_interval = self.time_window_data[-1]
        waveform_ = self.Y[frame_interval['first']:frame_interval['last']]
        f_out: Union[np.ndarray, List[complex]] = numpy.fft.fft(waveform_, len(waveform_))
        normalized = [log(norm(z), 10)*10 for z in f_out]
        self.frequency_data.append(normalized)
        real = [z.real for z in f_out]
        imag = [z.imag for z in f_out]
        self.fft_data.append(np.array([real, imag]))

    def move_window(self, frame: List[int]):
        """
        set new red bars to depict new frame of interest
        :param frame: set of pointers that is used for each frame to get specific data from
            either X/Y tables or to access other records
        """
        # print(self.lines["TOP"][1][0])
        # raise
        frame_index, data_index = frame
        self.lines["TOP"][1][0].set_data(
            self.time_window_data[frame_index]["left"][0],
            self.time_window_data[frame_index]["left"][1])
        self.lines["TOP"][2][0].set_data(
            self.time_window_data[frame_index]["right"][0],
            self.time_window_data[frame_index]["right"][1])

    def move_fft(self, frame_):
        """
        move points in FFT scatter-plot and rescale charts to properly show data
        """
        frame_index, data_index = frame_
        x_margin = 0.05
        y_margin = 0.1
        freq_limit = int(len(self.fft_freq_bounds)/4)
        # if frame_index % 30 == 0:
        #     print(len(self.frequency_data[frame_index]), len(self.fft_freq_bounds))
        #     print(self.frequency_data[frame_index][:freq_limit])
        #     print(self.fft_freq_bounds[:freq_limit])
        try:
            self.lines["LEFT"][0][0].set_data(
                self.fft_freq_bounds[:freq_limit],
                self.frequency_data[frame_index][:freq_limit],
            )
            self.lines["RIGHT"][0][0].set_data(
                self.fft_data[frame_index][0], self.fft_data[frame_index][1]
            )
        except IndexError:
            print(len(self.frame_info), frame_index)
            return

        if self.autoscale_limits:
            # set new limits for frequency viewer
            self.axes_dict["LEFT"].set_xlim(
                min(self.fft_freq_bounds[:freq_limit])-abs(
                    x_margin*min(self.fft_freq_bounds[:freq_limit])),
                max(self.fft_freq_bounds[:freq_limit])+abs(
                    x_margin*max(self.fft_freq_bounds[:freq_limit]))
            )
            self.axes_dict["LEFT"].set_ylim(
                min(self.frequency_data[frame_index])-abs(
                    y_margin*min(self.frequency_data[frame_index])),  # bot
                max(self.frequency_data[frame_index])+abs(
                    y_margin*max(self.frequency_data[frame_index]))  # top
            )

            # set new limits for raw fft viewer
            self.axes_dict["RIGHT"].set_xlim(
                min(self.fft_data[frame_index][0])-abs(x_margin*min(self.fft_data[frame_index][0])),
                max(self.fft_data[frame_index][0])+abs(x_margin*max(self.fft_data[frame_index][0])))
            self.axes_dict["RIGHT"].set_ylim(
                min(self.fft_data[frame_index][1])-abs(y_margin*min(self.fft_data[frame_index][1])),
                max(self.fft_data[frame_index][1])+abs(y_margin*max(self.fft_data[frame_index][1])))

    def prescale_charts(self):
        """
        find the acceptable global minima and maxima for the data that will be
        presented in the figure throughout the animation, and set them in stone for the
        entire rendering process
        """
        freq_limit = int(len(self.fft_freq_bounds)/4)
        reference_level = -11
        # now in dB, a bit lower than 10 to move it away from '0.00' from 'frequency' axis

        # find maxima and minima
        time_min = min(self.X)
        time_max = max(self.X)
        time_min = time_min - abs(0.02*(time_max-time_min))
        time_max = time_max + abs(0.02*(time_max-time_min))
        fft_min_re = min([np.min(fft_frame_data[0]) for fft_frame_data in self.fft_data])
        fft_min_im = min([np.min(fft_frame_data[1]) for fft_frame_data in self.fft_data])
        fft_max_re = max([np.max(fft_frame_data[0]) for fft_frame_data in self.fft_data])
        fft_max_im = max([np.max(fft_frame_data[1]) for fft_frame_data in self.fft_data])
        freq_max = max([np.max(freq_data) for freq_data in self.frequency_data])
        freq_min = min([np.min(freq_data) for freq_data in self.frequency_data])

        # set subplot's minima and maxima, first for signal in time domain,
        # then in freq. viewer, and finally for IM/RE fft chart
        self.axes_dict["TOP"].set_xlim(time_min, time_max)
        self.axes_dict["LEFT"].set_xlim(
            min(self.fft_freq_bounds[:freq_limit]),
            max(self.fft_freq_bounds[:freq_limit])
        )
        self.axes_dict["LEFT"].set_ylim(reference_level, freq_max)
        self.axes_dict["RIGHT"].set_xlim(fft_min_re, fft_max_re)
        self.axes_dict["RIGHT"].set_ylim(fft_min_im, fft_max_im)

    def prepare_charts(self, dry_run=False):
        """
        prepare chart space and layout for the animation to be played
        """
        self.animation_figure.clear()

        # mosaic to span top chart 2 columns wide, and rest have their own space
        # also with chart titles
        mosaic = [
            ["TOP", "TOP"],
            ["LEFT", "RIGHT"]
        ]
        plot_titles = ['SIGNAL IN TIME DOMAIN', 'SIGNAL POWER DISTRIBUTION', 'RAW FFT']

        # to color all the axes spines, we can do the following
        # plt.rc('axes', edgecolor=self.OSCILLOSCOPE_DIM)

        self.animation_figure.suptitle('ANIMATED FFT', color=self.OSCILLOSCOPE_GREEN)
        self.prepare_interval([0, 0])
        self.axes_dict = self.animation_figure.subplot_mosaic(
            mosaic, subplot_kw={'facecolor': self.OSCILLOSCOPE_NEARBLACK},
            gridspec_kw={'wspace': 0.16, 'hspace': 0.245,}
        )
        self.axes_dict: Dict[str, Axes]

        # if you have ever wondered how are the edges/axis of subplots called in matplotlib,
        # they are called "spines", we color them green here, as well as the single lines
        spines = ['bottom', 'top', 'left', 'right']
        for axes_item, plot_title in zip(self.axes_dict.items(), plot_titles):
            placement, ax = axes_item
            ax: Axes
            ax.tick_params(
                labelcolor=self.OSCILLOSCOPE_GREEN, color=self.OSCILLOSCOPE_DIM,
                direction='in', length=8
            )
            ax.set_title(plot_title, color=self.OSCILLOSCOPE_GREEN)
            ax.spines: Dict[str, Spine]  # noqa
            for spine in spines:
                ax.spines[spine].set_color(self.OSCILLOSCOPE_DIM)

        # another way to color ticks in the charts
        # for x_tickline in ax.get_xticklines():
        #     x_tickline.set_color(self.OSCILLOSCOPE_DIM)
        # for y_tickline in ax.get_yticklines():
        #     y_tickline.set_color(self.OSCILLOSCOPE_DIM)

        # top with signal + moving window
        # print(self.axes_dict["TOP"].get_position())
        self.lines["TOP"] = []
        self.lines["TOP"].append(self.axes_dict["TOP"].plot(  # the main plot
            self.X, self.Y, color=rgb_to_matlab(100, 255, 200)))
        self.lines["TOP"].append(self.axes_dict["TOP"].plot(  # left line of the time window
            self.time_window_data[-1]["left"][0], self.time_window_data[-1]["left"][1],
            color=self.WINDOW_RED, marker='None',
        ))
        self.lines["TOP"].append(self.axes_dict["TOP"].plot(  # right line of the time window
            self.time_window_data[-1]["right"][0], self.time_window_data[-1]["right"][1],
            color=self.WINDOW_RED, marker="None",
        ))
        self.axes_dict["TOP"].set_xlabel("time [s]", color=self.OSCILLOSCOPE_GREEN)
        self.axes_dict["TOP"].set_ylabel("Voltage [V]", color=self.OSCILLOSCOPE_GREEN)

        # bottom part with left/right to draw ffts and frequency responses
        self.lines["LEFT"] = []
        self.lines["LEFT"].append(self.axes_dict["LEFT"].plot(
            [1, 2, 3], color=self.OSCILLOSCOPE_GREEN))
        self.axes_dict["LEFT"].set_xlabel(
            "Frequency [MHz]", color=self.OSCILLOSCOPE_GREEN)
        self.axes_dict["LEFT"].set_ylabel(
            "Signal power [dB]", color=self.OSCILLOSCOPE_GREEN)
        self.lines["RIGHT"] = []
        self.lines["RIGHT"].append(self.axes_dict["RIGHT"].plot(
            [1, 2, 3], [1, 2, 3], color=self.OSCILLOSCOPE_GREEN,
            linestyle='', marker='o', markersize=3))
        self.axes_dict["RIGHT"].set_xlabel("RE", color=self.OSCILLOSCOPE_GREEN)
        self.axes_dict["RIGHT"].set_ylabel("IM", color=self.OSCILLOSCOPE_GREEN)
        # print(self.lines)
        if not self.autoscale_limits and not dry_run:
            self.prescale_charts()
        self.time_window_data.pop()

    def pre_calculate_frames(self):
        """
        calculate all the data needed for each frame to render, separate for each chart
        to be drawn in the canvas, if there are more than one.
        """
        for frame_data in self.frame_info:
            self.prepare_interval(frame_data)
            self.calculate_fft()

    def init_animation(self):
        """
        set the initial frame of the animation
        """
        self.prepare_interval([0, 0])
        self.move_window([0, 0])
        self.move_fft([0, 0])

    def animate(self, frame: List[int]):
        """
        animate charts by replacing the data each frame with precomputed values
        """
        self.prepare_interval(frame)
        self.move_window(frame)
        self.move_fft(frame)

    def generate_frame_images(self):
        """
        generate images that can be assembled into mp4 file with an external program like the
        ffmpeg library
        """
        self.pre_calculate_frames()
        self.prepare_charts()
        for frame_data in self.frame_info:
            self.prepare_interval(frame_data)
            self.move_window(frame_data)
            self.move_fft(frame_data)
            # format='png'<- format is dictated by
            # the extension passed in the filename
            plt.savefig(fname=f'rendered_frames/movie1/FFT_frame_{frame_data[0]}.png', dpi=200)

    def create_animation(self):
        """
        create the animation object used to show figures and used to save animation to the file
        """
        self.pre_calculate_frames()
        self.prepare_charts()
        self.anim: FuncAnimation = animation.FuncAnimation(
            fig=self.animation_figure, func=self.animate,
            frames=self.frame_info[1:], init_func=self.init_animation,  # noqa
            interval=self.interval, repeat_delay=1000
        )
        movie_writer = PillowWriter(fps=60)
        self.anim.save('FFT_v1_0.gif', dpi=100, writer=movie_writer)  # noqa


if __name__ == '__main__':
    pseudo_pointlist: bytearray = bytearray([int(b) for b in bin_data])
    pseudo_pointlist = pseudo_pointlist[10:-1]

    waveform = numpy.array([float(b) for b in pseudo_pointlist])
    x = numpy.array(list([float(i) for i in range(len(pseudo_pointlist))]))

    # sophisticated fft animation
    fft_anim = FFTAnimation(x, waveform, fps=120)
    fft_anim.prepare_charts(dry_run=True)
    fft_anim.generate_frame_images()
    # fft_anim.create_animation()
    # plt.show()
