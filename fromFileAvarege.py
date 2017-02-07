import numpy as np
import urllib.request as urlopen

f = urlopen('https://stepic.org/media/attachments/lesson/16462/boston_houses.csv')

sbux = np.loadtxt(f, skiprows=1, delimiter=",")

print(sbux)
