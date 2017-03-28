# Author: Simon Thelin
# Version: 1.3
# Date: 2017-03-24

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import time

# Calculate the accuracy before OOB and cross-validation
def rfc (data, targets):
    print "Lets calculate the accuracy... loading"
    start_time = time.time()
    print "Default RandomForestClassifier(n_estimators=10, max_depth=None, max_features='auto', bootstrap=True)"
    clf = RandomForestClassifier(n_estimators=10, max_depth=None, max_features='auto', bootstrap=True)
    clf.fit(data, targets)
    importances = clf.feature_importances_
    print importances
    y_pred = clf.predict(data)
    accuracy = accuracy_score(targets, y_pred, normalize=True)
    print "Accuracy: ", accuracy * 100
    print "time elapsed: {:.2f}s".format(time.time() - start_time)
    print "-----------------------------------------------------"

# Calculate the accuracy after OOB and cross-validation
def rfc_final(data, targets):
    print "Lets calculate the accuracy... loading"
    start_time = time.time()
    print "RandomForestClassifier(oob_score=True, n_estimators=15, max_depth=None, max_features='auto',min_samples_split=2, min_samples_leaf=5 , bootstrap=True, n_jobs=1)"
    clf = RandomForestClassifier(oob_score=True, n_estimators=15, max_depth=None, max_features='auto',min_samples_split=2, min_samples_leaf=5 , bootstrap=True, n_jobs=1)
    clf.fit(data, targets)
    importances = clf.feature_importances_
    print importances
    y_pred = clf.predict(data)
    accuracy = accuracy_score(targets, y_pred, normalize=True)
    print "Accuracy: ", accuracy * 100
    print "time elapsed: {:.2f}s".format(time.time() - start_time)
    print "-----------------------------------------------------"