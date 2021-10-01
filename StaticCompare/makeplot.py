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
import vplanet

num = 100
dest = ["/media/caitlyn/Data_Drive8/Projects/IceBelt/K_Cases/K_obl_stat_large/K_exp10000/",
"/media/caitlyn/Data_Drive8/Projects/IceBelt/G_Cases/G_obl_stat_large/Sol_exp10000/",
"/media/caitlyn/Data_Drive8/Projects/IceBelt/F_Cases/F_obl_stat_large/F_exp10000/",
]

colorz = [vpl.colors.red,vpl.colors.orange,vpl.colors.pale_blue]
labels = ['K Dwarf','G Dwarf','F Dwarf']

plt.figure(figsize=(9,6.5))

for i,value in enumerate(dest):

    folders = sorted([f.path for f in os.scandir(os.path.abspath(value)) if f.is_dir()])
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

    icebeltL = np.zeros(len(folders))
    icebeltS = np.zeros(len(folders))
    IceBelt = np.zeros(len(folders))

    iceFree = np.zeros(len(folders))
    tGlobal = np.zeros(len(folders))
    PolarCaps = np.zeros(len(folders))

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

        if snowballL[j] == 1 or snowballS[j] == 1:
            icebeltL[j] = 0
            icebeltS[j] = 0
            northCapL[j] = 0
            northCapS[j] = 0
            southCapL[j] = 0
            southCapS[j] = 0
            iceFree[j] = 0
            snowball[j] = 1

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

    obliq0 = np.reshape(obliq0, (num, num)) * 180 / np.pi
    semi0 = np.reshape(semi0, (num, num)) / 1.49598e11
    inst = np.reshape(inst, (num, num)) / 1350
    snowball = np.reshape(snowball, (num, num))
    northCapL = np.reshape(northCapL, (num, num))
    northCapS = np.reshape(northCapS, (num, num))
    southCapL = np.reshape(southCapL, (num, num))
    southCapS = np.reshape(southCapS, (num, num))
    IceBelt = np.reshape(IceBelt, (num, num))
    icebeltL = np.reshape(icebeltL, (num, num))
    icebeltS = np.reshape(icebeltS, (num, num))
    iceFree = np.reshape(iceFree, (num, num))
    tGlobal = np.reshape(tGlobal, (num, num))
    PolarCaps = np.reshape(PolarCaps, (num, num))

    pc = plt.contour(obliq0,inst,PolarCaps, [0.5, 1], colors = colorz[i],linewidths=3)
    icF = plt.contour(obliq0,inst,IceBelt, [0.5, 1], colors = colorz[i], linewidths=3)


plt.plot([37.8,45.0],[0.9674,0.9414], color = vpl.colors.red, linewidth = 3, dashes = [6,2])
plt.plot([36.0,47.7],[0.992,0.9623], color = vpl.colors.orange, linewidth = 3, dashes = [6,2])
plt.plot([36.8,60.5],[1.011,0.9813], color = vpl.colors.pale_blue, linewidth = 3, dashes = [6,2])

line0 = mlines.Line2D([],[],color = colorz[0],linewidth=3,label = labels[0])
line1 = mlines.Line2D([],[],color = colorz[1],linewidth=3,label = labels[1])
line2 = mlines.Line2D([],[],color = colorz[2],linewidth=3,label = labels[2])

#annotations
plt.annotate("Snowball",xy=(20.5,0.9055), fontsize = 14.5)
plt.annotate("IceBelt",xy=(75, 0.975), fontsize = 14.5)
plt.annotate("Polar Caps",xy=(2,1.05), fontsize = 14.5)
plt.annotate("Ice Free",xy=(45,1.1), fontsize = 14.5)

plt.legend(handles = [line0,line1,line2], loc='upper right', fontsize=14)

plt.ylabel('Instellation [Earth]', fontsize=16)
plt.xlabel(r'Obliquity [$^\circ$]', fontsize=16)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlim(0,90)
plt.ylim(0.87,1.225)

plt.tight_layout()

if (sys.argv[1] == 'pdf'):
    plt.savefig('StaticCompare' + '.pdf')
if (sys.argv[1] == 'png'):
    plt.savefig('StaticCompare' + '.png')

plt.show()
plt.close()
