import numpy as np
import sklearn
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt

index = np.arange(5)
bar_width = 0.35

divorce = np.loadtxt("divorce.csv", delimiter=";", skiprows=1)

def count (x):
    list = [0,0,0,0,0]
    for num in x:
        list[int(num)] += 1
    return list


q_35_y = [divorce[i][34] for i in range(0, 170) if divorce[i][-1] == 1]
q_36_y = [divorce[i][35] for i in range(0, 170) if divorce[i][-1] == 1]
q_40_y = [divorce[i][39] for i in range(0, 170) if divorce[i][-1] == 1]

q_35_n = [divorce[i][34] for i in range(0, 170) if divorce[i][-1] == 0]
q_36_n = [divorce[i][35] for i in range(0, 170) if divorce[i][-1] == 0]
q_40_n = [divorce[i][39] for i in range(0, 170) if divorce[i][-1] == 0]

question_35_y = count(q_35_y)
question_35_n = count(q_35_n)
question_36_y = count(q_36_y)
question_36_n = count(q_36_n)
question_40_y = count(q_40_y)
question_40_n = count(q_40_n)

# Good
plt.bar(index, question_35_y, bar_width, color="r", label = "Divorced")
plt.bar(index + bar_width, question_35_n, bar_width, color="g", label = "Not Divorced")
plt.title("35. I can insult my spouse during our arguments.")
plt.xlabel("Answer to the Survey Question")
plt.ylabel("Number of People")
plt.legend(["Divorce","No Divorce"])
plt.figure()

plt.bar(index, question_36_y, bar_width, color="r", label = "Divorced")
plt.bar(index + bar_width, question_36_n, bar_width, color="g", label = "Not Divorced")
plt.title("36. I can be humiliating when we argue.")
plt.xlabel("Answer to the Survey Question")
plt.ylabel("Number of People")
plt.legend(["Divorce","No Divorce"])
plt.figure()

plt.bar(index, question_40_y, bar_width, color="r", label = "Divorced")
plt.bar(index+ bar_width, question_40_n, bar_width, color="g", label = "Not Divorced")
plt.title("40. We're just starting an argument before I know what's going on.")
plt.xlabel("Answer to the Survey Question")
plt.ylabel("Number of People")
plt.legend(["Divorce","No Divorce"])
plt.figure()

#Bad
q_6_y = [divorce[i][5] for i in range(0, 170) if divorce[i][-1] == 1]
q_6_n = [divorce[i][5] for i in range(0, 170) if divorce[i][-1] == 0]
q_7_y = [divorce[i][6] for i in range(0, 170) if divorce[i][-1] == 1]
q_7_n = [divorce[i][6] for i in range(0, 170) if divorce[i][-1] == 0]

question_6_y = count(q_6_y)
question_6_n = count(q_6_n)
question_7_y = count(q_7_y)
question_7_n = count(q_7_n)

plt.bar(index, question_6_y, bar_width, color="r", label = "Divorced")
plt.bar(index + bar_width, question_6_n, bar_width, color="g", label = "Not Divorced")
plt.title("6. We don't have time at home as partners.")
plt.xlabel("Answer to the Survey Question")
plt.ylabel("Number of People")
plt.legend(["Divorce","No Divorce"])
plt.figure()

plt.bar(index, question_7_y, bar_width, color="r", label = "Divorced")
plt.bar(index+ bar_width, question_7_n, bar_width, color="g", label = "Not Divorced")
plt.title("7. We are like two strangers who share the same \n environment at home rather than family.")
plt.xlabel("Answer to the Survey Question")
plt.ylabel("Number of People")
plt.legend(["Divorce","No Divorce"])

plt.show()