import pandas as pd
import numpy as np
import warnings
#from sympy import *

fusion_data = pd.read_csv("OHIP-by-Month-PCrvenkovski.csv")
fusion = pd.DataFrame(fusion_data)
cols = [9, 10, 11, 18, 37]
cols[:] = [x - 1 for x in cols]
fusion = fusion[fusion.columns[cols]]
practitionerData = fusion[fusion['Practice Type'] == 'PRACTITIONERS']
# print(practitionerData.head())
physicianData = fusion[fusion['Practice Type'] == 'PHYSICIANS']
# print(physicianData.head())

# ==========================================================================================================#
dCode1000 = fusion[(fusion['OHIP Diagnosis Code'] >= 000) & (fusion['OHIP Diagnosis Code'] <= 1000)]
dCode7000 = fusion[(fusion['OHIP Diagnosis Code'] > 1000) & (fusion['OHIP Diagnosis Code'] <= 7000)]
dCode8000 = fusion[(fusion['OHIP Diagnosis Code'] > 7000)]

# ==========================================================================================================#

dCode1000M = dCode1000[(dCode1000['Sex'] == 'M')]
dCode1000F = dCode1000[(dCode1000['Sex'] == 'F')]

dCode7000M = dCode7000[(dCode7000['Sex'] == 'M')]
dCode7000F = dCode7000[(dCode7000['Sex'] == 'F')]

dCode8000M = dCode8000[(dCode8000['Sex'] == 'M')]
dCode8000F = dCode8000[(dCode8000['Sex'] == 'F')]

# ==========================================================================================================#

dCode1000Practitioner = practitionerData[(practitionerData['OHIP Diagnosis Code'] >= 000) & (practitionerData['OHIP Diagnosis Code'] <= 1000)]
dCode7000Practitioner = practitionerData[(practitionerData['OHIP Diagnosis Code'] > 1000) & (practitionerData['OHIP Diagnosis Code'] <= 7000)]
dCode8000Practitioner = practitionerData[(practitionerData['OHIP Diagnosis Code'] > 7000)]

dCode1000Physician = physicianData[(physicianData['OHIP Diagnosis Code'] >= 000) & (physicianData['OHIP Diagnosis Code'] <= 1000)]
dCode7000Physician = physicianData[(physicianData['OHIP Diagnosis Code'] > 1000) & (physicianData['OHIP Diagnosis Code'] <= 7000)]
dCode8000Physician = physicianData[(physicianData['OHIP Diagnosis Code'] > 7000)]

# ==========================================================================================================#

dCode1000PractitionerM = dCode1000Practitioner[(dCode1000Practitioner['Sex'] == 'M')]
dCode1000PractitionerF = dCode1000Practitioner[(dCode1000Practitioner['Sex'] == 'F')]

dCode7000PractitionerM = dCode7000Practitioner[(dCode7000Practitioner['Sex'] == 'M')]
dCode7000PractitionerF = dCode7000Practitioner[(dCode7000Practitioner['Sex'] == 'F')]


dCode8000PractitionerM = dCode8000Practitioner[(dCode8000Practitioner['Sex'] == 'M')]
dCode8000PractitionerF = dCode8000Practitioner[(dCode8000Practitioner['Sex'] == 'F')]


dCode1000PhysicianM = dCode1000Physician[(dCode1000Physician['Sex'] == 'M')]
dCode1000PhysicianF = dCode1000Physician[(dCode1000Physician['Sex'] == 'F')]

dCode7000PhysicianM = dCode7000Physician[(dCode7000Physician['Sex'] == 'M')]
dCode7000PhysicianF = dCode7000Physician[(dCode7000Physician['Sex'] == 'F')]

dCode8000PhysicianM = dCode8000Physician[(dCode8000Physician['Sex'] == 'M')]
dCode8000PhysicianF = dCode8000Physician[(dCode8000Physician['Sex'] == 'F')]

# ==========================================================================================================#

totalCount = len(dCode1000) + len(dCode7000) + len(dCode8000)
#
# print("0-1000 counts: ", len(dCode1000))
# print("7000 counts: ", len(dCode7000))
# print("8000 counts: ", len(dCode8000))
#
#
# print("Base 1000 : ", round(len(dCode1000)/totalCount, 8))
# print("Base 7000 : ", round(len(dCode7000)/totalCount, 8))
# print("Base 8000 : ", round(len(dCode8000)/totalCount, 8))
#
#
# print("b(Prac+1000+M)", round(len(dCode1000PractitionerM)/len(practitionerData),8))
# print("b(Prac+1000+F)", round(len(dCode1000PractitionerF)/len(practitionerData),8))

# ==========================================================================================================#

prac1000m = round(len(dCode1000PractitionerM)/len(practitionerData), 8)
prac1000f = round(len(dCode1000PractitionerF)/len(practitionerData), 8)
prac7000m = round(len(dCode7000PractitionerM)/len(practitionerData), 8)
prac7000f = round(len(dCode7000PractitionerF)/len(practitionerData), 8)
prac8000m = round(len(dCode8000PractitionerM)/len(practitionerData), 8)
prac8000f = round(len(dCode8000PractitionerF)/len(practitionerData), 8)

phyc1000m = round(len(dCode1000PhysicianM)/len(physicianData), 8)
phyc1000f = round(len(dCode1000PhysicianF)/len(physicianData), 8)
phyc7000m = round(len(dCode7000PhysicianM)/len(physicianData), 8)
phyc7000f = round(len(dCode7000PhysicianF)/len(physicianData), 8)
phyc8000m = round(len(dCode8000PhysicianM)/len(physicianData), 8)
phyc8000f = round(len(dCode8000PhysicianF)/len(physicianData), 8)

# ==========================================================================================================#

belief1 = [prac1000f, prac1000m, prac7000f, prac7000m]
belief2 = [phyc1000f, phyc1000m, phyc7000f, phyc7000m]

uncertainty1 = 1 - sum(belief1)
uncertainty2 = 1 - sum(belief2)

base_rate_counts = [len(dCode1000), len(dCode7000), len(dCode8000)]
b_Intersection_count = [[len(dCode1000M), len(dCode7000M), len(dCode8000M)],
                        [len(dCode1000F), len(dCode7000F), len(dCode8000F)]]


# interstion function used for relative base rate calculation
# def intersection(lst1, lst2):
#     lst3 = [value for value in lst1 if value in lst2]
#     return lst3

def get_intersection(list1, list2):
    return list1.intersection(list2)


# Variables for limits
# a=Symbol('a')
# b=Symbol('b')

# Objective: Calculate the cumulative fusion of agent 1 & 2's opinions
# Input: Uncertainty values 1 & 2 corresponding to each agent, and the number of
# subsets (the domains/number of opinions each agent will have)
# Belief vectors are used that are assumed to be globally defined arrays
# Output: A cumulative fused opinion (belief & uncertainty values) of agents 1 & 2
# I included the if case for uncertainties both = 0, but commented out because
# I am unsure iff the imported limit function allows for two variables to converge concurrently

def cumulative_fusion(uncertaintyA, uncertaintyB, numSubsets, b1, b2):
    # if uncertaintyA != 0 or uncertaintyB != 0:
    belief_fusion_agenti_agentii =[]
    uncertainty_fusion_agenti_agentii = []
    for i in range(numSubsets):
        bfvalue = ((b1[i] * uncertaintyB) + (b2[i] * uncertaintyA)) / \
                                          (uncertaintyA + uncertaintyB - (uncertaintyA * uncertaintyB))
        belief_fusion_agenti_agentii.append(bfvalue)

        ufvalue = (uncertaintyA * uncertaintyB) / \
                                               (uncertaintyA + uncertaintyB - uncertaintyA * uncertaintyB)
        uncertainty_fusion_agenti_agentii.append(ufvalue)
    return (belief_fusion_agenti_agentii,uncertainty_fusion_agenti_agentii)


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


def average_fusion(uncertaintyA, uncertaintyB, numSubsets, b1, b2):

    # We need global arrays for each agents belief value of each domain values
    # if uncertaintyA != 0 or uncertaintyB != 0:
    average_belief_fusion_agenti_agentii =[]
    average_uncertainty_fusion_agenti_agentii = []
    for i in range(numSubsets):
        average_belief_fusion_agenti_agentii[i] = ((b1[i] * uncertaintyB) + (b2[i] * uncertaintyA)) / (uncertaintyA + uncertaintyB)
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


def relative_base_rates(numSubsets, base_rate_intersection_set, baserate_set, w):
    relative_a_values = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
    for i in range(numSubsets-1):
        for j in range(numSubsets):
            if i == j:
                relative_a_values[i][j] = baserate_set[j]/(baserate_set[j] + w)
            else:
                relative_a_values[i][j] = base_rate_intersection_set[i][j]/(baserate_set[j]+w)
    return relative_a_values
                #find intersection of base rates and jth base rate

# Unfinished


def probability_projection(numSubsets , fused_belief, relative_a_values, xi_base_rate, uncertainty_fullset):
    summation_of_relative_base_rates = 0.0
    k =0
    for i in range(numSubsets-1):
        for j in range(numSubsets):
            summation_of_relative_base_rates = summation_of_relative_base_rates + (relative_a_values[i][j]*fused_belief[k])
            k = k+1

    return summation_of_relative_base_rates + (xi_base_rate*uncertainty_fullset)

#
# print(belief1)
# print(belief2)
#
# print("Uncert 1", uncertainty1)
# print("Uncert 2", uncertainty2)
# print("base rate intersection counts ", b_Intersection_count)

fused_belief_rates = cumulative_fusion(uncertainty1, uncertainty2, len(belief1), belief1, belief2)
final_relative_base_rates = relative_base_rates(len(belief1)-1, b_Intersection_count, base_rate_counts, 3)


x1_base = len(dCode1000)/len(fusion)

# projected_probability_x1 = probability_projection(len(belief1)-1, [0.02, 0.2, 0.28], final_relative_base_rates, x1_base, 0.5)
#
#
# print("fused beliefs ", fused_belief_rates[0])
# print("fused uncertainty ", fused_belief_rates[1])
#
#
# print("Relative base rates ", final_relative_base_rates)
# print("Projectied probability with x1 = ", x1_base, " E(x1) = ", projected_probability_x1)