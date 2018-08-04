import numpy as np
P = float(input())
T = float(input())
n1 = int(input())
interest_a=[]
interest_b=[]
period_a=[]
period_b=[]
for i in range(n1):
    interest_i,period_p=input().strip(' ').split(' ')
    interest_a.append(float(interest_i))
    period_a.append(int(period_p))
n2 = int(input())
for i in range(n2):
    interest_i,period_p=input().strip(' ').split(' ')
    interest_b.append(float(interest_i))
    period_b.append(int(period_p))

emi_a=0
emi_b=0
p_a=P
p_b=P

for i in range(n1):
    for _ in range(period_a[i]*12):
        x = 0
        emi=(p_a*interest_a[i]/12)/(1-1/(1+interest_a[i]/12)**(period_a[i]*12))
        x=x+emi
    emi_a = emi_a + x
    p_a = P - x
for i in range(n2):
    for _ in range(period_b[i]*12):
        x = 0
        emi=(p_b*interest_b[i]/12)/(1-1/(1+interest_b[i]/12)**(period_b[i]*12))
        x=x+emi
    emi_b = emi_b + x
    p_b = P - x
if(emi_a < emi_b):
    print("Bank A")
else:
    print("Bank B")