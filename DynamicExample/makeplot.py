import numpy as np
import matplotlib.pyplot as plt
import vplot as vpl
from matplotlib import ticker
import os
import subprocess
import re
import sys
import vplanet
import bigplanet as bp
import pathlib
from itertools import chain

def clim_evol(plname,dir='.',xrange=False,orbit=False,show=True):
  """
  Creates plots of insolation, temperature, albedo, ice mass,
  and bed rock height over the length of the simulation

  Parameters
  ----------
  plname : string
    The name of the planet with .Climate data

  Keyword Arguments
  -----------------
  dir : string
    Directory of vplanet simulation (default = '.')
  xrange : float tuple, list, or numpy array
    Range of x-values (time) to restrict plot
    (default = False (no restriction))
  orbit : bool
    Plot orbital data (obliquity, eccentricity, COPP)
    (default = False)
  show : bool
    Show plot in Python (default = True)

  Output
  ------
  PDF format plot with name 'evol_<dir>.pdf'

  """
  
  # gets current path
  path = pathlib.Path(__file__).parents[0].absolute()
  sys.path.insert(1, str(path.parents[0]))





  fig = plt.figure(figsize=(9,8))
  fig.subplots_adjust(wspace=0.5,hspace = 0.5)
  file = bp.BPLFile(path / "DynamicExample.bpf")

  ecc = bp.ExtractColumn(file,'earth:Eccentricity:forward')[0]
  obl = bp.ExtractColumn(file,'earth:Obliquity:forward')[0]

  copp = bp.ExtractColumn(file,'earth:COPP:forward')[0]
  lats = bp.ExtractUniqueValues(file,'earth:Latitude:climate')
  
  times = bp.ExtractColumn(file,'earth:Time:forward')[0]
  temp = bp.ExtractColumn(file,'earth:TempLat:climate')[0]
  alb = bp.ExtractColumn(file,'earth:AlbedoLat:climate')[0]
  ice = bp.ExtractColumn(file,'earth:IceHeight:climate')[0]
  insol = bp.ExtractColumn(file,'earth:AnnInsol:climate')[0]
  brock = bp.ExtractColumn(file,'earth:BedrockH:climate')[0]

  nlats = len(lats)
  ntimes = len(times)

  # plot temperature
  temp = bp.CreateMatrix(lats,times,temp)
  temp_T = np.array(temp).T.tolist()
  #temp = np.reshape(temp,(ntimes,nlats))
  plt.subplot(4,2,1)
  c = plt.contourf(times,lats,temp_T,cmap='plasma')
  plt.ylabel(r'Latitude [$^\circ$]', fontsize = 10)
  plt.title(r'Surface Temp [$^{\circ}$C]', fontsize = 12)
  plt.ylim(-85,85)
  plt.yticks([-60,-30,0,30,60], fontsize = 9)
  plt.xticks(fontsize = 9)
  if xrange:
    plt.xlim(xrange)
  cbar = plt.colorbar(c)
  plt.setp(cbar.ax.yaxis.get_ticklabels(), fontsize = 9)

  # plot albedo
  #alb = np.reshape(alb,(ntimes,nlats))
  alb = bp.CreateMatrix(lats,times,alb)
  alb_T = np.array(alb).T.tolist()
  plt.subplot(4,2,3)
  #pos = ax2.figbox.get_points()
  c = plt.contourf(times,lats,alb_T,cmap = 'Blues_r')
  plt.ylabel(r'Latitude [$^\circ$]', fontsize = 10)
  plt.title('Albedo [TOA]', fontsize = 12)
  plt.ylim(-85,85)
  plt.yticks([-60,-30,0,30,60], fontsize = 9)
  plt.xticks(fontsize = 9)
  if xrange:
    plt.xlim(xrange)
  cbar = plt.colorbar(c)
  plt.setp(cbar.ax.yaxis.get_ticklabels(), fontsize = 9)


  # plot ice height
  #ice = np.reshape(ice,(ntimes,nlats))
  ice = bp.CreateMatrix(lats,times,ice)
  ice_T = np.array(ice).T.tolist()
  plt.subplot(4,2,5)
  #pos = ax3.figbox.get_points()
  c = plt.contourf(times,lats,ice_T,cmap='Blues_r')
  plt.ylabel(r'Latitude [$^\circ$]', fontsize = 10)
  plt.title('Ice sheet height [m]', fontsize = 12)
  plt.ylim(-85,85)
  plt.yticks([-60,-30,0,30,60], fontsize = 9)
  plt.xticks(fontsize = 9)
  if xrange:
    plt.xlim(xrange)
  cbar = plt.colorbar(c)
  plt.setp(cbar.ax.yaxis.get_ticklabels(), fontsize = 9)


  # plot bedrock
  brock = bp.CreateMatrix(lats,times,brock)
  brock_T = np.array(brock).T.tolist()
  plt.subplot(4,2,7)
  c = plt.contourf(times,lats,brock_T,cmap='Reds_r')
  plt.ylabel(r'Latitude [$^\circ$]', fontsize = 10)
  plt.title('Bedrock height [m]', fontsize = 12)
  plt.ylim(-85,85)
  plt.yticks([-60,-30,0,30,60], fontsize = 9)
  plt.xlabel('Time [years]',fontsize = 10)
  plt.xticks(fontsize = 9)
  if xrange:
    plt.xlim(xrange)
  cbar = plt.colorbar(c)
  plt.setp(cbar.ax.yaxis.get_ticklabels(), fontsize = 9)

  # plot insolation
  insol = bp.CreateMatrix(lats,times,insol)
  insol_T = np.array(insol).T.tolist()
  plt.subplot(4,2,2)
  c = plt.contourf(times,lats,insol_T,cmap='plasma')
  plt.ylabel(r'Latitude [$^\circ$]', fontsize = 10)
  plt.title(r'Annual average instellation [W/m$^2$]', fontsize = 12)
  plt.ylim(-85,85)
  plt.yticks([-60,-30,0,30,60], fontsize = 9)
  plt.xticks(fontsize = 9)
  if xrange:
    plt.xlim(xrange)
  cbar = plt.colorbar(c)
  plt.setp(cbar.ax.yaxis.get_ticklabels(), fontsize = 9)

  #obliquity
  plt.subplot(4,2,4)
  plt.plot(times,obl,linestyle = 'solid',marker='None',color='darkblue',linewidth =2)
  plt.ylabel(r'Obliquity [$^\circ$]', fontsize = 10)
  plt.yticks(fontsize = 9)
  plt.xticks(fontsize = 9)
  plt.xlim(0,250000)

  if xrange:
      plt.xlim(xrange)

  #eccentricity
  plt.subplot(4,2,6)
  plt.plot(times,ecc,linestyle = 'solid',marker='None',color='darkorchid',linewidth =2)
  plt.ylabel('Eccentricity', fontsize = 10)
  plt.xticks(fontsize = 9)
  plt.yticks(fontsize = 9)
  plt.xlim(0,250000)
  if xrange:
      plt.xlim(xrange)

  #e sin(obl) sin varpi
  plt.subplot(4,2,8)
  plt.plot(times,copp,linestyle = 'solid',marker='None',color='salmon',linewidth=2)
  plt.ylabel('COPP', fontsize = 10)
  plt.xlabel('Time [years]', fontsize = 10)
  plt.xticks(fontsize = 9)
  plt.yticks(fontsize = 9)
  plt.xlim(0,250000)
  if xrange:
      plt.xlim(xrange)


  if (sys.argv[1] == 'pdf'):
      plt.savefig('DynamicExample.pdf')
  if (sys.argv[1] == 'png'):
      plt.savefig('DynamicExample.png')
  if show:
      plt.show()
  else:
      plt.close()

#makes the plots
print("Making evolution plot.")
clim_evol('earth', orbit=True,xrange = (0,250000))
