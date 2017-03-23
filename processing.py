#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import json
import netaddr
from itertools import chain
import socket

data=[]
accuracy=0

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
        elif items['notes'] == 'Scanning Host':
            ret_arr.append(0.0) #good
        elif items['notes'] == '':
            ret_arr.append(0.0) #good

    return ret_arr

'''
    Split a file into multiple output files.
    The first line read from 'filename' is a header line that is copied to
    every output file. The remaining lines are split into blocks of at
    least 'size' characters and written to output files whose names
    are pattern.format(1), pattern.format(2), and so on. The last
    output file may be short.
'''
def split_file(filename, pattern, size):
    with open(filename, 'rb') as f:
        header = next(f)
        for index, line in enumerate(f, start=1):
            with open(pattern.format(index), 'wb') as out:
                out.write(header)
                n = 0
                for line in chain([line], f):
                    out.write(line)
                    n += len(line)
                    if n >= size:
                        break

def stringToFloat(arr):
    if(len(arr[4])>0):
        notes = ''.join([(str(ord(x) - 96) if x.isalpha() else x) for x in list(arr[4])])
        notes = ''.join(c for c in notes if c not in '?:!/;.-')
        notes = notes.replace(" ", "")
        notes = float(notes)
        notes = (notes/10000)
        return notes
    else:
        return -3.0

def typeToFloat(arr):
    ipv4 = float(len(arr[1]))
    return ipv4

def dateToFloat(arr):
    date = float(''.join(c for c in arr[5] if c.isdigit()))
    return date

def ipv4ToFloat(arr):
    ip = float(int(netaddr.IPAddress(arr[0])))
    return ip

def fqdnIpToFloat(arr):
    ip = socket.gethostbyname(arr[0])
    ip = ''.join(c for c in ip if c not in '?:!/;.-')
    ip = float(ip)
    return ip

def fqdnToFloat(arr):
    fqdn = float(len(arr[1]) + 1)
    return fqdn

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
                data_arr.append([ipv4ToFloat(row), dateToFloat(row), typeToFloat(row), stringToFloat(row)])
            elif row[1] == 'FQDN':
                data_arr.append([fqdnIpToFloat(row), dateToFloat(row) , fqdnToFloat(row), stringToFloat(row)])
            elif row[1] == '':
                empty_type = float(len(row[1]))
                data_arr.append([-1.0, dateToFloat(row), empty_type, stringToFloat(row)])
    return data_arr


#-------------------------------------------------------------------#

#split_file('Logs/harvest.csv', 'Logs/harvest{0:03d}.csv', 3000000)

#createJsonFile('Logs/harvest007.csv', 'Logs/_targets7.json')
#targets1=setTargets('Logs/_targets7.json')
#SML(dataset1, targets1, 0.01, 10)

'''
X_folds = np.array_split(dataset1, 2)
y_folds = np.array_split(targets1, 2)
scores = list()
for k in range(3):
    # We use 'list' to copy, in order to 'pop' later on
    X_train = list(X_folds)
    X_test = X_train.pop(k)
    X_train = np.concatenate(X_train)
    y_train = list(y_folds)
    y_test = y_train.pop(k)
    y_train = np.concatenate(y_train)
    clf2 = svm.SVC(gamma=0.01, C=10)
    scores.append(clf2.fit(X_train, y_train).score(X_test, y_test))
    print(scores)
'''
#-------------------------------------------------------------------#
'''
All data! Took many hours...
Personal Record for SVC
Rows: 249026
Bad targets: 66908
Accuracy: 98.7961096432
Gamma: 0.01
C: 10

With harvest007.csv ...
Rows: 2976367
Bad targets: 3575
Personal Record for SVC
Accuracy: 99.6130551817
time elapsed: 162.30s
Gamma: 0.01
C: 10
'''