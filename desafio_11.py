#calculate how much paint would you need for wall painting

height = float(input('Wall height: '))
width = float(input('Wall width: '))

#wall area in m^2
wall_area = height * width

print('Knowing that each 1L paints 2m^2')

#paint needed
paint_needed = wall_area / 2

print('You would need {}L for complete wall painting'.format(paint_needed))