import csv
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set()
norm_visual = {};
dist_visual = {};
layers = [3, 27, 54, 81]
font = {'weight': 'normal',
        'size': 20}
with open('parameter_visual.csv','r') as myFile:
    lines=csv.reader(myFile)
    rows = [row for row in lines]
    print(rows[0])
    plt.figure(figsize = (12, 8))
    for index in range(4):
        plt.subplot(411 + index)
        plt.grid(True)
        sns.kdeplot( np.array(rows[index]).astype(np.float), linewidth=4)
        sns.kdeplot( np.array(rows[index+4]).astype(np.float), linewidth = 4)
        plt.xticks(fontsize=15)

        plt.yticks(fontsize=15)
        plt.ylabel("Layer {0}\nDensity".format(layers[index]), font)
        plt.legend([r'$I_a$', r'$I_r$'], loc='upper right', fontsize='x-large')
        plt.xlabel("Importance")
        #if index == 0:
        #    plt.xlabel("Importance")

plt.tight_layout()
plt.show()
