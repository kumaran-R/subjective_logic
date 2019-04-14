import pandas as pd
import numpy as np
import warnings
from operators import deduction_calculate, cumulative_fusion
fusion = pd.read_csv("OHIP-by-Month-PCrvenkovski.csv")

practitionerData = fusion[fusion['Practice Type'] == 'PRACTITIONERS']
physicianData = fusion[fusion['Practice Type'] == 'PHYSICIANS']

dataM = fusion[(fusion['Sex'] == 'M')]
dataF = fusion[(fusion['Sex'] == 'F')]

phyM = physicianData[(physicianData['Sex'] == 'M')]
phyF = physicianData[(physicianData['Sex'] == 'F')]

pracM = practitionerData[(practitionerData['Sex'] == 'M')]
pracF = practitionerData[(practitionerData['Sex'] == 'F')]
w = 1

baseM = len(dataM)/(len(fusion)+w)
baseF = len(dataF)/(len(fusion)+w)

pracb1 = len(pracM)/len(practitionerData)
pracb2 = len(pracF)/len(practitionerData)
phycb1 = len(phyM)/len(physicianData)
phycb2 = len(phyF)/len(physicianData)

u1 = 1 - (pracb1 + pracb2)
u2 = 1 - (phycb1 + phycb2)

agent1 = {
    "baserate":baseM,
    "belief":pracb1,
    "disbelief":pracb2,
    "uncertainty":u1,
   }

agent2 = {
    "baserate":baseM,
    "belief":phycb1,
    "disbelief":phycb2,
    "uncertainty":u2,
   }

print("Counts M=", len(dataM), " F=", len(dataF))

print("base rates with W = ", w)
print("Base (Male) = ", baseM)
print("Base (Female) = ", baseF)
print("x1=M , x2=F")
print("Agent 1 = Practitioner ; Agent 2 = Physician")
print("Agent 1  x1 belief = ", pracb1, " x2 belief = ", pracb2)
print("Agent 2  x1 belief = ", phycb1, " x2 belief = ", phycb2)
print("Agent 1  u1 = ", u1, "Agent 1 u2 = ", u2)


print("Agent 1 (b,d,u,a) = ", "(", pracb1, pracb2, u1, baseM, ")")
print("Agent 2 (b,d,u,a) = ", "(", phycb1, phycb2, u2, baseM, ")")


fused_opinions = cumulative_fusion(agent1, agent2)

print(fused_opinions)


dCode1000 = fusion[(fusion['OHIP Diagnosis Code'] >= 000) & (fusion['OHIP Diagnosis Code'] <= 1000)]
dCode1000M = dCode1000[(dCode1000['Sex'] == 'M')]
base1000M = len(dCode1000M)/(len(fusion)+w)

base_not_1000_in_M = 1 - base1000M

dCode1000Practitioner = practitionerData[(practitionerData['OHIP Diagnosis Code'] >= 000) & (practitionerData['OHIP Diagnosis Code'] <= 1000)]
dCode1000Physician = physicianData[(physicianData['OHIP Diagnosis Code'] >= 000) & (physicianData['OHIP Diagnosis Code'] <= 1000)]


dCode1000PractitionerM = dCode1000Practitioner[(dCode1000Practitioner['Sex'] == 'M')]
dCode1000PhysicianM = dCode1000Physician[(dCode1000Physician['Sex'] == 'M')]

prac1000m = round(len(dCode1000PractitionerM)/len(practitionerData), 8)
phyc1000m = round(len(dCode1000PhysicianM)/len(physicianData), 8)


agent11 = {
    "baserate":base1000M,
    "belief":prac1000m,
    "disbelief":(1-prac1000m),
    "uncertainty":u1,
   }

agent21 = {
    "baserate":base1000M,
    "belief":phyc1000m,
    "disbelief":(1-phyc1000m),
    "uncertainty":u2,
   }


agent12 = {
    "baserate":base_not_1000_in_M,
    "belief": (1-prac1000m),
    "disbelief":prac1000m,
    "uncertainty":u1,
   }

agent22 = {
    "baserate":base_not_1000_in_M,
    "belief":(1-phyc1000m),
    "disbelief":phyc1000m,
    "uncertainty":u2,
   }

fused_opinions_conditional = cumulative_fusion(agent11, agent21)
fused_opinions_conditional_not = cumulative_fusion(agent12, agent22)


print("Conditional 1 ,",fused_opinions_conditional)
print("Conditional 2 ,",fused_opinions_conditional_not)

deduced_opinions = deduction_calculate([fused_opinions_conditional,fused_opinions_conditional_not], fused_opinions)

print("Deduced opinions",deduced_opinions)