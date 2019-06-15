import json, csv
import numpy as np
import pandas as pd
from collections import defaultdict

# Process Disease and Symptom Names
def process_data(data):
    data_list = []
    data_name = data.replace('^','_').split('_')
    n = 1
    for names in data_name:
        if (n % 2 == 0):
            data_list.append(names)
        n += 1
    return data_list

def findMatchingDiseases(args_symptoms):
    df = pd.read_excel('raw_data.xlsx')
    df.head()
    data = df.fillna(method='ffill')


    disease_list = []
    disease_symptom_dict = defaultdict(list)
    disease_symptom_count = {}
    count = 0

    #print(args_symptoms)
    output = data.loc[data['Symptom'].str.contains(args_symptoms, na=False)]

    print(output)
    for idx, row in output.iterrows():
        # Get the Disease Names
        if (row['Disease'] !="\xc2\xa0") and (row['Disease'] != ""):
            disease = row['Disease']
            disease_list = process_data(data=disease)
            count = row['Count of Disease Occurrence']

        # Get the Symptoms Corresponding to Diseases
        if (row['Symptom'] !="\xc2\xa0") and (row['Symptom'] != ""):
            symptom = row['Symptom']
            symptom_list = process_data(data=symptom)
            for d in disease_list:
                for s in symptom_list:
                    disease_symptom_dict[d].append(s)
                disease_symptom_count[d] = count


    df1 = pd.DataFrame(list(disease_symptom_dict.items()), columns=['Disease','Symptom'])

    return(df1.to_dict())





def main():
    # display some lines

    print(findMatchingDiseases("(sleeplessness)|(asthenia)"))
