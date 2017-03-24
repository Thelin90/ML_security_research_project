import time
from sklearn.utils import shuffle
from sklearn.cross_validation import StratifiedKFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from print_result import plot_hist

# Author: Simon Thelin
# Version: 1.3
# Date: 2017-03-24
# SML: RandomForestClassifier
# Cross-validation: K-fold cross validation
#
# crossValidation will check how well the given model is able to get trained by some data and then predict data it has not seen.
def crossValidation(data, targets):
    data_plot = []

    start_time = time.time()
    clf_rf = RandomForestClassifier(n_estimators=20, max_depth=None, max_features='auto', bootstrap=True, min_samples_split=10, min_samples_leaf=1, n_jobs=-1)
    clf_rf = clf_rf.fit(data, targets)

    importances = clf_rf.feature_importances_
    print importances

    print "n_e: ", 20
    print "min_sample_split: ", 10
    print "min_sample_leaf: ", 1
    print "min_weight_fraction_leaf: 0.0"
    print "max_depth None"
    for i in range(10):
        X, y = shuffle(data, targets, random_state=i)
        skf = StratifiedKFold(y, 20)
        val = cross_val_score(clf_rf, X, y, cv=skf) * 100
        print val
        for j in range(10):
            data_plot.append(val[j])
        print "time elapsed: {:.2f}s".format(time.time() - start_time)

    plot_hist(data_plot)