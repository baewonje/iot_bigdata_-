# !/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# simple_data = [1,2,3,4,5,6,7,8,9,10]
simple_data = [3,12,15,16,16,17,19,34]
box_plot_data = [simple_data]

fig = plt.figure()
axl = fig.add_subplot(1,1,1)

box_labels = ['s1']
axl.boxplot(box_plot_data,notch=False,sym='.',vert=True,whis=1.5,showmeans=True,labels=box_labels)
axl.xaxis.set_ticks_position('bottom')
axl.yaxis.set_ticks_position('left')
axl.set_title('Box Plots: Resampling of Two Distributions')
axl.set_xlabel('Distribution')
axl.set_ylabel('Value')

plt.show()
