import pandas as pd
import numpy as np
import warnings
from sympy import *

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

//interstion function used for relative base rate calculation
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

// Variables for limits
a=Symbol('a')
b=Symbol('b')

# Objective: Calculate the cumulative fusion of agent 1 & 2's opinions
# Input: Uncertainty values 1 & 2 corresponding to each agent, and the number of
# subsets (the domains/number of opinions each agent will have)
# Belief vectors are used that are assumed to be globally defined arrays
# Output: A cumulative fused opinion (belief & uncertainty values) of agents 1 & 2
# I included the if case for uncertainties both = 0, but commented out because
# I am unsure iff the imported limit function allows for two variables to converge concurrently
def cumulative_fusion(uncertaintyA, uncertaintyB, numSubsets): //agentBeliefs1, agentBeliefs2
#    if uncertaintyA != 0 or uncertaintyB != 0:
        for (i=1; i<=numSubsets; i++)
            belief_fusion_agenti_agentii[i] = (b1[i] * uncertaintyB + b2[i] * uncertaintyA) / (uncertaintyA + uncertaintyB - uncertaintyA * uncertaintyB)
            uncertainty_fusion_agenti_agentii[i] = (uncertaintyA * uncertaintyB) / (uncertaintyA + uncertaintyB - uncertaintyA * uncertaintyB)
#    else
#        for (i=1; i<=numSubsets; i++)
#            a = uncertaintyA
#            b = uncertaintyB
#            gammaA = b / (a + b)
#            gammaB = a / (a + b)
#            result_of_limit_gammaA = limit(gammaA, a, 0, b, 0)
#            result_of_limit_gammaB = limit(gammaB, a, 0, b, 0)
#            average_belief_fusion_agenti_agentii[i] = result_of_limit_gammaA * b1[i] + result_of_limit_gammaB * b2[i]
#            average_uncertainty_fusion_agenti_agentii[i] = 0

# Objective: Calculate the average fusion of agent 1 & 2's opinions
# Input: Uncertainty values 1 & 2 corresponding to each agent, and the number of
# subsets (the domains/number of opinions each agent will have)
# Belief vectors are used that are assumed to be globally defined arrays
# Output: An average fused opinion (belief & uncertainty values) of agents 1 & 2
# I included the if case for uncertainties both = 0, but commented out because
# I am unsure iff the imported limit function allows for two variables to converge concurrently
def average_fusion(uncertaintyA, uncertaintyB, numSubsets): //agentBeliefs1, agentBeliefs2
    //We need global arrays for each agents belief value of each domain values
#    if uncertaintyA != 0 or uncertaintyB != 0:
        for (i=1; i<=numSubsets; i++)
            average_belief_fusion_agenti_agentii[i] = (b1[i] * uncertaintyB + b2[i] * uncertaintyA) / (uncertaintyA + uncertaintyB)
            average_uncertainty_fusion_agenti_agentii[i] = (2 * uncertaintyA * uncertaintyB) / (uncertaintyA + uncertaintyB)
#    else
#        for (i=1; i<=numSubsets; i++)
#            a = uncertaintyA
#            b = uncertaintyB
#            gammaA = b / (a + b)
#            gammaB = a / (a + b)
#            result_of_limit_gammaA = limit(gammaA, a, 0, b, 0)
#            result_of_limit_gammaB = limit(gammaB, a, 0, b, 0)
#            average_belief_fusion_agenti_agentii[i] = result_of_limit_gammaA * b1[i] + result_of_limit_gammaB * b2[i]
#            average_uncertainty_fusion_agenti_agentii[i] = 0

# I was unable to complete, unsure how to account for the case i=j, and calculate
# the intersection of xi & xj
# Objective: Find all relative base rates
# Input: Number of subsets in the analyzed domain
# Output: All of the relative base rates stored in the array 'relative_a_values'
def relative_base_rates(numSubsets): //agentBeliefs1, agentBeliefs2
    for (i=1; i<=numSubsets; i++)
        for (j=1; j<=numSubsets; i++)
            if i == j: #Unsure if this is a special case or treated the same
                relative_a_values[i][j] = 1
                continue
            else
                relative_a_values[i][j] = 1

# Unfinished
def probability_projection(numSubsets): //agentBeliefs1, agentBeliefs2
    for (i=1; i<=numSubsets; i++)
        for (j=1; j<=numSubsets; i++)
            summation_of_relative_base_rates += relative_a_values[i][j]
