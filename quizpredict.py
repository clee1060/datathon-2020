import numpy as np
import sklearn
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
from scipy.stats import pearsonr
import statistics
import pickle
import sys
from tkinter import *
from tkinter.ttk import *

#!/usr/bin/env python

from tkinter import *

from tkinter.ttk import *

window = Tk()

window.title("Principal Indicators of Divorce")
window.geometry('600x250')
window.configure(background = "gray")

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()

selected = IntVar()

rad1_1 = Radiobutton(window, text='1', value=0, variable=var1)
rad2_1 = Radiobutton(window, text='2', value=1, variable=var1)
rad3_1 = Radiobutton(window, text='3', value=2, variable=var1)
rad4_1 = Radiobutton(window, text='4', value=3, variable=var1)
rad5_1 = Radiobutton(window, text='5', value=4, variable=var1)

rad1_2 = Radiobutton(window, text='1', value=0, variable=var2)
rad2_2 = Radiobutton(window, text='2', value=1, variable=var2)
rad3_2 = Radiobutton(window, text='3', value=2, variable=var2)
rad4_2 = Radiobutton(window, text='4', value=3, variable=var2)
rad5_2 = Radiobutton(window, text='5', value=4, variable=var2)

rad1_3 = Radiobutton(window, text='1', value=0, variable=var3)
rad2_3 = Radiobutton(window, text='2', value=1, variable=var3)
rad3_3 = Radiobutton(window, text='3', value=2, variable=var3)
rad4_3 = Radiobutton(window, text='4', value=3, variable=var3)
rad5_3 = Radiobutton(window, text='5', value=4, variable=var3)

def predict(q35, q36, q40):

    clf = pickle.load(open("svmweb.p", 'rb'))
    response = [[q35, q36, q40]]

    result = clf.predict(response)

    return(result)

def clicked():
    print(int(var1.get()), int(var2.get()), int(var3.get()))
    divorce = predict(int(var1.get()), int(var2.get()), int(var3.get()))
    if divorce:
        div = Label(window, text="   You're getting a divorce  ").grid(column=0, row=8)
    else:
        div = Label(window, text="You're not getting a divorce").grid(column=0, row=8)



btn_1 = Button(window, text="Click Me", command=clicked)
a_1 = Label(window ,text = "35. I can insult my spouse when we argue.").grid(row = 0,column = 0)
rad1_1.grid(column=1, row=0)
rad2_1.grid(column=2, row=0)
rad3_1.grid(column=3, row=0)
rad4_1.grid(column=4, row=0)
rad5_1.grid(column=5, row=0)

btn_2 = Button(window, text="Click Me", command=clicked)
a_2 = Label(window ,text = "36. I can humiliate my spouse when we argue.").grid(row = 2,column = 0)
rad1_2.grid(column=1, row=2)
rad2_2.grid(column=2, row=2)
rad3_2.grid(column=3, row=2)
rad4_2.grid(column=4, row=2)
rad5_2.grid(column=5, row=2)

btn_3 = Button(window, text="Click Me", command=clicked)
a_3 = Label(window ,text = "40. I start to argue with my spouse before I know what's going on.").grid(row = 4,column = 0)
rad1_3.grid(column=1, row=4)
rad2_3.grid(column=2, row=4)
rad3_3.grid(column=3, row=4)
rad4_3.grid(column=4, row=4)
rad5_3.grid(column=5, row=4)
btn_3.grid(column=0, row=6)

window.mainloop()


#
# print("On a scale of 1 to 5, to what degree do you agree with the following statements?\n")
# print("I can insult my spouse during our discussions")
# q35 = float(input("Response: "))
# while q35 not in [1, 2, 3, 4, 5]:
#     q35 = float(input("Please enter an integer between 1 and 5: "))
#
# print("I can be humiliating during discussions with my spouse")
# q36 = float(input("Response: "))
# while q36 not in [1, 2, 3, 4, 5]:
#     q36 = float(input("Please enter an integer between 1 and 5: "))
#
# print("I am just starting a discussion with my spouse before I know what's going on")
# q40 = float(input("Response: "))
# while q40 not in [1, 2, 3, 4, 5]:
#     q40 = float(input("Please enter an integer between 1 and 5: "))
#
# result = predict(q35-1, q36-1, q40-1)
#
# if result == 1:
#     print("You will get divorced!")
# else:
#     print("You will not get divorced!")