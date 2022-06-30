#calculate new revenue price after 5% off

price = float(input('Enter product price: '))

#5% off
five_off = price - (5/100)*price

print('With 5% off: {}R$'.format(five_off))