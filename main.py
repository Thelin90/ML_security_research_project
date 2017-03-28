# Author: Simon Thelin
# Version: 1.3
# Date: 2017-03-24
#
# main.py will start the whole application, run this file and the rest will run smoothly

from processing import getDatasetFromCsv, createJsonFile, setTargets
from random_forest_classifier import rfc, rfc_final
from cross_validation import crossValidation
from OOB_errors_rf import print_oob_error

def main():
    dataset1 = getDatasetFromCsv('Logs/harvest005.csv')

    createJsonFile('Logs/harvest005.csv', 'Logs/_targets5.json')

    targets1 = setTargets('Logs/_targets5.json')
    bad_targets = targets1.count(1)

    print len(dataset1)
    print len(targets1)

    if (bad_targets > 0):
        print "-----------------------------------------------------"
        print "Bad targets found"
        rfc(dataset1, targets1)
        #print_oob_error(dataset1, targets1) #highest error 23.6746941602% with number of estimators to: 172
        crossValidation(dataset1, targets1)
        rfc_final(dataset1, targets1)

if __name__ == "__main__":
    main()