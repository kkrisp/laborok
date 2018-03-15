import matplotlib.pyplot as plt
import numpy as np
import sys
import math
import scipy.optimize
from scipy.optimize import curve_fit

pohar_tomege = 3 # gram
poharnyi_muanyag = np.average([18, 19, 18]) # gram
poharnyi_koles = np.average([106, 104, 102]) # gram
poharnyi_koles = poharnyi_koles/6-pohar_tomege

meres_nevek = ['pohar', 'tolcser', 'finom', 'muanyag']
meres_anyagok = [poharnyi_koles, poharnyi_koles, poharnyi_koles, poharnyi_muanyag]

def atlagot_plottol(meres):
    adatsor_neve = meres_nevek[meres] + '_atlag.dat'
    adatok = np.loadtxt(adatsor_neve, skiprows=1)
    plt.plot( (adatok[:,0])*meres_anyagok[meres], adatok[:,1], 'r+', label= meres_nevek[meres])

def errorbart_plottol(meres):
    adatsor_neve = meres_nevek[meres] + '_atlag.dat'
    adatok = np.loadtxt(adatsor_neve, skiprows=1)
    err = [5]*len(adatok[:,0])
    plt.errorbar( (adatok[:,0])*meres_anyagok[meres], adatok[:,1], err, ms=5, marker='o',color='b',capsize=5,ls='')

def exp_funct(m, m_0, m_inf):
    return m_0 + m_inf * ( 1-np.exp(-m/m_inf) )

def illeszt(meres):
    adatsor_neve = meres_nevek[meres] + '_atlag.dat'
    adatok = np.loadtxt(adatsor_neve, skiprows=1)
    x = [i*meres_anyagok[meres] for i in adatok[:,0] ]
    y = [i                for i in adatok[:,1] ]

    err = [5]*len(x)
    popt, pcov = curve_fit(exp_funct, x, y, p0=[50,125])
    poptwe, pcovwe = curve_fit(exp_funct, x, y, p0=popt,sigma=err)
    tt = tt = np.arange(0, 26*meres_anyagok[meres], 1)
    plt.plot(tt, exp_funct(tt, *poptwe), color='#55aaffff', label='illesztes' )
    #plt.plot([0,25*meres_anyagok[meres]], [poptwe[0]+poptwe[1], poptwe[0]+poptwe[1]], '--', label=r'$m_{\infty}$' )
    #return poptwe[1]
    z = [ exp_funct(i, *poptwe) for i in x ]
    
    plt.plot(x, z, 'r+')

def szorastszamol(meres):
    adatsor_neve = meres_nevek[meres] + '_atlag.dat'
    adatok = np.loadtxt(adatsor_neve, skiprows=1)

illeszt(1)
plt.show()