#hypotenuse calculator

import math

op_side = float(input('Enter the opposite side: '))
adj_side = float(input('Enter the adjacent side: '))

#calculating hypotenuse
hyp = math.sqrt(math.pow(op_side, 2) + math.pow(adj_side, 2))

print('Hypotenuse is equal to: {:.2f}'.format(hyp))
