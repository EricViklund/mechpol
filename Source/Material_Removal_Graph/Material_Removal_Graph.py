# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

Data = pd.read_csv('C:/Users/Eric Viklund/Documents/Nb3Sn/Nb3Sn_Mechanical_Polishing/Mechanical_Polishing_Manuscript/Figures/Source/Material_Removal_Graph/Data/Material_Removal.txt',
                   sep = None,
                   header=0)

Tumbling_Duration = (Data['Tumbling_Duration'],Data['Tumbling_Duration.1'].dropna())
Sample_Thickness = (Data['Thickness'],Data['Thickness.1'].dropna())

mm = 0.0393701
fig, ax = plt.subplots(figsize=(86*mm,80*mm),dpi=1200)

ax.set_ylim(0,3.5)

ax.scatter(Tumbling_Duration[0],Sample_Thickness[0],c='m',marker='x',label='Felt Cubes')
m, b = np.polyfit(Tumbling_Duration[0],Sample_Thickness[0], deg=1)
ax.axline(xy1=(0, b),slope=m,c='m',ls='--',label=f'{-1000*m:.0f} nm/hour')

ax.scatter(Tumbling_Duration[1],Sample_Thickness[1],c='y',marker='x',label='Wooden Spheres')
m, b = np.polyfit(Tumbling_Duration[1],Sample_Thickness[1], deg=1)
ax.axline(xy1=(0, b),slope=m,c='y',ls='--',label=f'{-1000*m:.0f} nm/hour')

ax.legend(loc='lower center')

ax.set_xlabel('Tumbling Duration in Hours')
ax.set_ylabel('$Nb_{3}Sn$ Film Thickness [μm]')

ax.yaxis.set_major_formatter(ScalarFormatter())
ax.yaxis.set_minor_formatter(ScalarFormatter())
ax.tick_params(axis='both', which='major', labelsize=10)
ax.tick_params(axis='both', which='minor', labelsize=8)