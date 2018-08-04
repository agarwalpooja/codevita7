import math


velocity_1 = int(input())
radius_1 = int(input())
velocity_2 = int(input())
radius_2 = int(input())
n = int(input())

velocity_1,velocity_2 = velocity_1*n, velocity_2*n

distance = math.cos(math.radians(velocity_2-velocity_1))
distance = radius_1**2 + radius_2**2 - 2*radius_1*radius_2*distance
distance = math.sqrt(distance) 
print("%.2f"%round(distance,3),end="")