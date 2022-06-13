import numpy as np  
import pandas as pd
import math

data = pd.DataFrame(data=pd.read_csv('data.csv'))
print(data)

def countPosNeg(data):
    pos = data.iloc[:,-1:].value_counts()['yes']
    neg = len(data) - pos
    return pos, neg

def calcEntropy(pos, neg):
    entropy = -(pos/(pos+neg))*math.log2(pos/(pos+neg)) -(neg/(pos+neg))*math.log2(neg/(pos+neg))

    return entropy

def calcAverageInformation(data):
    # iterate through each attribute (col)
    attribs = data.iloc[:0,:-1].columns.values
    print(attribs)

    for attrib in attribs:
        # get possible values 
        values = data[attrib].unique()

        valueEntropies = pd.DataFrame(0, columns=['p','n','entropy'], index=values)
        print()
        print(attrib)
        print(valueEntropies)

        # iterate through whole dataframe
        for i in data.index:
            print(data['Answer'][i])
            if data['Answer'][i] == 'yes':
                valueEntropies[data[attrib]]['p'] += 1
            elif data['Answer'][i] == 'no':
                valueEntropies[data[attrib]]['n'] += 1

        for value in valueEntropies:
            value['entropy'] = calcEntropy(value['p'], value['n'])
        
        print(valueEntropies)

    return 10

calcAverageInformation(data)  

def calcGain(entropy, avg_info):
    return entropy - avg_info

# data for the total dataset

tot_pos, tot_neg = countPosNeg(data)
tot_entropy = calcEntropy(tot_pos, tot_neg)
print(tot_entropy)

# iterate through dataset and calc pos, neg and entropy vals for each column
