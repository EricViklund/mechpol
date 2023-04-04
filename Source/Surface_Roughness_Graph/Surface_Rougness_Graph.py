# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import os

Data = np.loadtxt('C:/Users/Eric Viklund/Documents/Nb3Sn/Nb3Sn_Mechanical_Polishing/Mechanical_Polishing_Manuscript/Figures/Source/Surface_Roughness_Graph/Data/Surface_Roughness.txt')

Tumbling_Duration = Data[:,0]
Polished_Rq = Data[:,1]
Shiny_Nb3Sn = Data[:,2]
EP_Nb = Data[:,3]
As_coated_Nb3Sn = Data[:,4]


mm = 0.0393701
fig, (ax1, ax2) = plt.subplots(2,1,figsize=(86*mm,180*mm),dpi=1200)
ax1.set_yscale('log')
ax1.set_ylim(10,500)

ax1.scatter(Tumbling_Duration,Polished_Rq,c='c',marker='x',label='Polished $Nb_{3}Sn$')
ax1.plot(Tumbling_Duration,As_coated_Nb3Sn,'b--',label='As-coated $Nb_{3}Sn$')
ax1.plot(Tumbling_Duration,Shiny_Nb3Sn,'m--',label='Thin Coated $Nb_{3}Sn$')
ax1.plot(Tumbling_Duration,EP_Nb,'y--',label='Electropolished Nb')

ax1.legend(loc='upper right',fontsize=8)

ax1.set_xlabel('Tumbling Duration in Hours')
ax1.set_ylabel('RMS Surface Roughness [nm]')

ax1.yaxis.set_major_formatter(ScalarFormatter())
# ax1.yaxis.set_minor_formatter(ScalarFormatter())
ax1.tick_params(axis='both', which='major', labelsize=10)
# ax1.tick_params(axis='both', which='minor', labelsize=7)

#%%

data_folder = "C:/Users/Eric Viklund/Documents/Nb3Sn/Nb3Sn_Mechanical_Polishing/Mechanical_Polishing_Manuscript/Figures/Source/Surface_Roughness_Graph/Data/Height_Maps/"
files = sorted(os.listdir(data_folder))
pixel_size = 0.112072

ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.set_xlabel('Wavelength [µm]')
ax2.set_ylabel('Amplitude [$µm^3$]')
# ax2.set_ylim(1e-7,1e0)
ax2.set_xlim(2e-1,1e2)
# ax2.grid(which='both')

for file in files:
    # plt.figure()
    data = np.loadtxt(data_folder+file, skiprows=20, delimiter=',', quotechar='"')
    # plt.imshow(data)
    resolution = data.shape
    
    # plt.figure()
    PSD_2D = np.square(np.abs(np.fft.fft2(data)))/(resolution[0]*resolution[1])
    PSD_2D_shifted = np.roll(PSD_2D,(int(resolution[0]/2),int(resolution[1]/2)),axis=(0,1))
    # plt.imshow(PSD_2D_shifted,norm=mpl.colors.LogNorm())
    
   
    PSD = np.mean(PSD_2D,axis=1)
    frequencies = np.fft.fftfreq(PSD.shape[0],pixel_size)[1:int(PSD.shape[0]/2)]
    wavelength = 1/frequencies
    PSD = (PSD[1:int(PSD.shape[0]/2)]+np.flip(PSD[int(PSD.shape[0]/2):-1]))/2
    ax2.plot(wavelength,PSD,)

labels = ('Initial Coating','2 Hours','4 Hours','6 Hours','8 Hours','Electropolished Nb','Thin Coated $Nb_{3}Sn$')
ax2.legend(labels,loc='lower right',fontsize=8)

