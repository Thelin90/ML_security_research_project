import time

from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier


def crossValidation(data, targets):
    print "Lets do cross validation... loading"
    start_time = time.time()
    clf = RandomForestClassifier(n_estimators=(5), max_depth=None, max_features='auto', bootstrap=True)
    clf.fit(data, targets)
    X_folds = np.array_split(data, 20)
    y_folds = np.array_split(targets, 20)
    scores = list()
    for k in range(20):
        # We use 'list' to copy, in order to 'pop' later on
        X_train = list(X_folds)
        X_test  = X_train.pop(k)
        X_train = np.concatenate(X_train)
        y_train = list(y_folds)
        y_test  = y_train.pop(k)
        y_train = np.concatenate(y_train)
        scores.append(clf.fit(X_train, y_train).score(X_test, y_test))
    print "time elapsed: {:.2f}s".format(time.time() - start_time)
    print scores
    print "-----------------------------------------------------"