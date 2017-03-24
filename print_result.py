# Author: Simon Thelin
# Version: 1.3
# Date: 2017-03-24

import matplotlib.pyplot as plt

def plot_hist(histData):
    bins = []
    for i in range(100000):
        if i == 0:
            bins.append(0)
        else:
            bins.append(i/10)

    plt.hist(histData, bins)
    plt.title("RandomForestClassifier with K-fold cross validation implementing 80% train and 20% split the Pareto principle to detect malicious/spamming ip-adresses")
    plt.xlabel("Accuracy in percent")
    plt.ylabel("Correct targets")
    fig = plt.gcf()
    DefaultSize = fig.get_size_inches()
    fig.set_size_inches((DefaultSize[0] * 2, DefaultSize[1]))
    plt.show()
