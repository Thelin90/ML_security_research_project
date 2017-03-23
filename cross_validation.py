from sklearn.ensemble import RandomForestClassifier
from processing import getDatasetFromCsv, createJsonFile, setTargets
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split

def crossValidation(data, targets, gammaVal, cVal):

    X_train, X_test, y_train, y_test = train_test_split(data, targets, test_size=0.4, random_state=0)

    clf = svm.SVC(kernel='linear', gamma=gammaVal ,C=cVal).fit(X_train, y_train)
    clf.score(X_test, y_test)
    print clf.score





'''
    clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
    clf.score(X_test, y_test)

    clf = clf_rf = RandomForestClassifier(n_estimators=300, min_samples_leaf=5, n_jobs=1, random_state=70, max_depth = None, max_features='auto', bootstrap=True)
    clf.fit(dataset1, targets1)

    X_folds = np.array_split(dataset1, 3)
    y_folds = np.array_split(targets1, 3)
    scores = list()

    for k in range(3):
        # We use 'list' to copy, in order to 'pop' later on
        X_train = list(X_folds)
        X_test  = X_train.pop(k)
        X_train = np.concatenate(X_train)
        y_train = list(y_folds)
        y_test  = y_train.pop(k)
        y_train = np.concatenate(y_train)
        scores.append(clf.fit(X_train, y_train).score(X_test, y_test))
    print "--------"
    print(scores)
'''