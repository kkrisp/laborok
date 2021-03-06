import matplotlib.pyplot as plt
import numpy as np
import sys
import math
import scipy.optimize
from scipy.optimize import curve_fit

# nincs meg a dugattyu surlodasa...
dugattyu_surlodasa = 1

# mert anyagok tomege
pohar_tomege = 3 # gram
poharnyi_muanyag = np.average([18, 19, 18]) # gram
poharnyi_koles = np.average([106, 104, 102]) # gram
# saccra 6 meropohar lehetett egy muanyag poharban...
poharnyi_koles = poharnyi_koles/6-pohar_tomege

# harom meres van
# 0 - feltoltes poharral
# 1 - feltoltes tolcserrel
# 2 - feltoltes csillapitva (finoman ejtve)
# 3 - muanyag granulatum - feltoltes tolcserrel
meres_nevek = ['pohar', 'tolcser', 'finom', 'muanyag']
meres_anyagok = [poharnyi_koles, poharnyi_koles, poharnyi_koles, poharnyi_muanyag]

# az adatfajlokban az 1. oszlop poharak szama a 2. a mert tomeg
# az elso sor a fejlec, azt kihagyjuk...
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
    print(poptwe)

def surlodast_szamol(m, c, a_list):
    mu_list = []
    for a in a_list:
        b = np.sqrt(c**2 - a**2)
        mu_list.append(a/b)
    return np.average(mu_list)

uveglap_hossza = 24.8
emeles_magassaga = [7, 6.9, 7.1]
mu = surlodast_szamol(1, uveglap_hossza, emeles_magassaga)
print("A surlodas erteke:" , mu)

this = 1
illeszt(this)
atlagot_plottol(this)
#atlagot_plottol(1)
#atlagot_plottol(2)

plt.grid(True)
#plt.ylim(0, 220)
plt.xlabel('valós tömeg (g)', fontsize=12)
plt.ylabel('mért tömeg (g)', fontsize=12)

plt.plot([0, 180], [47, 227], ':k')
small = False
if small:
    sr = np.arange(0, 80, 10)
    plt.plot(sr, sr+43.5, ':k')
    plt.xticks(sr)
    plt.yticks(sr)
    plt.xlim(0, 40)
    plt.ylim(40, 80)
#plt.xticks(np.arange(0, 600, 20))
#plt.legend(loc='upper left')
plt.show()