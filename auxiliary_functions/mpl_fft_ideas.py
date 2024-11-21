from typing import List
from math import sqrt, pow, log
from copy import deepcopy

import numpy
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.animation import FuncAnimation, PillowWriter    # noqa
from matplotlib.axes import Axes
from matplotlib.figure import Figure, SubFigure


from .bin_data_file_1 import bin_data


def norm(z: complex):
    return sqrt(pow(z.real, 2) + pow(z.imag, 2))


# initialization for the use in simple animations
arr = numpy.array([[1, 2, 3], [4, 5, 6]])
arr2 = numpy.ndarray([15, 15], numpy.float64)
arr2[::2, ::2] = 0

pseudo_pointlist: bytearray = bytearray([int(b) for b in bin_data])
pseudo_pointlist = pseudo_pointlist[10:-1]

waveform = numpy.array([float(b) for b in pseudo_pointlist])
x = numpy.array(list([float(i) for i in range(len(pseudo_pointlist))]))
pruned = deepcopy(waveform)
pruned[:850] = 120.
# waveform.dtype = numpy.int
print(waveform.shape, waveform.dtype, waveform.base)
print(x.shape, x.dtype, x.base)
print(waveform)

num_samples = 4000
total_recorded_timewindow = 0.0005  # in seconds
timebase_divisor = total_recorded_timewindow/num_samples

waveform[:] -= 120
pruned[:] -= 120
waveform[:] /= 120
pruned[:] /= 120
# x[:] /= timebase_divisor  # div by 1 milion = miliseconds (from 'range' perspective)
x[:] *= timebase_divisor  # "div" by 1 milion = miliseconds (from 'range' perspective)

f = numpy.fft.rfft(waveform, len(waveform))
normalized_fft = [log(norm(z), 10)*10 for z in f]
pruned_f = numpy.fft.rfft(pruned, len(pruned))
normalized_pruned_fft = [log(norm(z), 10)*10 for z in pruned_f]

fft_diff = [(a - b) for a, b in zip(normalized_fft, normalized_pruned_fft)]
# freq_content = numpy.fft.fftfreq(len(x), d=1/timebase_divisor)
freq_content = numpy.fft.fftfreq(len(x), d=timebase_divisor)
X = [z.real for z in f]
Y = [z.imag for z in f]
print(waveform)

figure, axes = plt.subplots(3, 2)
axes: List[List[Axes]]
axes2: Axes
figure: Figure
anim: animation.Animation

# axes[1].plot(freq_content[:int(len(freq_content)/16)], normalized_fft[:int(len(freq_content)/16)])
# axes[1].set_xlabel('frequency')
axes[0][0].plot(x, waveform)
axes[1][0].plot(x, pruned)
axes[0][1].plot(
    freq_content[:int(len(freq_content)/4)], normalized_fft[:int(len(freq_content)/4)])
axes[1][1].plot(
    freq_content[:int(len(freq_content)/4)], normalized_pruned_fft[:int(len(freq_content)/4)])
axes[0][1].set_xlabel('frequency')
axes[1][1].set_xlabel('frequency')
axes[0][1].grid(True, linestyle='-.')
axes[1][1].grid(True, linestyle='-.')
axes[0][1].tick_params(labelcolor='b', labelsize='medium', width=3)
axes[1][1].tick_params(labelcolor='b', labelsize='medium', width=3)
axes[2][0].plot(freq_content[:int(len(freq_content)/4)], fft_diff[:int(len(freq_content)/4)])
plt.show()

figure2, axes2 = plt.subplots()
figure2: Figure
axes2: Axes
figure2.set(constrained_layout=True)
figure2.set_figwidth(8)
figure2.set_figheight(6)
axes2.scatter(X, Y)
axes2.set_xlabel('Re')
axes2.set_ylabel('Im')
plt.show()



def subfigure_split():
    """
    showcase of the idea on how to generate a plot that split main
    figure into Subfigure instances
    """
    # split figure into subfigures
    figure3: Figure = plt.figure(constrained_layout=True, figsize=(12., 9.))
    subfigures: List[SubFigure] = figure3.subfigures(
        nrows=2, ncols=1, hspace=0.05, height_ratios=[2./3., 1./3.])

    # subfigure 1 - 2x2 subaxes space:
    subaxes1 = subfigures[0].subplots(nrows=2, ncols=2)
    subfigures[0].suptitle('signal and it\'s FFT')
    subaxes1: List[List[Axes]]

    subaxes1[0][0].plot(x, waveform, color='y')
    subaxes1[1][0].plot(x, pruned, color='g')
    subaxes1[0][1].plot(
        freq_content[:int(len(freq_content)/16)],
        normalized_fft[:int(len(freq_content)/16)],
        color='y'
    )
    subaxes1[1][1].plot(
        freq_content[:int(len(freq_content)/16)],
        normalized_pruned_fft[:int(len(freq_content)/16)],
        color='g'
    )
    subaxes1[0][1].set_xlabel('frequency')
    subaxes1[1][1].set_xlabel('frequency')
    subaxes1[0][0].set_xlabel('time')
    subaxes1[1][0].set_xlabel('time')
    subaxes1[0][1].grid(True, linestyle='-.')
    subaxes1[1][1].grid(True, linestyle='-.')
    subaxes1[0][1].tick_params(labelcolor='b', labelsize='medium', width=3)
    subaxes1[1][1].tick_params(labelcolor='b', labelsize='medium', width=3)

    # subfigure 2: only the diff of the FFT components
    subaxes2 = subfigures[1].subplots(1, 1)
    subfigures[1].suptitle('difference between FFT\'s')
    subaxes2: Axes

    subaxes2.plot(
        freq_content[:int(len(freq_content)/8)],
        fft_diff[:int(len(freq_content)/8)])
    subaxes2.plot(
        freq_content[:int(len(freq_content)/8)],
        normalized_fft[:int(len(freq_content)/8)])
    subaxes2.plot(
        freq_content[:int(len(freq_content)/8)],
        normalized_pruned_fft[:int(len(freq_content)/8)])
    subaxes2.set_xlabel('frequency')
    plt.show()


