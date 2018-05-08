import numpy as np
import math

#files = ["S1F9XXXX.ASC",
#         "S2F8XXXX.ASC",
#         "S3F7XXXX.ASC",
#         "S4F6XXXX.ASC",
#         "S5F5XXXX.ASC",
#         "S6F4XXXX.ASC",
#         "S7F3XXXX.ASC",
#         "S8F2XXXX.ASC",
#         "S9F1XXXX.ASC"]

files = ["S4F6T251.ASC",
        "S4F6T300.ASC",
        "S4F6T349.ASC",
        "S4F6T400.ASC",
        "S4F6T450.ASC",
        "S4F6T500.ASC",
        "S4F6T550.ASC",
        "S4F6T600.ASC"]

temps = [251, 300, 349, 400, 450, 500, 550, 600]

fout = open("3feladat.txt",'w')
for f in range(len(files)):
    listOfDatas = np.loadtxt(files[f], delimiter=',')
    peak = 0
    for i in listOfDatas:
        if peak < i[1]:
            peak = i[1]
    fout.write("{} {} {}\n".format(temps[f], peak, 1/peak))
    print("Peak of the '{}' is {}".format(files[f], peak))

