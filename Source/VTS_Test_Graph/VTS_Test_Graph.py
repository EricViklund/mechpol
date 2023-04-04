# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

mpl.rcParams['lines.markersize'] = 2
mpl.rcParams["lines.linewidth"] = 0.5

Data = pd.read_csv('C:/Users/Eric Viklund/Documents/Nb3Sn/Nb3Sn_Mechanical_Polishing/Mechanical_Polishing_Manuscript/Figures/Source/VTS_Test_Graph/VTS_Data.txt',
                   sep = None,
                   header=0)



mm = 0.0393701
fig, ax = plt.subplots(2,1,figsize=(86*mm,120*mm),dpi=1200)

ax[0].scatter(Data['Eacc 4.4K Before CBP'],Data['Qo 4.4K Before CBP'],c='m',marker='o',label='As-coated')
ax[0].scatter(Data['Eacc 4.4K After CBP'],Data['Qo 4.4K After CBP'],c='c',marker='^',label='Polished')
ax[0].scatter(Data['Eacc 4.4K After Recoating'],Data['Qo 4.4K After Recoating'],c='y',marker='+',s=20,label='Re-coated')

ax[0].set_yscale('log')
ax[0].set_xlim(0,17)
ax[0].set_ylim(3e8,2e11)
ax[0].grid()

ax[1].scatter(Data['Eacc 2.0K Before CBP'],Data['Qo 2.0K Before CBP'],c='m',marker='o',label='As-coated')
ax[1].scatter(Data['Eacc 2.0K After CBP'],Data['Qo 2.0K After CBP'],c='c',marker='^',label='Polished')
ax[1].scatter(Data['Eacc 2.0K After Recoating'],Data['Qo 2.0K After Recoating'],c='y',marker='+',s=20,label='Re-coated')

ax[1].set_yscale('log')
ax[1].set_xlim(0,17)
ax[1].set_ylim(3e8,2e11)
ax[1].grid()



ax[0].legend(loc='upper right')

ax[1].set_xlabel('Accelerating Field Strength [MV/m]')
ax[0].set_ylabel('Quality Factor')
ax[1].set_ylabel('Quality Factor')

ax[0].set_title('VTS Temperature: 4.4 K')
ax[1].set_title('VTS Temperature: 2.0 K')

fig.tight_layout()
