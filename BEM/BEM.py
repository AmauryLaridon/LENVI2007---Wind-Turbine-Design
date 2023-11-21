# -*- coding: utf-8 -*-
"""
Created on November 15 2022

@author: Romain Debroeyer
"""

import numpy as np
import scipy.interpolate as sp



def BEM(U, Omega, pitch, r, twist, chord, B, airfoils):
    
    pitch *= np.pi / 180
    n =  len(r)
    
    a = np.zeros(n)
    ap = np.zeros(n)
    
    omega = 0.3
    iter_max = 150
    tol = 1e-12 
    
    rho = 1.225
    for i in range(n):
        clinterp,cdinterp = getInterpolator(airfoils[i])
        beta = twist[i] * np.pi / 180
        
        xk_1 = np.array((a[i],ap[i]))
        iiter = 0
        xnew = f(xk_1,U,Omega,r[i],B,chord[i],clinterp,cdinterp,beta,pitch)
        xk = np.copy(xnew)
        for j in (0,1):
            xk[j] = (1-omega)*xk_1[j] + omega*xnew[j]
            
        while (abs(xk[0]-xk_1[0])>tol and abs(xk[1]-xk_1[1])>tol and iiter<iter_max):
            xk_1 = np.copy(xk)
            xnew = f(xk_1,U,Omega,r[i],B,chord[i],clinterp,cdinterp,beta,pitch)
            for j in (0,1):
                xk[j] = (1-omega)*xk_1[j] + omega*xnew[j]           
            iiter = iiter + 1
            
        if(iiter==iter_max):
            print('No convergence for airfoil ' + airfoils[i] +' at wind speed {:d} m/s - residual is {:.2e}'.format(U,max(abs(xk[0]-xk_1[0]),abs(xk[1]-xk_1[1]))))
            xk[0] = 0
            xk[1] = 0
            
        a[i] = xk[0]
        ap[i] = xk[1]
    dT = 4*np.pi*r*rho * U**2 * (1-a) * a
    dQ = 4*np.pi*r**3*rho*U*(1-a)*ap*Omega
    T = np.trapz(dT,r)
    Q = np.trapz(dQ,r)

    P = Omega * Q

    return T,Q,P

def f(x,U,Omega,r,B,c,clinterp,cdinterp,beta,pitch):
# system of equations to be solved
# x[0] = a
# x[1] = a'
    y = np.copy(x)
    yaxis = U * (1-x[0])
    xaxis = Omega*r*(1+x[1])
    phi  = np.arctan2(yaxis,xaxis)

    alpha = phi - beta - pitch

    cl = clinterp(alpha)
    cd = cdinterp(alpha)
    cN = cl*np.cos(phi)+cd*np.sin(phi)
    cT = cl*np.sin(phi)-cd*np.cos(phi)
    
    V_res = np.sqrt((U*(1-x[0]))**2 + (Omega * r * (1+x[1]))**2)

    dT = B * 0.5 * V_res**2 * (cl * np.cos(phi) + cd * np.sin(phi)) * c  # We omit rho and dr in these two equations, because they will be canceled out in the fraction below 
    dQ = B * 0.5 * V_res**2 * (cl * np.sin(phi) - cd * np.cos(phi)) * c * r

    y[0] = dT / (4*np.pi*r*U**2*(1-x[0])) # rho and dr are absent from these two fractions, because they cancel out at the numerator and denominator
    y[1] = dQ / (4*np.pi*r**3*U*(1-x[0])*Omega)

    return y


def getInterpolator(airfoilName):
    """
    
    Parameters
    ----------
    airfoilName : String
        Name of the airfoil - must correspond to the .dat filename of the polar, without the extension

    Returns
    -------
    cl_interp : 
        interpolator for the lift coefficient. Its argument is the angle of attack (alpha) angle 
    cd_interp : TYPE
        interpolator for the drag coefficient. Its argument is the angle of attack (alpha) angle 

    """
    f = open(airfoilName+".dat")    
    lines = f.readlines()    

    angle = np.zeros(0)
    cl = np.zeros(0)
    cd = np.zeros(0)

    index = 0
    startindex = 100    
    for line in lines:
        data = line.split()
        if len(data) > 0 and data[0] == '-180.00':
            startindex = index
        if index >= startindex and len(data)>0:
            
            angle = np.append(angle,float(data[0])* np.pi/180) 
            cl = np.append(cl,float(data[1]))
            cd = np.append(cd,float(data[2])) 

        index += 1
    cl_interp = sp.interp1d(angle,cl)
    cd_interp = sp.interp1d(angle,cd)
    
    return cl_interp,cd_interp

def clcd(clinterp,cdinterp,alpha):
    return clinterp(alpha),cdinterp(alpha)

    