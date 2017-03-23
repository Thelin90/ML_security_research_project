from sklearn import svm
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis, LinearDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import time

from sklearn.neighbors import KNeighborsClassifier


def rfc (data, targets):
    print "Lets calculate the accuracy... loading"
    start_time = time.time()
    #clf = svm.SVC(kernel='rbf',gamma = gammaVal, C = cVal)

    clf = RandomForestClassifier(n_estimators=(5), max_depth=None, max_features='auto', bootstrap=True)
    #clf = RandomForestClassifier(n_estimators=500, min_samples_leaf=100, n_jobs=-1, random_state=1, max_depth=None, max_features='auto', bootstrap=True)
    clf.fit(data, targets)
    y_pred = clf.predict(data)
    accuracy = accuracy_score(targets, y_pred, normalize=True)
    print "Accuracy: ", accuracy * 100
    print "time elapsed: {:.2f}s".format(time.time() - start_time)
    print "-----------------------------------------------------"
