#calculate sin, cosin and tangent of an angle

import math

angle = float(input('Enter an angle: '))

#sin
sin = math.sin(math.radians(angle))

#cos
cos = math.cos(math.radians(angle))

#tangent
tan = math.tan(math.radians(angle))

print('The sin: {:.2f}\n cos: {:.2f}\n tan: {:.2f}\n'.format(sin, cos, tan))