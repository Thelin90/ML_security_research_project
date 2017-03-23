from processing import getDatasetFromCsv, createJsonFile, setTargets
from random_forest_classifier import rfc
from cross_validation import crossValidation
import socket

for i in range(8):
    dataset1 = getDatasetFromCsv('Logs/harvest00'+str(5)+'.csv')

    createJsonFile('Logs/harvest00'+str(5)+'.csv', 'Logs/_targets'+str(5)+'.json')

    targets1=setTargets('Logs/_targets'+str(5)+'.json')
    bad_targets = targets1.count(1)

    if (bad_targets>0):
        print "------------------"
        print "Bad targets found"
        rfc(dataset1, targets1)
        crossValidation(dataset1, targets1)

