# Write a program area.py which reads a radius (R, a float) and computes the area A of a circle with radius R.
#  An example of an execution:

 #Provide radius: 2.5
#Corresponding area is 19.6

# Formula A=3.14*r² or A=3.14*r**2
#> A = 3.14*2.5**2
#> A = 3.14*6.25
#> A = 19.6

from math import pi


pi = 3.14

Radius = float(input('Provide radius:'))

Area = pi * Radius * Radius

number = round(Area, 1 )

print("Value of corresponding are is = %.1f" %number)
