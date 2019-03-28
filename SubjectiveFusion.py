import pandas as pd
import numpy as np
import warnings

fusion_data = pd.read_csv("OHIP-by-Month-PCrvenkovski.csv")
fusion = pd.DataFrame(fusion_data)
cols = [9, 10, 11, 18, 37]
cols[:] = [x - 1 for x in cols]
fusion = fusion[fusion.columns[cols]]
practitionerData = fusion[fusion['Practice Type'] == 'PRACTITIONERS']
# print(practitionerData.head())
physicianData = fusion[fusion['Practice Type'] == 'PHYSICIANS']
# print(physicianData.head())


dCode1000 = fusion[(fusion['OHIP Diagnosis Code'] >= 000) & (fusion['OHIP Diagnosis Code'] <= 1000)]
dCode7000 = fusion[(fusion['OHIP Diagnosis Code'] > 1000) & (fusion['OHIP Diagnosis Code'] <= 7000)]
dCode8000 = fusion[(fusion['OHIP Diagnosis Code'] > 7000)]

dCode1000Practitioner = practitionerData[(practitionerData['OHIP Diagnosis Code'] >= 000) & (practitionerData['OHIP Diagnosis Code'] <= 1000)]
dCode7000Practitioner = practitionerData[(practitionerData['OHIP Diagnosis Code'] > 1000) & (practitionerData['OHIP Diagnosis Code'] <= 7000)]
dCode8000Practitioner = practitionerData[(practitionerData['OHIP Diagnosis Code'] > 7000)]


dCode1000PractitionerM = dCode1000Practitioner[(dCode1000Practitioner['Sex'] == 'M')]
dCode1000PractitionerF = dCode1000Practitioner[(dCode1000Practitioner['Sex'] == 'F')]

totalCount = len(dCode1000) + len(dCode7000) + len(dCode8000)

print("0-1000 counts: ", len(dCode1000))
print("7000 counts: ", len(dCode7000))
print("8000 counts: ", len(dCode8000))


print("Base 1000 : ", round(len(dCode1000)/totalCount, 2))
print("Base 7000 : ", round(len(dCode7000)/totalCount, 2))
print("Base 8000 : ", round(len(dCode8000)/totalCount, 2))


print("b(Prac+1000+M)", round(len(dCode1000PractitionerM)/len(dCode1000Practitioner),2))
print("b(Prac+1000+F)", round(len(dCode1000PractitionerF)/len(dCode1000Practitioner),2))
