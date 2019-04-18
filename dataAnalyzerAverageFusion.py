import pandas as pd
import numpy as np
import warnings
from operators import deduction_calculate, cumulative_fusion, average_fusion
fusion = pd.read_csv("OHIP-by-Month-PCrvenkovski.csv")

practitionerData = fusion[fusion['Practice Type'] == 'PRACTITIONERS']
physicianData = fusion[fusion['Practice Type'] == 'PHYSICIANS']

dataM = fusion[(fusion['Sex'] == 'M')]
dataF = fusion[(fusion['Sex'] == 'F')]

phyM = physicianData[(physicianData['Sex'] == 'M')]
phyF = physicianData[(physicianData['Sex'] == 'F')]

pracM = practitionerData[(practitionerData['Sex'] == 'M')]
pracF = practitionerData[(practitionerData['Sex'] == 'F')]
w = 2

baseM = len(dataM)/(len(fusion)+w)
baseF = len(dataF)/(len(fusion)+w)

pracb1 = len(pracM)/len(practitionerData)
pracb2 = len(pracF)/len(practitionerData)
phycb1 = len(phyM)/len(physicianData)
phycb2 = len(phyF)/len(physicianData)

u1 = 0.2
u2 = 0.2

agent1x1 = {
    "baserate":baseM,
    "belief":pracb1,
    "disbelief":1-(pracb1+u1),
    "uncertainty":u1,
   }

agent2x1 = {
    "baserate":baseM,
    "belief":phycb1,
    "disbelief":1-(phycb1+u2),
    "uncertainty":u2,
   }


agent1x2 = {
    "baserate":baseF,
    "belief":pracb2,
    "disbelief":1-(pracb2+u1),
    "uncertainty":u1,
   }

agent2x2 = {
    "baserate":baseF,
    "belief":phycb2,
    "disbelief":1-(phycb2+u2),
    "uncertainty":u2,
   }

print("Counts M=", len(dataM), " F=", len(dataF))

print("base rates with W = ", w)
print("Base (Male) = ", baseM)
print("Base (Female) = ", baseF)
print("x1=M , x2=F")
print("y1= (0-1000) , y2= (1000<)")


print("Agent 1 = Practitioner ; Agent 2 = Physician")
print("\n")


print("Agent 1  x1 opinions = ", agent1x1)
print("Agent 2  x1 opinions = ", agent2x1)
print("Agent 1  u1 = ", u1, "Agent 1 u2 = ", u2)

print("\n")

print("Agent 1  x2 opinions = ", agent1x2)
print("Agent 2  x2 opinions = ", agent2x2)
print("Agent 1  u1 = ", u1, "Agent 1 u2 = ", u2)
fused_opinions_x1 = average_fusion(agent1x1, agent2x1)
fused_opinions_x2 = average_fusion(agent1x2, agent2x2)

print("\n")

print("fused opinions x1= ",fused_opinions_x1)
print("fused opinions x2= ",fused_opinions_x2)

print("\n")


dCode1000 = fusion[(fusion['OHIP Diagnosis Code'] >= 000) & (fusion['OHIP Diagnosis Code'] <= 1000)]
dCode1000M = dCode1000[(dCode1000['Sex'] == 'M')]
dCode1000F = dCode1000[(dCode1000['Sex'] == 'M')]
base1000M = len(dCode1000M)/(len(fusion)+w)
base1000F = len(dCode1000M)/(len(fusion)+w)

base_not_1000_in_M = 1 - base1000M

dCode1000Practitioner = practitionerData[(practitionerData['OHIP Diagnosis Code'] >= 000) & (practitionerData['OHIP Diagnosis Code'] <= 1000)]
dCode1000Physician = physicianData[(physicianData['OHIP Diagnosis Code'] >= 000) & (physicianData['OHIP Diagnosis Code'] <= 1000)]


dCode1000PractitionerM = dCode1000Practitioner[(dCode1000Practitioner['Sex'] == 'M')]
dCode1000PhysicianM = dCode1000Physician[(dCode1000Physician['Sex'] == 'M')]


dCode1000PractitionerF = dCode1000Practitioner[(dCode1000Practitioner['Sex'] == 'F')]
dCode1000PhysicianF = dCode1000Physician[(dCode1000Physician['Sex'] == 'F')]

prac1000m = round(len(dCode1000PractitionerM)/len(practitionerData), 8)
phyc1000m = round(len(dCode1000PhysicianM)/len(physicianData), 8)


prac1000f = round(len(dCode1000PractitionerF)/len(practitionerData), 8)
phyc1000f = round(len(dCode1000PhysicianF)/len(physicianData), 8)

agent111 = {
    "baserate":base1000M,
    "belief":prac1000m,
    "disbelief":1-(prac1000m+u1),
    "uncertainty":u1,
   }

agent211 = {
    "baserate":base1000M,
    "belief":phyc1000m,
    "disbelief":1-(phyc1000m+u2),
    "uncertainty":u2,
   }


agent121 = {
    "baserate":base_not_1000_in_M,
    "belief": 1-(prac1000m+u1),
    "disbelief":prac1000m,
    "uncertainty":u1,
   }

agent221 = {
    "baserate":base_not_1000_in_M,
    "belief":1-(phyc1000m+u2),
    "disbelief":phyc1000m,
    "uncertainty":u2,
   }





agent112 = {
    "baserate":base1000F,
    "belief":1-(prac1000f+u1),
    "disbelief":prac1000f,
    "uncertainty":u1,
   }

agent212 = {
    "baserate":base1000M,
    "belief":phyc1000m,
    "disbelief":1-(phyc1000m+u2),
    "uncertainty":u2,
   }


agent122 = {
    "baserate":base_not_1000_in_M,
    "belief": (1-(prac1000m+u1)),
    "disbelief":prac1000m,
    "uncertainty":u1,
   }

agent222 = {
    "baserate":base_not_1000_in_M,
    "belief":(1-(phyc1000m+u2)),
    "disbelief":phyc1000m,
    "uncertainty":u2,
   }





agent113 = {
    "baserate":base1000M,
    "belief":prac1000m,
    "disbelief":(1-(prac1000m+u1)),
    "uncertainty":u1,
   }

agent213 = {
    "baserate":base1000M,
    "belief":phyc1000m,
    "disbelief":(1-(phyc1000m+u2)),
    "uncertainty":u2,
   }


agent123 = {
    "baserate":base_not_1000_in_M,
    "belief": (1-(prac1000m+u1)),
    "disbelief":prac1000m,
    "uncertainty":u1,
   }

agent223 = {
    "baserate":base_not_1000_in_M,
    "belief":(1-(phyc1000m+u2)),
    "disbelief":phyc1000m,
    "uncertainty":u2,
   }



agent114 = {
    "baserate":base1000M,
    "belief":prac1000m,
    "disbelief":(1-(prac1000m+u1)),
    "uncertainty":u1,
   }

agent214 = {
    "baserate":base1000M,
    "belief":phyc1000m,
    "disbelief":(1-(phyc1000m+u2)),
    "uncertainty":u2,
   }


agent124 = {
    "baserate":base_not_1000_in_M,
    "belief": (1-(prac1000m+u1)),
    "disbelief":prac1000m,
    "uncertainty":u1,
   }

agent224 = {
    "baserate":base_not_1000_in_M,
    "belief":(1-(phyc1000m+u2)),
    "disbelief":phyc1000m,
    "uncertainty":u2,
   }


fused_opinions_conditional1 = average_fusion(agent111, agent211)
fused_opinions_conditional_not1 = average_fusion(agent121, agent221)



fused_opinions_conditional2 = average_fusion(agent112, agent212)
fused_opinions_conditional_not2 = average_fusion(agent122, agent222)


fused_opinions_conditional3 = average_fusion(agent112, agent212)
fused_opinions_conditional_not3 = average_fusion(agent122, agent222)



fused_opinions_conditional4 = average_fusion(agent112, agent212)
fused_opinions_conditional_not4 = average_fusion(agent122, agent222)



print("Fused Y1|X1 ,",fused_opinions_conditional1)
print("Fused Y1|~X1 ,",fused_opinions_conditional_not1)

print("Fused Y1|X2 ,",fused_opinions_conditional2)
print("Fused Y1|~X2 ,",fused_opinions_conditional_not2)

print("Fused Y2|X1 ,",fused_opinions_conditional3)
print("Fused Y2|~X1 ,",fused_opinions_conditional_not3)

print("Fused Y2|X2 ,",fused_opinions_conditional4)
print("Fused Y2|~X2 ,",fused_opinions_conditional_not4)

print("\n")
deduced_opinions_x1_y1 = deduction_calculate([fused_opinions_conditional1, fused_opinions_conditional_not1],
                                             fused_opinions_x1)

deduced_opinions_x1_y2 = deduction_calculate([fused_opinions_conditional2, fused_opinions_conditional_not2],
                                             fused_opinions_x1)

deduced_opinions_x2_y1 = deduction_calculate([fused_opinions_conditional3, fused_opinions_conditional_not3],
                                             fused_opinions_x2)

deduced_opinions_x2_y2 = deduction_calculate([fused_opinions_conditional4, fused_opinions_conditional_not4],
                                             fused_opinions_x2)
print("\n")
print("Deduced opinions (0-1000,M)", deduced_opinions_x1_y1)
print("Deduced opinions (0-1000,F)", deduced_opinions_x2_y1)
print("Deduced opinions (>1000,M)", deduced_opinions_x1_y2)
print("Deduced opinions (>1000,F)", deduced_opinions_x2_y2)
print("\n")