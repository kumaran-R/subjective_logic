import pandas as pd
import numpy as np
import warnings
from SubjectiveFusion import cumulative_fusion, average_fusion, probability_projection, relative_base_rates
from operators import deduction_calculate, cumulative_fusion
fusion = pd.read_csv("Sample_dataset.csv")

practitionerData = fusion[fusion['Practice Type'] == 'PRACTITIONERS']
physicianData = fusion[fusion['Practice Type'] == 'PHYSICIANS']

dCode1000 = fusion[(fusion['OHIP Diagnosis Code'] >= 000) & (fusion['OHIP Diagnosis Code'] <= 1000)]
dCode7000 = fusion[(fusion['OHIP Diagnosis Code'] > 1000) & (fusion['OHIP Diagnosis Code'] <= 7000)]
dCode8000 = fusion[(fusion['OHIP Diagnosis Code'] > 7000)]

base1000 = len(dCode1000)/len(fusion)
base7000 = len(dCode7000)/len(fusion)
base8000 = len(dCode8000)/len(fusion)

dCode1000M = dCode1000[(dCode1000['Sex'] == 'M')]
dCode1000F = dCode1000[(dCode1000['Sex'] == 'F')]

dCode7000M = dCode7000[(dCode7000['Sex'] == 'M')]
dCode7000F = dCode7000[(dCode7000['Sex'] == 'F')]

dCode8000M = dCode8000[(dCode8000['Sex'] == 'M')]
dCode8000F = dCode8000[(dCode8000['Sex'] == 'F')]

base1000M = len(dCode1000M)/len(fusion)
base1000F = len(dCode1000F)/len(fusion)
base7000M = len(dCode7000M)/len(fusion)
base7000F = len(dCode7000F)/len(fusion)
base8000M = len(dCode8000M)/len(fusion)
base8000F = len(dCode8000F)/len(fusion)


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

print("Practitioner Data count: ", len(practitionerData))
print("Physician Data count: ", len(physicianData))
print("\n")
print("X1:(0 - 1000) : count = ", len(dCode1000), " ; Base rate = ", base1000)
print("X2:(1000 - 7000) : count = ", len(dCode7000), " ; Base rate = ", base7000)
print("X3:(7000 - 8000) : count = ", len(dCode8000), " ; Base rate = ", base8000)

print("\n")

print("Y1:(0 - 1000)| (M) : count = ", len(dCode1000M), " ; Base rate = ", base1000M)
print("Y2:(0 - 1000)| (F) : count = ", len(dCode1000F), " ; Base rate = ", base1000F)
print("Y3:(1000 - 7000)| (M) : count = ", len(dCode7000M), " ; Base rate = ", base7000M)
print("Y4:(1000 - 7000)| (F) : count = ", len(dCode7000F), " ; Base rate = ", base7000F)
print("Y5:(7000 - 8000)| (M) : count = ", len(dCode8000M), " ; Base rate = ", base8000M)
print("Y6:(7000 - 8000)| (F) : count = ", len(dCode8000F), " ; Base rate = ", base8000F)

print("\n")

print("Practitioner Data")

print("Z1:(0 - 1000)| (M) : count = ", len(dCode1000PractitionerM), " ; Belief rate = ", prac1000m)
print("Z2:(0 - 1000)| (F) : count = ", len(dCode1000PractitionerF), " ; Belief rate = ", prac1000f)
print("Z3:(1000 - 7000)| (M) : count = ", len(dCode7000PractitionerM), " ; Belief rate = ", prac7000m)
print("Z4:(1000 - 7000)| (F) : count = ", len(dCode7000PractitionerF), " ; Belief rate = ", prac7000f)
print("Z5:(7000 - 8000)| (M) : count = ", len(dCode8000PractitionerM), " ; Belief rate = ", prac8000m)
print("Z6:(7000 - 8000)| (F) : count = ", len(dCode8000PractitionerF), " ; Belief rate = ", prac8000f)


print("\n")

print("Physician Data")

print("ZA1:(0 - 1000)| (M) : count = ", len(dCode1000PhysicianM), " ; Belief rate = ", phyc1000m)
print("ZA2:(0 - 1000)| (F) : count = ", len(dCode1000PhysicianF), " ; Belief rate = ", phyc1000f)
print("ZA3:(1000 - 7000)| (M) : count = ", len(dCode7000PhysicianM), " ; Belief rate = ", phyc7000m)
print("ZA4:(1000 - 7000)| (F) : count = ", len(dCode7000PhysicianF), " ; Belief rate = ", phyc7000f)
print("ZA5:(7000 - 8000)| (M) : count = ", len(dCode8000PhysicianM), " ; Belief rate = ", phyc8000m)
print("ZA6:(7000 - 8000)| (F) : count = ", len(dCode8000PhysicianF), " ; Belief rate = ", phyc8000f)

print("\n")

# ==========================================================================================================#

belief1 = [prac1000f, prac1000m, prac7000f, prac7000m, prac8000f, prac8000m]
belief2 = [phyc1000f, phyc1000m, phyc7000f, phyc7000m, phyc8000f, phyc8000m]

uncertainty1 = 1 - sum(belief1)
uncertainty2 = 1 - sum(belief2)

uncertainty_full = 0.5
base_rate_w = 1
base_rate_counts = [len(dCode1000), len(dCode7000), len(dCode8000)]
b_Intersection_count = [[len(dCode1000M), len(dCode7000M), len(dCode8000M)],
                        [len(dCode1000F), len(dCode7000F), len(dCode8000F)]]

print("Agent 1 beliefs : ", belief1)
print("Agent 2 beliefs : ", belief2)
print("\n")
print("Uncertainty Agent 1 : ", uncertainty1)
print("Uncertainty Agent 2 : ", uncertainty2)

print("\n")
fused_belief_rates = cumulative_fusion(uncertainty1, uncertainty2, len(belief1), belief1, belief2)
final_relative_base_rates = relative_base_rates(3, b_Intersection_count, base_rate_counts, base_rate_w)
projected_probability_x1 = probability_projection(3, fused_belief_rates[0],
                                                  final_relative_base_rates, base1000F, uncertainty_full)

projected_probability_x2 = probability_projection(3, fused_belief_rates[0],
                                                  final_relative_base_rates, base1000M, uncertainty_full)

projected_probability_x3 = probability_projection(3, fused_belief_rates[0],
                                                  final_relative_base_rates, base7000F, uncertainty_full)

projected_probability_x4 = probability_projection(3, fused_belief_rates[0],
                                                  final_relative_base_rates, base7000M, uncertainty_full)

projected_probability_x5 = probability_projection(3, fused_belief_rates[0],
                                                  final_relative_base_rates, base8000F, uncertainty_full)

projected_probability_x6 = probability_projection(3, fused_belief_rates[0],
                                                  final_relative_base_rates, base8000M, uncertainty_full)
print("cumulative fused beliefs: ")

print("X1: 0 -1000 , F")
print("X2: 0 -1000 , M")
print("X3: 1000 -7000 , F")
print("X4: 1000 -7000 , M")
print("X5: 7000 -8000 , F")
print("X6: 7000 -8000 , M")



for x in fused_belief_rates[0]:
    print(x)

print("\n")

print("fused uncertainty ", fused_belief_rates[1][0])

print("\n")

print("Relative base rates with W:", base_rate_w)

for x in final_relative_base_rates:
    for y in x:
        print(y)

print("\n")
print("Projected probability with x1 = ", fused_belief_rates[0][0], ", uncertainty(X) = ",
      uncertainty_full, "  E(x1) = ", projected_probability_x1)

print("Projected probability with x2 = ", fused_belief_rates[0][1], ", uncertainty(X) = ",
      uncertainty_full, "  E(x1) = ", projected_probability_x2)
print("Projected probability with x3 = ", fused_belief_rates[0][2], ", uncertainty(X) = ",
      uncertainty_full, "  E(x1) = ", projected_probability_x3)
print("Projected probability with x4 = ", fused_belief_rates[0][3], ", uncertainty(X) = ",
      uncertainty_full, "  E(x1) = ", projected_probability_x4)
print("Projected probability with x5 = ", fused_belief_rates[0][4], ", uncertainty(X) = ",
      uncertainty_full, "  E(x1) = ", projected_probability_x5)
print("Projected probability with x6 = ", fused_belief_rates[0][5], ", uncertainty(X) = ",
      uncertainty_full, "  E(x1) = ", projected_probability_x6)

px = {
    "baserate":0.76,
    "belief":0.22,
    "disbelief":0.58,
    "uncertainty":0.2,
    "projectedproba":0.38
}

pyx = {
    "baserate":0.68,
    "belief":0.7,
    "disbelief":0.15,
    "uncertainty":0.15,
    "projectedproba":0.8
}

pyx1 = {
    "baserate":0.68,
    "belief":0.14,
    "disbelief":0.63,
    "uncertainty":0.23,
    "projectedproba":0.29
}

arg1 = [pyx, pyx1]


dec = deduction_calculate(arg1, px)

print(dec)
