import numpy as np
import math
import matplotlib.pyplot as plt
import sys
from scipy.optimize import curve_fit

def B(x,k,d):
    return -k*d/2 - k*d*x -k/2 + k*x - 1

def C(x,k,d):
    return k*d/4 - k*d*x**2

def f(x,k,d,a):
    return a/(2*k)*(-B(x,k,d)-np.sqrt(B(x,k,d)**2 - 4*k*C(x,k,d)))

# 1% a pipettazas hibaja
# 
l = [522, 528, 528, 528, 526, 528, 528, 527, 528]
errors = []

csucs = [0.4989, 0.8788, 1.2015, 1.4757, 1.4084, 1.1942, 0.9064, 0.5999, 0.2839]

for i in range(len(l)):
    errors.append(0.1-csucs[i]*0.4)
keveres = [(i-5)/10 for i in range(1, 10)]


#errors = [1]*9

fout = open("feladat2.txt",'w')
for i in range(len(csucs)):
    fout.write("{} {} {}\n".format(keveres[i], csucs[i], errors[i]))