#!/usr/bin/env python3

# assume the two positive nonzero integers input by the user are 30 and 35
num1 = 30
num2 = 35

# assign M and N to the two numbers corresponding to the flowchart
M = num1
N = num2

# use temp variable to find GCD
while(num2 != 0):
	temp = num2
	num2 = num1 % num2
	num1 = temp
	
gcd = num1

# end: output the result
print("\n GCD of {0} and {1} = {2}".format(M, N, gcd))