import math


air_den=1.23
radius_a = float(input())
cost_a = float(input())
eff_a = float(input())
radius_b = float(input())
cost_b = float(input())
eff_b = float(input())
budget= float(input())
land= float(input())
wind_speed = float(input())

area_a =2*radius_a*radius_a
area_b = 2*radius_b*radius_b
power_a = ((1/2)*air_den*area_a*(wind_speed**3)*eff_a)/(10**6)
power_b = ((1/2)*air_den*area_b*(wind_speed**3)*eff_b)/(10**6)
count_a1=1
count_b1=1
W_land=land-area_a-area_b
w_budget=budget-cost_b-cost_a
if cost_a < cost_b:
    count=W_land/area_a
    if count*cost_a > w_budget:
        exd_cost=count*cost_a - w_budget
        frac=exd_cost/cost_a
        count=count-frac
    count_a1 += count    
elif cost_a > cost_b :
    count=W_land/area_b
    if count*cost_b > w_budget:
        exd_cost=count*cost_b - w_budget
        frac=exd_cost/cost_b
        count=count-frac
    count_b1 += count    
count_a2=1
count_b2=1
if area_a < area_b:
    count=w_budget/cost_a
    if count*area_a > W_land:
        exd_land=count*area_a - W_land
        frac=exd_land/area_a
        count=count-frac
    count_a2 += count 
elif area_a > area_b:
    count=w_budget/cost_b
    if count*area_b > W_land:
        exd_land=count*area_b - W_land
        frac=exd_land/area_b
        count=count-frac
    count_b2 += count    
power1=(count_a1*power_a)+(count_b1*power_b)
power2=(count_a2*power_a)+(count_b2*power_b)   
if power1 > power2:
    print("%.2f"%round(power1,2))
    print(str(int(count_a1))+' '+str(int(count_b1)))
    print("%.2f"%round((int(count_a1)*power_a)+(int(count_b1)*power_b),2))
elif power1 < power2:
    print("%.2f"%round(power2,2))
    print(str(int(count_a2))+' '+str(int(count_b2)))
    print("%.2f"%round((int(count_a2)*power_a)+(int(count_b2)*power_b),2))
