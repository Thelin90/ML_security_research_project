# Author: Simon Thelin
# Version: 1.3
# Date: 2017-03-24

import matplotlib.pyplot as plt

# Print the cross-validation result in a histogram
def plot_hist(histData):
    plt.hist(histData, bins=100)
    plt.title("RandomForestClassifier with K-fold cross validation: 90% train and 10% split")
    plt.xlabel("Accuracy in percent")
    plt.ylabel("Frequency")
    plt.gcf()
    plt.show()
