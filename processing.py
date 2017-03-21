#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import os
import json
import numpy as np
from sklearn import svm
from sklearn.metrics import accuracy_score
import netaddr
import errno
import socket


data=[]
accuracy=0

def SML (data, targets, gammaVal, cVal):
    print "inside"
    clf = svm.SVC(gamma = gammaVal, C = cVal)
    clf.fit(data, targets)
    y_pred = clf.predict(data)
    accuracy = accuracy_score(targets, y_pred, normalize=True)
    print "Accuracy: ", accuracy * 100

def createJsonFile(csvFile, jsonFileName):
    csvfile = open(csvFile, 'r')
    jsonfile = open(jsonFileName, 'w')
    reader = csv.DictReader(csvfile)
    for row in reader:
        json.dump(row, jsonfile)
        jsonfile.write('\n')
    jsonfile.close()
    csvfile.close()

def setTargets (fileName):
    arr=[]
    ret_arr=[]
    for line in open(fileName, 'r'):
         arr.append(json.loads(line))

    for items in arr:
        if items['notes'] == 'Malicious Host;Scanning Host':
            ret_arr.append(1.0) #bad
        elif items['notes'] == 'Scanning Host;Malicious Host':
            ret_arr.append(1.0) #bad
        elif items['notes'] == 'Malicious Host':
            ret_arr.append(1.0) #bad
        elif items['notes'] == 'Spamming':
            ret_arr.append(1.0) #bad
        else:
            ret_arr.append(0.0) #good

    return ret_arr

def getDatasetFromCsv (csvFile):
    data_arr = []

    with open(csvFile, 'rb') as f:
        has_header = csv.Sniffer().has_header(f.read(1024))
        f.seek(0)
        reader = csv.reader(f, delimiter=',')

        if has_header:
            next(reader)

        for row in reader:
            if row[1] == 'IPv4':
                data_arr.append([float(int(netaddr.IPAddress(row[0])))])
            elif row[1] == 'FQDN':
                data_arr.append([-1.0])
            elif row[1] == '':
                data_arr.append([-1.0])

    return data_arr


#-------------------------------------------------------------------#
dataset=getDatasetFromCsv('harvest.csv')

# Add the path to the project

createJsonFile('harvest.csv', '_targets.json')

targets=setTargets('_targets.json')

#test = int(netaddr.IPAddress(dataset[0][0]))

#test = float(test)

#print test

print len(dataset)
print len(targets)

test_dataset = []
test_targets = []

for i in range (1, 116404):
    test_dataset.append(dataset[i])
    test_targets.append(targets[i])

print len(test_targets)
print len(test_dataset)

#for i in range(1, 11):
    #for j in range(90, 101):
SML(test_dataset, test_targets, 0.01, 10)
#print "Gamma: ", float((i / 1000.0))
#print "Accuracy: ", accuracy * 100
#print "C: ", j

#-------------------------------------------------------------------#
'''
Personal Record for SVC
Accuracy:
Gamma:
C:
'''