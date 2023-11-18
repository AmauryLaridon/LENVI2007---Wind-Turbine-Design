#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on November 15 2022

@author: Romain Debroeyer
"""

import BEM
import matplotlib.pyplot as plt
import numpy as np

# global parameters of the turbine 
U = np.array([3,4,5,6,7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]  )
rpm = np.array([7, 7.2, 7.5, 8, 8.5, 9.1, 10.2, 11.4, 11.9, 12.1, 12.1, 12.1, 12.1, 12.1, 12.1, 12.1, 12.1, 12.1, 12.1, 12.1, 12.1, 12.1, 12.1 ])
pitch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 3.83, 6.60, 8.70, 10.45, 12.06, 13.54, 14.92, 16.23, 17.47, 18.70, 19.94, 21.18, 22.35, 23.47])
Omega = rpm * 2 * np.pi/60

# blade data  
B = 3
r =  np.array([2.8667,5.6,8.3333,11.75,15.85,19.95,24.05,28.15,32.25,36.35,40.45,44.55,48.65,52.75,56.1667,58.9,61.6333])
twist =  np.array([13.308,13.308,13.308,13.308,11.48,10.162,9.011,7.795,6.544,5.361,4.188,3.125,2.319,1.526,0.863,0.37,0.106])
chord =  np.array([3.542,3.854,4.167,4.557,4.652,4.458,4.249,4.007,3.748,3.502,3.256,3.01,2.764,2.518,2.313,2.086,1.419])

airfoils = ["Cylinder1","Cylinder1","Cylinder2","DU40_A17","DU35_A17","DU35_A17","DU30_A17","DU25_A17","DU25_A17","DU21_A17","DU21_A17","NACA64_A17","NACA64_A17","NACA64_A17","NACA64_A17","NACA64_A17","NACA64_A17"]

N = len(U)
P = np.zeros(N)
for k in range(N):
    _,_,P[k] = BEM.BEM(U[k],Omega[k],pitch[k],r,twist,chord,B,airfoils)
    print(P[k]*1e-3)

plt.figure('P')
plt.plot(U, P*1e-3)
plt.xlim([0,25])
plt.ylim([0,6000])
plt.xlabel(r"$U$ $[m/s]$")
plt.ylabel(r"$P$ $[kW]$")

