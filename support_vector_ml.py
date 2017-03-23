from sklearn import svm
from sklearn.metrics import accuracy_score
import time

def SML (data, targets, gammaVal, cVal):
    print "Lets calculate the accuracy... loading"
    start_time = time.time()
    clf = svm.SVC(kernel='rbf',gamma = gammaVal, C = cVal)
    clf.fit(data, targets)
    y_pred = clf.predict(data)
    accuracy = accuracy_score(targets, y_pred, normalize=True)
    print "Accuracy: ", accuracy * 100
    print "time elapsed: {:.2f}s".format(time.time() - start_time)
    print "-----------------------------------------------------"
