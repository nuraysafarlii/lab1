#19 
import math

x=float(input("Determine x:"))
eps=0.01
N=1
R=1
I=0

while abs(N)>eps:
    N=math.sin(x*R)/R
    R+=2
    I+=N

print(I) 