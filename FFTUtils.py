"""
Utility functions for FFT
"""

# import packages and print some version information

import matplotlib.pyplot as plt
import numpy as np
import time
import os
import peakutils 
import msvcrt
import pandas as pd
import sys
from datetime import datetime

class FFT:
    
    '''fft and plot'''

    def __init__(self, inputData, log_rate = 200000.0):
        self.data = inputData
        self.data = self.data - np.mean(self.data)
        self.log_rate = log_rate
       
    
    def FFT(self, fmin = 20, fmax= 450):
        n =int(len(self.data))
        k = np.arange(n, step = 1)
        T = n/self.log_rate
        frq = k/T # two sides frequency range
        frq = frq[range(int(n/2))] # one side frequency range

        # trim frq
        keepInd = (frq > fmin) & (frq < fmax)
        frqKeep = frq[keepInd]

        Y = np.fft.fft(self.data)/n # fft computing and normalization
        Y = Y[range(int(n/2))]

        # remove Y that is outside the frequency rang of interest
        Ykeep = Y[keepInd]



        # calculate top frequency
        ind = np.argpartition(abs(Ykeep), -4)[-4:]
        # Find highest point on the spectrum
        peakFrq = frqKeep[ind[::-1]]
        pwr = (abs(Ykeep)[ind[::-1]])

        domPK = [x for (y,x) in sorted(zip(pwr,peakFrq), reverse = True)][0]

        domPkPwr = pwr[peakFrq == domPK]

        self.frq = frq
        self.peakFrq = peakFrq
        self.pwr = pwr
        self.domPK = domPK
        self.domPkPwr = domPkPwr 
        self.Y = Y



    def plotFFT(self, fmin =0, fmax = 1000):
        f = plt.figure(figsize=(15,4))
        ax1 = f.add_subplot(121)
        ax1.plot(np.array(range(len(self.data)))/ float(self.log_rate), self.data)
        ax1.set_ylabel("Signal")
        ax1.set_xlabel("time (s)")


        # create subplot 2
        ax2 = f.add_subplot(122)
        ax2.plot(self.frq,abs(self.Y),'r')
        ax2.plot(self.peakFrq,self.pwr, 'ro')
        ax2.set_xlim(fmin, fmax)
        ax2.set_ylabel('power')
        ax2.set_xlabel('frequency')
        ax2.plot(self.domPK, self.domPkPwr,'o', color = 'black', markersize = 5)
        ax2.annotate(str(self.domPK) + ' Hz', 
                 xy=(self.domPK, self.domPkPwr), 
                 xytext=(self.domPK + 40, 
                         self.domPkPwr- 0.0001), size = 12)
        plt.tight_layout()
        plt.show()