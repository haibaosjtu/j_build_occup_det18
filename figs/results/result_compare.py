#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', family='serif')
rc('text', usetex=True)

accuracy = [

        ('$\mathrm{RNN_1}$', 0.79),
        ('$\mathrm{RNN_2}$', 0.976),
        ('$\mathrm{RNN_3}$', 0.9929),
        ('$\mathrm{RNN_1^H}$', 0.9989),
        ('$\mathrm{RNN_2^H}$', 1),
        ('$\mathrm{RNN_3^H}$', 0.9962),

        ('$\mathrm{SVR_4^{100}}$', 0.932),
        ('$\mathrm{SVR_4^{500}}$', 0.9422),
        ('$\mathrm{SVR_4^{1K}}$', 0.9468),
        ('$\mathrm{SVR_5^{100}}$', 0.9736),
        ('$\mathrm{SVR_5^{500}}$', 0.9726),
        ('$\mathrm{SVR_5^{1K}}$', 0.9675),

        ('Dong2014', 0.92)
]

objects = [item[0] for item in accuracy]
heights = [item[1] for item in accuracy]

y_pos = np.arange(len(objects))

plt.figure(figsize=(9, 2)).subplots_adjust(left=0.06, right=0.94, top=0.92, bottom=0.18)

plt.grid(linestyle='--', alpha=0.5, color='black')

plt.bar(y_pos, heights, align='center', color='black')
plt.xticks(y_pos, objects)
plt.ylabel('Detection accuracy')
plt.ylim([0.75, 1.01])

plt.show()
