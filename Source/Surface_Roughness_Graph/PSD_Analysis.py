#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 13:10:39 2022

@author: eric
"""

import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

data_folder = "C:/Users/Eric Viklund/Documents/Nb3Sn/Nb3Sn_Mechanical_Polishing/Mechanical_Polishing_Manuscript/Figures/Source/Surface_Roughness_Graph/Data/Height_Maps/"
files = sorted(os.listdir(data_folder))
pixel_size = 0.112072
plt.figure()
plt.xscale('log')
plt.xlabel('Wavelength [µm]')
plt.ylabel('Amplitude [$µm^3$]')
plt.grid(which='both')

for file in files:
    # plt.figure()
    data = np.loadtxt(data_folder+file, skiprows=20, delimiter=',', quotechar='"')
    # plt.imshow(data)
    resolution = data.shape
    
    # plt.figure()
    PSD_2D = np.abs(np.fft.fft2(data))
    PSD_2D_shifted = np.roll(PSD_2D,(int(resolution[0]/2),int(resolution[1]/2)),axis=(0,1))
    # plt.imshow(PSD_2D_shifted,norm=mpl.colors.LogNorm())
    
   
    PSD = np.mean(PSD_2D,axis=1)
    frequencies = np.fft.fftfreq(PSD.shape[0],1/pixel_size)[1:int(PSD.shape[0]/2)]
    wavelength = 1/frequencies
    PSD = (PSD[1:int(PSD.shape[0]/2)]+np.flip(PSD[int(PSD.shape[0]/2):-1]))/2
    plt.plot(wavelength,PSD,)

labels = ('Initial Coating','2 hours','4 hours','6 hours','8 hours','Electropolished Nb','Thin Coated $Nb_{3}Sn$')
plt.legend(labels,title='Tumbling Duration')