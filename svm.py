import numpy as np
import pandas
import sklearn
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

import os
from matplotlib import pyplot as plt

#os.chdir("/Users/matthewbrun/Spring 2020/Datathon/")


divorce = np.loadtxt("divorce.csv", delimiter=";", skiprows=1)


