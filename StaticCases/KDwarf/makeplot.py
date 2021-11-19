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
case_list = ["WarmStart/",
              "ColdStart/"]

fig, axs = plt.subplots(2,1,figsize=(7,9))
fig.subplots_adjust(top=0.94,
bottom=0.065,
left=0.08,
right=0.975,
hspace=0.2,
wspace=0.2)

for x,dest in enumerate(case_list):
    folders = sorted([f.path for f in os.scandir(os.path.abspath(dest)) if f.is_dir()])
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

    iFF = axs[x].contourf(obliq0,inst,iceFree,[0,1],colors = vpl.colors.dark_blue)
    sNF = axs[x].contourf(obliq0,inst,snowball,[0.5,1],colors = '#efefef')
    PcF = axs[x].contourf(obliq0,inst,PolarCaps,[0.5,1],colors = vpl.colors.purple)
    icF = axs[x].contourf(obliq0,inst,icebeltL,[0.5,1],colors = vpl.colors.pale_blue)
    icF = axs[x].contourf(obliq0,inst,icebeltS,[0.5,1],colors = vpl.colors.pale_blue)
    icF = axs[x].contourf(obliq0,inst,IceBelt,[0.5,1],colors = vpl.colors.pale_blue)

    h1, _ = iFF.legend_elements()
    h2, _ = icF.legend_elements()
    h3, _ = sNF.legend_elements()
    h4, _ = PcF.legend_elements()

    axs[0].legend([h1[0], h2[0], h3[0], h4[0]], [ 'Ice Free', 'Ice Belt', 'Snowball','Polar Ice Caps'],
               loc = 'upper left', bbox_to_anchor=(0, 1.1, 1, 0.11),ncol=4, mode="expand", borderaxespad=0)

    axs[0].set_title("K Star Warm Start", fontsize = 16)
    axs[1].set_title("K Star Cold Start", fontsize = 16)

    axs[x].set_ylabel("Instellation [Earth]", fontsize=14)
    axs[x].set_xlabel("Obliquity [$^\circ$]", fontsize=14)

    axs[x].set_xlim(0,90)


    axs[0].set_ylim(0.87,1.25)
    axs[1].set_ylim(1.05,1.3)

    plt.tight_layout()
    plt.ylabel('Instellation [Earth]', fontsize=16)
    plt.xlabel(r'Obliquity [$^\circ$]', fontsize=16)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.xlim(0,90)

if (sys.argv[1] == 'pdf'):
    plt.savefig('K_StaticCompare' + '.pdf')
if (sys.argv[1] == 'png'):
    plt.savefig('K_StaticCompare' + '.png')

plt.show()
plt.close()
