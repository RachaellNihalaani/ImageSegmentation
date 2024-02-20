# PLOT ACCURACY/AHD WRT START SLICE IN VOLUME

import csv
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


longest_line = 0
furthest_max_pos = 0
max_s2e = 0

start_pos = []
names = []
lines = []
data= []
data2 = []


with open('file.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        if len(line) > longest_line:
            longest_line = len(line) 
        line = [ele for ele in [float(f"{float(ele):.4f}") for ele in line[1:]] if not np.isnan(ele)]
        #print(line.index(max(line)))
        if line.index(max(line)) > max_s2e:
            max_s2e =  line.index(max(line))
        if (len(line)-line.index(max(line))) > max_s2e:
            max_s2e = len(line)-line.index(max(line))
        
        data.append(line)
    print(longest_line, max_s2e)

for row in data:
    # print(len(row), type(row))
    start_slice = row.index(np.max(row))
    # print("Start slice to beginning", start_slice)
    add_to_start = abs(start_slice - max_s2e )
    # print("Add to beginning ", add_to_start)
    # print("End Slice to Start Slice", abs(len(row)-start_slice))
    add_to_end = abs( max_s2e - abs(len(row)-start_slice))
    # print("Add to end", add_to_end )
    row = [np.nan]*add_to_start + row + [np.nan]*add_to_end
    # print(len(row))
    data2.append(row)


data2 = np.transpose(data2)
print(len(data2))
not_nan = []
for i in data2:
    not_nan.append(np.count_nonzero(~np.isnan(i)))
    
# Convert the nested list into a long-format DataFrame
data3 = {'Slice': [], 'Dice': []}
for i, lst in enumerate(data2):
    data3['Slice'].extend([f'{i-max_s2e}'] * len(lst))
    data3['Dice'].extend(lst)

df = pd.DataFrame(data3)

plt.figure(figsize=(30, 15)) 
# Create the boxplot
ax = sns.boxplot(x='Slice', y='Dice', data=df, color="yellow", showmeans=True, showfliers=False, whis =0,meanprops={'marker':'o',
                       'markerfacecolor':'red', 
                       'markeredgecolor':'black',
                       'markersize':'8'})
plt.title('Variation in DICE w.r.t. Distance from Start Slice \nSpleen Dataset', loc='left', fontsize=20)  # Add a title
plt.xlabel('Distance from Start Slice')
plt.ylabel('Mean Dice')
plt.xticks(rotation=0)  
plt.annotate('Start Slice = Largest Annotation in Volume',
            xy=(max_s2e, 550), xycoords='data',
            xytext=(-10, 90), textcoords='offset points',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='center', verticalalignment='bottom')


# Customizing x-axis labels to display them at regular intervals
interval = 10  # Set the interval for displaying x-axis labels
all_labels = [f'{i-max_s2e}' for i in range(len(data2))]  # Generate all labels based on data2 length
# Set custom tick labels with specified interval, using '' to skip labels
ax.set_xticklabels([label if i % interval == 0 else '' for i, label in enumerate(all_labels)], rotation=45)

# # For full graph
for i, label in enumerate(not_nan):
    plt.text(i, 0.0, label, ha='center', va='top')

# FOR ZOOM  
# crop =15
# plt.xlim(max_s2e-crop, max_s2e+crop)
# plt.ylim(300,600)
# for i, label in enumerate(not_nan[max_s2e-crop:max_s2e+crop]):
#     plt.text(i+(max_s2e-crop), 250, label, ha='center', va='top')

# Display the plot
plt.show()
