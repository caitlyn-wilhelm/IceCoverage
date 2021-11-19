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
import bigplanet as bp
import h5py

num = 100
dest = [
["../StaticCases/KDwarf/WarmStart/",
 "../StaticCases/KDwarf/Ecc01/",
 "../StaticCases/KDwarf/Ecc02/",
 "../StaticCases/KDwarf/Ecc03/"],

["../StaticCases/GDwarf/WarmStart/",
"../StaticCases/GDwarf/Ecc01/",
"../StaticCases/GDwarf/Ecc02/",],

["../StaticCases/FDwarf/WarmStart/",
"../StaticCases/FDwarf/Ecc01/"]
]

matplotlib.rc('xtick', labelsize = 12)
matplotlib.rc('ytick', labelsize = 12)


style = ["solid","dashed", "dotted", "dashdot"]
labels = ["e=0","e=0.1","e=0.2","e=0.3"]
star = ["K Dwarf", "G Dwarf", "F Dwarf"]

fig, axs = plt.subplots(3,1,figsize=(6.5,9))
fig.subplots_adjust(top=0.913,bottom=0.079,left=0.14,right=0.952,hspace=0.35,wspace=0.13)

for i in range(len(dest)):
    for ii in range(len(dest[i])):

        HDF5_File = h5py.File('Test.bpf', 'r')

        earth_icebelt_L = bp.ExtractColumn(HDF5_File,'earth:IceBeltLand:final')
        earth_icebelt_S = bp.ExtractColumn(HDF5_File,'earth:IceBeltSea:final')
        earth_northcap_L = bp.ExtractColumn(HDF5_File,'earth:IceCapNorthLand:final')
        earth_northcap_S = bp.ExtractColumn(HDF5_File,'earth:IceCapNorthSea:final')
        earth_southcap_L = bp.ExtractColumn(HDF5_File,'earth:IceCapSouthLand:final')
        earth_southcap_S = bp.ExtractColumn(HDF5_File,'earth:IceCapSouthSea:final')

        earth_icefree = bp.ExtractColumn(HDF5_File,'earth:IceFree:final')
        earth_snowball_L = bp.ExtractColumn(HDF5_File,'earth:SnowballLand:final')
        earth_snowball_S = bp.ExtractColumn(HDF5_File,'earth:SnowballSea:final')


        #gets the x and y axis data
        earth_Obliq_uniq = bp.ExtractUniqueValues(HDF5_File,'earth:Obliquity:initial')
        earth_intstel_uniq = bp.ExtractUniqueValues(HDF5_File,'earth:Instellation:final')

        #changing units of axis
        earth_intstel_uniq =  np.reshape(earth_intstel_uniq,(earth_intstel_uniq.shape)) / 1350
        earth_Obliq_uniq = np.reshape(earth_Obliq_uniq,(earth_Obliq_uniq.shape)) * 180 / np.pi

        # #creates a new numpy array that is for Polar Caps
        PolarCaps = np.zeros(len(earth_northcap_L))
        Snowball = np.zeros(len(earth_northcap_L))
        IceBelt = np.zeros(len(earth_northcap_L))


        for j in range(len(PolarCaps)):

            if earth_snowball_L[j] == 1 or earth_snowball_S[j] == 1:
                earth_icebelt_L[j] = 0
                earth_icebelt_S[j] = 0
                earth_northcap_L[j] = 0
                earth_northcap_S[j] = 0
                earth_southcap_L[j] = 0
                earth_southcap_S[j] = 0
                earth_icefree[j] = 0
                Snowball[j] = 1


            if (
                    #North Land, South Land
                    earth_northcap_L[j] == 1 and earth_northcap_S[j] == 0 and
                    earth_southcap_L[j] == 1 and earth_southcap_S[j] == 0 and
                    earth_icebelt_L[j] == 0  and earth_icebelt_S[j] == 0  and
                    earth_snowball_L[j] == 0 and earth_snowball_S[j] == 0 or

                    #North Sea, South Land
                    earth_northcap_L[j] == 0 and earth_northcap_S[j] == 1 and
                    earth_southcap_L[j] == 1 and earth_southcap_S[j] == 0 and
                    earth_icebelt_L[j] == 0  and earth_icebelt_S[j] == 0  and
                    earth_snowball_L[j] == 0 and earth_snowball_S[j] == 0 or

                    #North Both, South Land
                    earth_northcap_L[j] == 1 and earth_northcap_S[j] == 1 and
                    earth_southcap_L[j] == 1 and earth_southcap_S[j] == 0 and
                    earth_icebelt_L[j] == 0  and earth_icebelt_S[j] == 0  and
                    earth_snowball_L[j] == 0 and earth_snowball_S[j] == 0 or

                    #North Land, South Sea
                    earth_northcap_L[j] == 1 and earth_northcap_S[j] == 0 and
                    earth_southcap_L[j] == 0 and earth_southcap_S[j] == 1 and
                    earth_icebelt_L[j] == 0  and earth_icebelt_S[j] == 0  and
                    earth_snowball_L[j] == 0 and earth_snowball_S[j] == 0 or

                    #North Sea, South Sea
                    earth_northcap_L[j] == 0 and earth_northcap_S[j] == 1 and
                    earth_southcap_L[j] == 0 and earth_southcap_S[j] == 1 and
                    earth_icebelt_L[j] == 0  and earth_icebelt_S[j] == 0  and
                    earth_snowball_L[j] == 0 and earth_snowball_S[j] == 0 or

                    #North Both, South Sea
                    earth_northcap_L[j] == 1 and earth_northcap_S[j] == 1 and
                    earth_southcap_L[j] == 0 and earth_southcap_S[j] == 1 and
                    earth_icebelt_L[j] == 0  and earth_icebelt_S[j] == 0  and
                    earth_snowball_L[j] == 0 and earth_snowball_S[j] == 0 or

                    #North Land, South Both
                    earth_northcap_L[j] == 1 and earth_northcap_S[j] == 0 and
                    earth_southcap_L[j] == 1 and earth_southcap_S[j] == 1 and
                    earth_icebelt_L[j] == 0  and earth_icebelt_S[j] == 0  and
                    earth_snowball_L[j] == 0 and earth_snowball_S[j] == 0 or

                    #North Sea, South Both
                    earth_northcap_L[j] == 0 and earth_northcap_S[j] == 1 and
                    earth_southcap_L[j] == 1 and earth_southcap_S[j] == 1 and
                    earth_icebelt_L[j] == 0  and earth_icebelt_S[j] == 0  and
                    earth_snowball_L[j] == 0 and earth_snowball_S[j] == 0 or

                    #North Both, South Both
                    earth_northcap_L[j] == 1 and earth_northcap_S[j] == 1 and
                    earth_southcap_L[j] == 1 and earth_southcap_S[j] == 1 and
                    earth_icebelt_L[j] == 0  and earth_icebelt_S[j] == 0  and
                    earth_snowball_L[j] == 0 and earth_snowball_S[j] == 0
                
                ):
                        PolarCaps[j] = 1
                        
                        
            if (
                #Land
                earth_northcap_L[j] == 0 and earth_northcap_S[j] == 0 and
                earth_southcap_L[j] == 0 and earth_southcap_S[j] == 0 and
                earth_icebelt_L[j] == 1  and earth_icebelt_S[j] == 0  and
                earth_snowball_L[j] == 0 and earth_snowball_S[j] == 0 or

                #Sea
                earth_northcap_L[j] == 0 and earth_northcap_S[j] == 0 and
                earth_southcap_L[j] == 0 and earth_southcap_S[j] == 0 and
                earth_icebelt_L[j] == 0  and earth_icebelt_S[j] == 1  and
                earth_snowball_L[j] == 0 and earth_snowball_S[j] == 0 or

                #Both
                earth_northcap_L[j] == 0 and earth_northcap_S[j] == 0 and
                earth_southcap_L[j] == 0 and earth_southcap_S[j] == 0 and
                earth_icebelt_L[j] == 1  and earth_icebelt_S[j] == 1 and
                earth_snowball_L[j] == 0 and earth_snowball_S[j] == 0
            ):
                IceBelt[j] = 1
            
            icF = axs[i].contour(earth_Obliq_uniq,earth_intstel_uniq,IceBelt, [0.5, 1], colors = 'black', linestyles = style[ii])
            pc = axs[i].contour(earth_Obliq_uniq,earth_intstel_uniq,PolarCaps, [0.5, 1], colors = 'black', linestyles = style[ii])

    e0 = mlines.Line2D([],[],color = 'black',linewidth=2,label = labels[0],linestyle = style[0])
    e1 = mlines.Line2D([],[],color = 'black',linewidth=2,label = labels[1],linestyle = style[1])
    e2 = mlines.Line2D([],[],color = 'black',linewidth=2,label = labels[2],linestyle = style[2])
    e3 = mlines.Line2D([],[],color = 'black',linewidth=2,label = labels[3],linestyle = style[3])

    axs[0].set_title("K Dwarf", fontsize = 16)
    axs[1].set_title("G Dwarf", fontsize = 16)
    axs[2].set_title("F Dwarf", fontsize = 16)

    axs[0].legend(handles = [e0,e1,e2,e3], fontsize=14, loc = 'upper left', bbox_to_anchor=(0, 1.25, 1, 0.102),ncol=4, mode="expand", borderaxespad=0,edgecolor='k')
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
