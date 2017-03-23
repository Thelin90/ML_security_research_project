from processing import getDatasetFromCsv, createJsonFile, setTargets
from support_vector_ml import SML
from cross_validation import crossValidation

dataset1 = getDatasetFromCsv('Logs/harvest00'+ '5' +'.csv')
createJsonFile('Logs/harvest00'+'5'+'.csv', 'Logs/_targets'+'5'+'.json')
targets1=setTargets('Logs/_targets'+'5'+'.json')
bad_targets = targets1.count(1)
#if(bad_targets>0):
    #SML(dataset1, targets1, 0.01, 10)

crossValidation(dataset1, targets1, 0.01, 10)