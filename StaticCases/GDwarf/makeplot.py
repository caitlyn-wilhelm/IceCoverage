import subprocess as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import vplot as vpl
import os
import sys
import h5py
from matplotlib.pyplot import figure
#bigplanet imports
from bigplanet.bp_extract import *

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
    
    HDF5_File = h5py.File('Test.bpf', 'r')

    earth_icebelt_L = ExtractColumn(HDF5_File,'earth:IceBeltLand:final')
    earth_icebelt_S = ExtractColumn(HDF5_File,'earth:IceBeltSea:final')
    earth_northcap_L = ExtractColumn(HDF5_File,'earth:IceCapNorthLand:final')
    earth_northcap_S = ExtractColumn(HDF5_File,'earth:IceCapNorthSea:final')
    earth_southcap_L = ExtractColumn(HDF5_File,'earth:IceCapSouthLand:final')
    earth_southcap_S = ExtractColumn(HDF5_File,'earth:IceCapSouthSea:final')

    earth_icefree = ExtractColumn(HDF5_File,'earth:IceFree:final')
    earth_snowball_L = ExtractColumn(HDF5_File,'earth:SnowballLand:final')
    earth_snowball_S = ExtractColumn(HDF5_File,'earth:SnowballSea:final')


    #gets the x and y axis data
    earth_Obliq_uniq = ExtractUniqueValues(HDF5_File,'earth:Obliquity:initial')
    earth_intstel_uniq = ExtractUniqueValues(HDF5_File,'earth:Instellation:final')

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
                #Both
                earth_northcap_L[j] == 0 and earth_northcap_S[j] == 0 and
                earth_southcap_L[j] == 0 and earth_southcap_S[j] == 0 and
                earth_icebelt_L[j] == 1  and earth_icebelt_S[j] == 1 and
                earth_snowball_L[j] == 0 and earth_snowball_S[j] == 0
            ):
                IceBelt[j] = 1


    #creates the zaxis for plotting
    icebeltLmatrix = CreateMatrix(earth_Obliq_uniq, earth_intstel_uniq, earth_icebelt_L)
    icebeltSmatrix = CreateMatrix(earth_Obliq_uniq, earth_intstel_uniq, earth_icebelt_S)
    icefreematrix = CreateMatrix(earth_Obliq_uniq, earth_intstel_uniq, earth_icefree)
    snowballmatrix = CreateMatrix(earth_Obliq_uniq, earth_intstel_uniq, Snowball)
    Capsmatrix = CreateMatrix(earth_Obliq_uniq, earth_intstel_uniq, PolarCaps)

    #figure size and axiss
    plt.figure(figsize=(9,6.5))
    plt.ylabel("Instellation [Earth]", fontsize=16)
    plt.xlabel("Obliquity [$^\circ$]", fontsize=16)
    plt.ylim(0.891,1.211)
    plt.xlim(0,90)

    #plots data
    iFF = plt.contourf(earth_Obliq_uniq,earth_intstel_uniq,icefreematrix,[0,1],colors = vpl.colors.dark_blue)
    sNF = plt.contourf(earth_Obliq_uniq,earth_intstel_uniq,snowballmatrix,[0.5,1],colors = '#efefef')
    PcF = plt.contourf(earth_Obliq_uniq,earth_intstel_uniq,Capsmatrix,[0.5,1],colors = vpl.colors.purple)
    icF = plt.contourf(earth_Obliq_uniq,earth_intstel_uniq,icebeltLmatrix,[0.5,1],colors = vpl.colors.pale_blue)
    icF = plt.contourf(earth_Obliq_uniq,earth_intstel_uniq,icebeltSmatrix,[0.5,1],colors = vpl.colors.pale_blue)


    #legend
    h1, _ = iFF.legend_elements()
    h2, _ = icF.legend_elements()
    h3, _ = sNF.legend_elements()
    h4, _ = PcF.legend_elements()

    h1[0].set_edgecolor('k')
    h2[0].set_edgecolor('k')
    h3[0].set_edgecolor('k')
    h4[0].set_edgecolor('k')

    plt.legend([h1[0], h2[0], h3[0], h4[0]], [ 'Ice Free', 'Ice Belt', 'Snowball','Polar Ice Caps'],
                loc = 'upper left', bbox_to_anchor=(0, 1.02, 1, 0.102),ncol=4, mode="expand", borderaxespad=0,edgecolor='k')


    axs[0].set_title("G Dwarf, Warm Start", fontsize = 16)
    axs[1].set_title("G Dwarf, Cold Start", fontsize = 16)

    axs[x].set_ylabel("Instellation [Earth]", fontsize=14)
    axs[x].set_xlabel("Obliquity [$^\circ$]", fontsize=14)

    axs[x].set_xlim(0,90)

    axs[0].set_ylim(0.89,1.25)
    axs[1].set_ylim(1.1,1.4)

    plt.tight_layout()
    plt.ylabel('Instellation [Earth]', fontsize=16)
    plt.xlabel(r'Obliquity [$^\circ$]', fontsize=16)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.xlim(0,90)

if (sys.argv[1] == 'pdf'):
    plt.savefig('G_StaticCompare' + '.pdf')
if (sys.argv[1] == 'png'):
    plt.savefig('G_StaticCompare' + '.png')

plt.show()
plt.close()
