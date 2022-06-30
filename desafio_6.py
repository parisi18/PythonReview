#show numbers double, triple and square root

from math import sqrt
import math

num_a = int(input('Enter a number: '))

#double
double_a  = num_a * 2

#triple
triple_a = num_a * 3

#square root

sqrt_a = num_a**(1/2)

print('The {} double = {}, triple = {} and square root = {:.2f}'.format(num_a, double_a, triple_a, sqrt_a))

