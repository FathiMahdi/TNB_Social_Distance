import matplotlib.pyplot as plt

import matplotlib.cbook as cbook

import numpy as np
from np import *
import pandas as pd

data = np.genfromtxt("data.csv",delimiter=",",names=['persons','sitting','standing','moving','masks','time'])
for i in rang(0,93):
    plt.plot(i,data['persons'])
