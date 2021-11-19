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
import bigplanet as bp


num = 100
dest = ["../StaticCases/KDwarf/WarmStart/",
"../StaticCases/GDwarf/WarmStart/",
"../StaticCases/Fwarf/WarmStart/",
]

colorz = [vpl.colors.red,vpl.colors.orange,vpl.colors.pale_blue]
labels = ['K Dwarf','G Dwarf','F Dwarf']

plt.figure(figsize=(9,6.5))

for i,value in enumerate(dest):

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

    pc = plt.contour(earth_Obliq_uniq,earth_intstel_uniq,PolarCaps, [0.5, 1], colors = colorz[i],linewidths=3)
    icF = plt.contour(earth_Obliq_uniq,earth_intstel_uniq,IceBelt, [0.5, 1], colors = colorz[i], linewidths=3)


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

plt.legend(handles = [line0,line1,line2], loc='upper right', fontsize=14,edgecolor='k')

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
