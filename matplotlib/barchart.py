#!/usr/bin/python3.5
"""
========
Barchart
========

A bar plot with errorbars and height labels on individual bars.
"""
import numpy as np
import matplotlib.pyplot as plt
import csv

#with open('gpu_utility_comparsion.csv', newline='') as csvfile:
#    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
#    for row in spamreader:
#        print(', '.join(row))

distro_utility = (30.64, 29.97, 28.83, 29.76, 29.36, 30.92, 30.67, 30.00)
single_utility = (82.69, 89.63, 85.18, 83.57, 88.80, 85.85, 45.92, 45.12)

ind = np.arange(len(distro_utility))  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(12, 6)) # figsize
rects1 = ax.bar(ind - width/2, distro_utility, width,
                color='SkyBlue', label='Distributed')
rects2 = ax.bar(ind + width/2, single_utility, width,
                color='IndianRed', label='Single')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('GPU Utility')
ax.set_title('Single/Distributed GPU Utility comparison')
ax.set_xticks(ind)
ax.set_xticklabels(('GPU0', 'GPU1', 'GPU2', 'GPU3', 'GPU4', 'GPU5', 'GPU6', 'GPU7'))
ax.legend()

def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


autolabel(rects1, "center")
autolabel(rects2, "center")

plt.savefig('./gpu_utility.png')
plt.show()
