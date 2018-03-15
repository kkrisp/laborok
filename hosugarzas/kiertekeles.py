import matplotlib.pyplot as plt
import numpy as np
import sys
import math
from scipy.optimize import curve_fit

adatok = np.loadtxt("meresi_adatok.dat", skiprows=1)
homerseklet = []
feszultseg = []

# uj tombok, minden paratlan oszlop homerseklet...
# ... es minden paros (a 2.-tol kezdve) feszultseg

for i in range(10):
    for T in adatok[:,1+(i*2)]:
        homerseklet.append(T)
    for U in adatok[:,2+(i*2)]:
        feszultseg.append(U)

# homerseklet atvaltasa kelvinbe
homerseklet = [i+273.15 for i in homerseklet]
# a feszultseg negyedik gyoket vesszuk
feszultseg4 = [pow(i, 1/4) for i in feszultseg]

# latex tablazat generalasa...
fout = open("textable.txt",'w')
fout.write("$T(K)$ & $U (\mu V)$ & $U^{1/4} (\mu V^{1/4})$\\\\ \hline \hline \n")
for p in range(len(homerseklet)):
    fout.write("{:.0f}&{:.0f}&{:.03f}\\\\".format(homerseklet[p], feszultseg[p], feszultseg4[p]))
    if (p+1)%5 == 0:
        fout.write(" \hline \n")
    else:
        fout.write("\n")
fout.close()

# az illesztendo linearis fuggveny
def linear(x, a, b):
    return a + x*b 

# fuggvenyillesztes
popt, pcov = curve_fit(linear, homerseklet, feszultseg4)
perr = np.sqrt(np.diag(pcov))  #A kovariancia mátrix diagonális elemeinek gyöke az illesztés hibája
#lehetne +- 1 hibaval a leolvasas miatt, de ugyanezt adja...

print("A meredeksegre {:.6f} +- {:.6f}-et kaptunk.".format(popt[1], perr[1]) )

# plottolas...
tt = np.arange(200, 850, 1)
plt.xlabel('T (K)', fontsize=13)
plt.ylabel(r'$\sqrt[4]{U}$  ($\sqrt[4]{\mu V}$)', fontsize=13)
plt.plot(tt, linear(tt, *poptwe), 'b')
plt.plot(homerseklet, feszultseg4, 'r+')
plt.xlim(250, 850)
plt.ylim(1.5, 7.5)
plt.grid(True)

#plt.show()             # megjelenites konzolon
#plt.savefig("illesztett.png")  # mentes ... neven