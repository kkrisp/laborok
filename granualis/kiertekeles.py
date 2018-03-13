import matplotlib.pyplot as plt
import numpy as np
import sys
import math
import scipy.optimize
from scipy.optimize import curve_fit
# nincs meg a dugattyu surlodasa...

# latszolagos tomeg fuggese a valodi tomegetol
oszlop_tomege = []
pohar_tomege = 3 # gram
poharnyi_muanyag = np.average([18, 19, 18])
poharnyi_koles = np.average([106, 104, 102])
poharnyi_koles = poharnyi_koles/5-pohar_tomege

print(poharnyi_koles)

# kivalasztott meres:
this = 0 
meres_nevek = ['pohar', 'tolcser', 'finom']

def atlagot_plottol(j):
    adatsor_neve = meres_nevek[j] + '_atlag.dat'
    adatok = np.loadtxt(adatsor_neve, skiprows=1)
    plt.plot( (adatok[:,0])*poharnyi_koles, adatok[:,1], 'r+', label= meres_nevek[j])

def errorbart_plottol(j):
    adatsor_neve = meres_nevek[j] + '_atlag.dat'
    adatok = np.loadtxt(adatsor_neve, skiprows=1)
    err = [5]*len(adatok[:,0])
    plt.errorbar( (adatok[:,0])*poharnyi_koles, adatok[:,1], err, ms=5, marker='o',color='b',capsize=5,ls='')

def funct(m, m_0, m_inf):
    return m_0 + m_inf * ( 1-np.exp(-m/m_inf) )

def illeszt(j):
    adatsor_neve = meres_nevek[j] + '_atlag.dat'
    adatok = np.loadtxt(adatsor_neve, skiprows=1)
    x = [i*poharnyi_koles for i in adatok[:,0] ]
    y = [i                for i in adatok[:,1] ]

    err = [5]*len(x)
    popt, pcov = curve_fit(funct, x, y, p0=[50,125])
    poptwe, pcovwe = curve_fit(funct, x, y, p0=popt,sigma=err)
    tt = tt = np.arange(0, 25*poharnyi_koles, 1)
    plt.plot( tt, funct(tt, *poptwe), 'b', label='illesztes' )
    #plt.plot([0,25*poharnyi_koles], [poptwe[0]+poptwe[1], poptwe[0]+poptwe[1]], '--', label=r'$m_{\infty}$' )
    print(poptwe)

def surlodast_szamol(m, c, a_list):
    mu_list = []
    for a in a_list:
        b = np.sqrt(c**2 - a**2)
        mu_list.append(a/b)
    return np.average(mu_list)

# adatok betoltese...
# az elso oszlop a beletett poharak szama, a masik a mert tomeg
# az elso sor a fejlec, azt kihagyjuk
adatok = np.loadtxt("finom_atlag.dat", skiprows=1)

# az elso oszlopot beszorozzuk egy pohar tomegevel ...
# ... ezzel megkapjuk az oszlop valodi tomeget
#plt.plot( (adatok[:,0])*poharnyi_anyag, adatok[:,1], lw=0.8, color='#999999', label=str(1) + '.meres')

#for i in range(10):
#    plt.plot(adatok[:,2+(i*2)], (adatok[:,1+(i*2)])**4, label=str(i+1) + '.meres')
#plt.legend(loc="upper left")

asdasd = adatok[:,0]
uveglap_hossza = 24.8
emeles_magassaga = [7, 6.9, 7.1]
mu = surlodast_szamol(1, uveglap_hossza, emeles_magassaga)
print(mu)

this = 1
illeszt(this)
atlagot_plottol(this)
#atlagot_plottol(1)
#atlagot_plottol(2)

plt.grid(True)
#plt.ylim(0, 220)
plt.xlabel('valós tömeg (g)', fontsize=12)
plt.ylabel('mért tömeg (g)', fontsize=12)
#plt.legend(loc='upper left')
plt.show()
