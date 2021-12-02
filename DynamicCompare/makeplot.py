import subprocess as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import vplot as vpl
import os
import matplotlib.patches as mpatches
import sys
import scipy.ndimage
from matplotlib.pyplot import figure
import matplotlib.lines as mlines

matplotlib.rc('xtick', labelsize = 12)
matplotlib.rc('ytick', labelsize = 12)

def subcatagorybar(X,vals,axis, color,width = 0.8):
    n = len(vals)
    _X =np.arange(len(X))
    for i in range(n):
        axs[axis].bar(_X - width/2. + i/float(n)*width,vals[i],
                width = width/float(n), align = 'edge', color = color[i])
    axs[axis].set_xticks(_X)


labels = ["Moist Greenhouse","Ice Free", "Singular Caps", "Polar Caps", "Ice Belts", "Snowball"]

legend = ["Case A","Case B","Case C","Case D", "Case E"]

colors = [vpl.colors.red,vpl.colors.orange,vpl.colors.pale_blue,vpl.colors.dark_blue,vpl.colors.purple]

F_norm = [307, 7785, 51, 215, 69, 1573]
F_norm_alb = [319, 7782, 35, 197, 78, 1588]
F_alb_gu = [294, 7483 ,47, 168, 81, 1923]
F_alb_un = [308, 7491, 29, 180, 66, 1924]
F_rotation = [304,7795,43,191,73,1594]

F_Cases = [F_norm,F_norm_alb,F_alb_gu,F_alb_un,F_rotation]

G_norm = [401,7054,26,216,385,1918]
G_norm_alb = [391,7065,28,204,400,1911]
G_alb_gu = [395,6727,14,193,338,2327]
G_alb_un = [406,6740,17,196,311,2327]
G_rotation = [392,7042,34,212,401,1919]

G_Cases = [G_norm,G_norm_alb,G_alb_gu,G_alb_un,G_rotation]

K_norm = [132,7070,39,279,650,1829]
K_norm_alb = [138,7015,28,318,646,1852]
K_alb_gu = [134,5772,26,199,446,3416]
K_alb_un = [130,5773,27,193,424,3423]
K_rotation = [128,7007,38,311,660,1856]

K_Cases = [K_norm,K_norm_alb,K_alb_gu,K_alb_un,K_rotation]

All = [K_Cases,G_Cases,F_Cases]

x = np.arange(len(labels))
width = 0.2
fig, axs = plt.subplots(3,1,figsize=(9,8))
fig.subplots_adjust(top=0.83,hspace = 0.54)

for i in range(len(All)):
    axs[0].set_title("K Dwarf", fontsize = 16)
    axs[1].set_title("G Dwarf", fontsize = 16)
    axs[2].set_title("F Dwarf", fontsize = 16)
    subcatagorybar(labels,All[i],i,colors)
    axs[i].set_ylabel("Number of Cases", fontsize = 14)
    axs[i].set_xticklabels(labels, fontsize = 12)
    axs[i].set_yscale('log')
    axs[2].set_xlabel("Classification", fontsize = 14)
    axs[i].set_yticks([10**2,10**3,10**4])

handles = [mpatches.Patch(color = colors[count], label = value) for count, value in enumerate(legend)]

plt.legend(handles = handles, fontsize = 14, bbox_to_anchor=(0.,4.35,1.,.105),loc = 'lower left',
           ncol=2, mode="expand", borderaxespad=0,edgecolor='k')

if (sys.argv[1] == 'pdf'):
    plt.savefig('DynamicCompare' + '.pdf')
if (sys.argv[1] == 'png'):
    plt.savefig('DynamicCompare' + '.png')

plt.show()
plt.close()
