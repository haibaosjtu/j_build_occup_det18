#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', family='serif')
rc('text', usetex=True)

colors = {'rnn': '#000040', 'svr': '#400040', 'other': '#004000'}

accuracy = [

        ('$\mathrm{RNN_1}$', 0.79, colors['rnn']),
        ('$\mathrm{RNN_2}$', 0.976, colors['rnn']),
        ('$\mathrm{RNN_3}$', 0.9929, colors['rnn']),
        ('$\mathrm{RNN_1^H}$', 0.9989, colors['rnn']),
        ('$\mathrm{RNN_2^H}$', 1, colors['rnn']),
        ('$\mathrm{RNN_3^H}$', 0.9962, colors['rnn']),

        ('$\mathrm{SVR_4^{100}}$', 0.932, colors['svr']),
        ('$\mathrm{SVR_4^{500}}$', 0.9422, colors['svr']),
        ('$\mathrm{SVR_4^{1K}}$', 0.9468, colors['svr']),
        ('$\mathrm{SVR_5^{100}}$', 0.9736, colors['svr']),
        ('$\mathrm{SVR_5^{500}}$', 0.9726, colors['svr']),
        ('$\mathrm{SVR_5^{1K}}$', 0.9675, colors['svr']),

        ('Dong2014', 0.92, colors['other'])
]

objects = [item[0] for item in accuracy]
heights = [item[1] for item in accuracy]

y_pos = np.arange(len(objects))

plt.figure(figsize=(9, 2)).subplots_adjust(left=0.06, right=0.94, top=0.92, bottom=0.18)

plt.grid(linestyle='--', color='gray', zorder=0)

bar_list = plt.bar(y_pos, heights, align='center', width=0.5, zorder=10)

for bar, accu in zip(bar_list, accuracy):
    bar.set_color(accu[2])

plt.xticks(y_pos, objects)
plt.ylabel('Detection accuracy')
plt.ylim([0.75, 1.01])

plt.show()
