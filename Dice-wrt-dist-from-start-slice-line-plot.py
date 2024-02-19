'''
This code gives a line plot, for all volumes in a dataset, and shows the change in dice score/ accuracy with respect to the distances from start slice 

Assumes that in the .csv file, each row represents a volume as such - the first column is the volume name/id and the following columns are the ordered dice score of slices 
'''

# PLOT ACCURACT WRT START SLICE IN VOLUME

import csv
from matplotlib import pyplot as plt
import numpy as np


longest_line = 0
furthest_max_pos = 0
start_pos = []
names = []
lines = []

# Find the Longest Volume
with open('BaseInferenceResults/Spleen_S2V_Eval.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        if len(line) > longest_line:
            longest_line = len(line) 

# Pads each volume such that (1)All the start slices are aligned (in my case, the start slice = one with max segmentation) and (2)All volumes are of the same length
with open('BaseInferenceResults/Spleen_S2V_Eval.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        names.append(line[0])
        line = [ele for ele in [float(f"{float(ele):.4f}") for ele in line[1:]] if not np.isnan(ele)]
        #print("Length", len(line), "|||| Pos of Max Dice", line.index(max(line)))
        lines.append(line)
        max_pos = line.index(max(line))
        if max_pos > furthest_max_pos:
            furthest_max_pos = max_pos
        start_pos.append(- max_pos)

fully_nested = [list(zip(range(start_idx, start_idx + len(lst)), lst)) for lst, start_idx in zip(lines, start_pos)]

# Plot
fig, ax = plt.subplots(figsize=(20,10))
for l in fully_nested:
    ax.plot(*zip(*l))
ax.annotate('Start Slice = Largest Annotation in Volume',
            xy=(0, 1.0), xycoords='data',
            xytext=(-10, 90), textcoords='offset points',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='center', verticalalignment='bottom')
#ax.set(xlim=(-furthest_max_pos, longest_line))
ax.set_xlabel("Values")
ax.legend(names, fontsize=7, loc = 'upper left', ncol=5, prop = {'size' : 5})
plt.title("Accuracy w.r.t. Start Slice - SPLEEN Dataset", loc='left', fontsize = 20)
plt.show()



