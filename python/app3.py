import json, csv
import numpy as np
import pandas as pd
from collections import defaultdict


df = pd.read_excel('raw_data.xlsx')
df.head()
data = df.fillna(method='ffill')
#data.head()

# output = data.loc[data['Symptom'].str.match(pat = '(UMLS:C0008031_pain chest)|(UMLS:C0004093_asthenia)')]
output = data.loc[data['Symptom'].str.contains("(sleeplessness)|(asthenia)", na=False)]
print(output)
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



disease_list = []
disease_symptom_dict = defaultdict(list)

disease_symptom_count = {}
count = 0


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

# print(list(disease_symptom_dict.items())
df1 = pd.DataFrame(list(disease_symptom_dict.items()), columns=['Disease','Symptom'])
print(df1.to_dict())


# print(df1[df1['Symptom'].str.match("out of breath")])
# #print(df1['Symptom'].filter(like = 'out of breath'))
# # output = df1.loc[df1['Symptom'].str.contains(pat = 'out of breath')] #df1.loc[df1['Symptom'].str.match(pat = 'out of breath')]
# # print(output)
#

"""
"""

"""#f = open( 'disease-symptom-merged.csv', 'r' )
filename ='disease_symptoms.csv'
raw_data = open('disease_symptoms.csv', 'rt')

data = pd.read_csv(filename,encoding='utf-8')

df = pd.DataFrame(data)

#output = df['Symptom'].str.match('C0030552')
output = df.loc[df['Symptom'].str.match(pat = '(UMLS:C0008031_pain chest)|(UMLS:C0004093_asthenia)')]
print(output)
print(type(output.to_dict()))
"""
""""
for x in output:
	if x == True:
		print(x['Disease'])
		"""

"""
spike_cols = [col for col in df. if 'C0030552' in col]
print(list(df.columns))
print(spike_cols)

csvReader = csv.DictReader(f, ['Disease', 'Symptom'])

outputjson = json.dumps( [ row for row in csvReader ] )

myoutputjson = {
	"results" : outputjson
}

print (myoutputjson)



for myindex in myoutputjson['results']:
	print(myindex)"""
