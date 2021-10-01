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
import math
import vplanet

num = 100
dest = [
["/media/caitlyn/Data_Drive8/Projects/IceBelt/K_Cases/K_obl_stat_large/K_exp10000/",
"/media/caitlyn/Data_Drive8/Projects/IceBelt/K_Cases/K_ecc01_stat/K_exp10000_ecc01/",
"/media/caitlyn/Data_Drive8/Projects/IceBelt/K_Cases/K_ecc02_stat/K_exp10000_ecc02/",
"/media/caitlyn/Data_Drive8/Projects/IceBelt/K_Cases/K_ecc03_stat/K_exp10000_ecc03/"],

["/media/caitlyn/Data_Drive8/Projects/IceBelt/G_Cases/G_obl_stat_large/Sol_exp10000/",
"/media/caitlyn/Data_Drive8/Projects/IceBelt/G_Cases/G_ecc01_stat/Sol_exp10000_ecc01/",
"/media/caitlyn/Data_Drive8/Projects/IceBelt/G_Cases/G_ecc02_stat/G_exp10000_ecc02/"],

["/media/caitlyn/Data_Drive8/Projects/IceBelt/F_Cases/F_obl_stat_large/F_exp10000/",
"/media/caitlyn/Data_Drive8/Projects/IceBelt/F_Cases/F_ecc01_stat/F_exp10000_ecc01/"]
]

matplotlib.rc('xtick', labelsize = 12)
matplotlib.rc('ytick', labelsize = 12)


style = ["solid","dashed", "dotted", "dashdot"]
labels = ["e=0","e=0.1","e=0.2","e=0.3"]
star = ["K Star", "G Star", "F Star"]

fig, axs = plt.subplots(3,1,figsize=(6.5,9))
fig.subplots_adjust(top=0.913,bottom=0.079,left=0.14,right=0.952,hspace=0.35,wspace=0.13)

for i in range(len(dest)):
    for ii in range(len(dest[i])):

        folders = sorted([f.path for f in os.scandir(os.path.abspath(dest[i][ii])) if f.is_dir()])
        #print(folders)
        num = int(num)

        print(len(folders))

        lum0 = np.zeros(len(folders))
        obliq0 = np.zeros(len(folders))
        semi0 = np.zeros(len(folders))
        inst = np.zeros(len(folders))

        snowballL = np.zeros(len(folders))
        snowballS = np.zeros(len(folders))
        snowball = np.zeros(len(folders))

        northCapL = np.zeros(len(folders))
        northCapS = np.zeros(len(folders))
        southCapL = np.zeros(len(folders))
        southCapS = np.zeros(len(folders))
        PolarCaps = np.zeros(len(folders))

        icebeltL = np.zeros(len(folders))
        icebeltS = np.zeros(len(folders))
        IceBelt = np.zeros(len(folders))

        iceFree = np.zeros(len(folders))
        tGlobal = np.zeros(len(folders))

        for j,value in enumerate(folders,start = 0):
            print(value)
            out = vplanet.get_output(value, units = False)
            lum0[j] = getattr(out.log.initial, 'sun').Luminosity
            obliq0[j] = getattr(out.log.initial, 'earth').Obliquity
            semi0[j] = getattr(out.log.initial, 'earth').SemiMajorAxis
            inst[j] = getattr(out.log.final, 'earth').Instellation

            snowballL[j] = getattr(out.log.final, 'earth').SnowballLand
            snowballS[j] = getattr(out.log.final, 'earth').SnowballSea


            northCapL[j] = getattr(out.log.final, 'earth').IceCapNorthLand
            northCapS[j] = getattr(out.log.final, 'earth').IceCapNorthSea

            southCapL[j] = getattr(out.log.final, 'earth').IceCapSouthLand
            southCapS[j] = getattr(out.log.final, 'earth').IceCapSouthSea

            icebeltL[j] = getattr(out.log.final, 'earth').IceBeltLand
            icebeltS[j] = getattr(out.log.final, 'earth').IceBeltSea

            iceFree[j] = getattr(out.log.final, 'earth').IceFree

            tGlobal[j] = getattr(out.log.final, 'earth').TGlobal

            if snowball[j] == 1:
                icebeltL[j] = 0
                icebeltS[j] = 0
                northCapL[j] = 0
                northCapS[j] = 0
                southCapL[j] = 0
                southCapS[j] = 0
                iceFree[j] = 0

            if (
                #North Land, South Land
                northCapL[j] == 1 and northCapS[j] == 0 and
                southCapL[j] == 1 and southCapS[j] == 0 and
                icebeltL[j] == 0  and icebeltS[j] == 0  and
                snowballL[j] == 0 and snowballS[j] == 0 or

                #North Sea, South Land
                northCapL[j] == 0 and northCapS[j] == 1 and
                southCapL[j] == 1 and southCapS[j] == 0 and
                icebeltL[j] == 0  and icebeltS[j] == 0  and
                snowballL[j] == 0 and snowballS[j] == 0 or

                #North Both, South Land
                northCapL[j] == 1 and northCapS[j] == 1 and
                southCapL[j] == 1 and southCapS[j] == 0 and
                icebeltL[j] == 0  and icebeltS[j] == 0  and
                snowballL[j] == 0 and snowballS[j] == 0 or

                #North Land, South Sea
                northCapL[j] == 1 and northCapS[j] == 0 and
                southCapL[j] == 0 and southCapS[j] == 1 and
                icebeltL[j] == 0  and icebeltS[j] == 0  and
                snowballL[j] == 0 and snowballS[j] == 0 or

                #North Sea, South Sea
                northCapL[j] == 0 and northCapS[j] == 1 and
                southCapL[j] == 0 and southCapS[j] == 1 and
                icebeltL[j] == 0  and icebeltS[j] == 0  and
                snowballL[j] == 0 and snowballS[j] == 0 or

                #North Both, South Sea
                northCapL[j] == 1 and northCapS[j] == 1 and
                southCapL[j] == 0 and southCapS[j] == 1 and
                icebeltL[j] == 0  and icebeltS[j] == 0  and
                snowballL[j] == 0 and snowballS[j] == 0 or

                #North Land, South Both
                northCapL[j] == 1 and northCapS[j] == 0 and
                southCapL[j] == 1 and southCapS[j] == 1 and
                icebeltL[j] == 0  and icebeltS[j] == 0  and
                snowballL[j] == 0 and snowballS[j] == 0 or

                #North Sea, South Both
                northCapL[j] == 0 and northCapS[j] == 1 and
                southCapL[j] == 1 and southCapS[j] == 1 and
                icebeltL[j] == 0  and icebeltS[j] == 0  and
                snowballL[j] == 0 and snowballS[j] == 0 or

                #North Both, South Both
                northCapL[j] == 1 and northCapS[j] == 1 and
                southCapL[j] == 1 and southCapS[j] == 1 and
                icebeltL[j] == 0  and icebeltS[j] == 0  and
                snowballL[j] == 0 and snowballS[j] == 0
            ):
                PolarCaps[j] = 1

            if (
                #Land
                northCapL[j] == 0 and northCapS[j] == 0 and
                southCapL[j] == 0 and southCapS[j] == 0 and
                icebeltL[j] == 1  and icebeltS[j] == 0  and
                snowballL[j] == 0 and snowballS[j] == 0 or

                #Sea
                northCapL[j] == 0 and northCapS[j] == 0 and
                southCapL[j] == 0 and southCapS[j] == 0 and
                icebeltL[j] == 0  and icebeltS[j] == 1  and
                snowballL[j] == 0 and snowballS[j] == 0 or

                #Both
                northCapL[j] == 0 and northCapS[j] == 0 and
                southCapL[j] == 0 and southCapS[j] == 0 and
                icebeltL[j] == 1  and icebeltS[j] == 1 and
                snowballL[j] == 0 and snowballS[j] == 0
            ):
                IceBelt[j] = 1

        lum0 = np.reshape(lum0, (num, num))
        obliq0 = np.reshape(obliq0, (num, num)) * 180 / np.pi
        semi0 = np.reshape(semi0, (num, num)) / 1.49598e11
        inst = np.reshape(inst, (num, num)) / 1350
        snowball = np.reshape(snowball, (num, num))
        northCapL = np.reshape(northCapL, (num, num))
        northCapS = np.reshape(northCapS, (num, num))
        southCapL = np.reshape(southCapL, (num, num))
        southCapS = np.reshape(southCapS, (num, num))
        icebeltL = np.reshape(icebeltL, (num, num))
        icebeltS = np.reshape(icebeltS, (num, num))
        iceFree = np.reshape(iceFree, (num, num))
        tGlobal = np.reshape(tGlobal, (num, num))
        PolarCaps = np.reshape(PolarCaps, (num, num))
        IceBelt = np.reshape(IceBelt, (num, num))

        icF = axs[i].contour(obliq0,inst,IceBelt, [0.5, 1], colors = 'black', linestyles = style[ii])
        pc = axs[i].contour(obliq0,inst,PolarCaps, [0.5, 1], colors = 'black', linestyles = style[ii])

    e0 = mlines.Line2D([],[],color = 'black',linewidth=2,label = labels[0],linestyle = style[0])
    e1 = mlines.Line2D([],[],color = 'black',linewidth=2,label = labels[1],linestyle = style[1])
    e2 = mlines.Line2D([],[],color = 'black',linewidth=2,label = labels[2],linestyle = style[2])
    e3 = mlines.Line2D([],[],color = 'black',linewidth=2,label = labels[3],linestyle = style[3])

    axs[0].set_title("K Star", fontsize = 16)
    axs[1].set_title("G Star", fontsize = 16)
    axs[2].set_title("F Star", fontsize = 16)

    axs[0].legend(handles = [e0,e1,e2,e3], fontsize=14, loc = 'upper left', bbox_to_anchor=(0, 1.25, 1, 0.102),ncol=4, mode="expand", borderaxespad=0)
    axs[1].set_ylabel("Instellation [Earth]", fontsize=14)
    axs[2].set_xlabel("Obliquity [$^\circ$]", fontsize=14)

    axs[0].set_xlim(0,90)
    axs[1].set_xlim(0,90)
    axs[2].set_xlim(0,90)

    # axs[i].set_xticks(obliq0)
    # axs[i].set_yticks(inst)

    axs[0].set_ylim(0.87,1.225)
    axs[1].set_ylim(0.875,1.225)
    axs[2].set_ylim(0.935,1.225)

plt.tight_layout()
# os.chdir('/home/caitlyn/IceSheet/EccCompareIceBelt')
if (sys.argv[1] == 'pdf'):
    plt.savefig('EccCompare2' + '.pdf')
if (sys.argv[1] == 'png'):
    plt.savefig('EccCompare2' + '.png')

plt.show()
plt.close()
