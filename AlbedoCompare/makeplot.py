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

def subcatagorybar(X,vals,axis, color,width = 0.8):
    n = len(vals)
    _X =np.arange(len(X))
    for i in range(n):
        axs[axis].bar(_X - width/2. + i/float(n)*width,vals[i],
                width = width/float(n), align = 'edge', color = color[i])
    axs[axis].set_xticks(_X)


labels = ["Moist Greenhouse","Ice Free", "Singular Caps", "Polar Caps", "Ice Belts", "Snowball"]

legend = ["Case A","Case B","Case C","Case D"]

colors = [vpl.colors.red,vpl.colors.orange,vpl.colors.pale_blue,vpl.colors.dark_blue]

F_norm = [307, 7784, 103, 164, 70, 1572]
F_norm_alb = [319, 7782, 77, 155, 78, 1558]
F_alb_gu = [294, 7483 ,79, 136, 85, 1923]
F_alb_un = [308, 7491, 72, 136, 67, 1924]

F_Cases = [F_norm,F_norm_alb,F_alb_gu,F_alb_un]

G_norm = [401,7054,55,188,385,1917]
G_norm_alb = [391,7065,65,167,401,1910]
G_alb_gu = [395,6727,40,167,338,2327]
G_alb_un = [406,6740,44,169,311,2327]

G_Cases = [G_norm,G_norm_alb,G_alb_gu,G_alb_un]

K_norm = [132,7070,58,270,651,1819]
K_norm_alb = [139,7015,38,308,647,1852]
K_alb_gu = [134,5772,34,191,446,3397]
K_alb_un = [130,5773,34,186,424,3423]

K_Cases = [K_norm,K_norm_alb,K_alb_gu,K_alb_un]

All = [K_Cases,G_Cases,F_Cases]

x = np.arange(len(labels))
width = 0.2
fig, axs = plt.subplots(3,1,figsize=(9,8))
fig.subplots_adjust(top=0.8,hspace = 0.5)

for i in range(len(All)):
    axs[0].set_title("K Star", fontsize = 16)
    axs[1].set_title("G Star", fontsize = 16)
    axs[2].set_title("F Star", fontsize = 16)
    subcatagorybar(labels,All[i],i,colors)
    axs[i].set_ylabel("Number of Cases", fontsize = 13)
    axs[i].set_xticklabels(labels, fontsize = 12)
    axs[i].set_yscale('log')
    axs[i].set_xlabel("Classification", fontsize = 13)
    axs[i].set_yticks([10**2,10**3,10**4])

handles = [mpatches.Patch(color = colors[count], label = value) for count, value in enumerate(legend)]
plt.legend(handles = handles, fontsize = 14, bbox_to_anchor=(0.,4.35,1.,.105),loc = 'lower left',
           ncol=2, mode="expand", borderaxespad=0)

if (sys.argv[1] == 'pdf'):
    plt.savefig('AlbedoComparison' + '.pdf')
if (sys.argv[1] == 'png'):
    plt.savefig('AlbedoComparison' + '.png')
