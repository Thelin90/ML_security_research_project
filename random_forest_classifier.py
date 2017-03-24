# Author: Simon Thelin
# Version: 1.3
# Date: 2017-03-24

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import time

def rfc (data, targets):
    print "Lets calculate the accuracy... loading"
    start_time = time.time()
    print "Default training method: RandomForestClassifier(n_estimators=15, max_depth=None, max_features='auto', bootstrap=True)"
    clf = RandomForestClassifier(n_estimators=15, max_depth=None, max_features='auto', bootstrap=True)
    clf.fit(data, targets)
    importances = clf.feature_importances_
    print importances
    y_pred = clf.predict(data)
    accuracy = accuracy_score(targets, y_pred, normalize=True)
    print "Accuracy: ", accuracy * 100
    print "time elapsed: {:.2f}s".format(time.time() - start_time)
    print "-----------------------------------------------------"

def rfc_final(data, targets):
    print "Lets calculate the accuracy... loading"
    start_time = time.time()
    print "After K-fold cross validating: RandomForestClassifier(n_estimators=20, max_depth=None, max_features='auto', bootstrap=True, min_samples_split=10, min_samples_leaf=1, n_jobs=-1)"
    clf = RandomForestClassifier(n_estimators=20, max_depth=None, max_features='auto', bootstrap=True, min_samples_split=10, min_samples_leaf=1, n_jobs=-1)
    clf.fit(data, targets)
    importances = clf.feature_importances_
    print importances
    y_pred = clf.predict(data)
    accuracy = accuracy_score(targets, y_pred, normalize=True)
    print "Accuracy: ", accuracy * 100
    print "time elapsed: {:.2f}s".format(time.time() - start_time)
    print "-----------------------------------------------------"