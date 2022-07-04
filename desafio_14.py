#temperature conversor, wich shows farenheit and celcius relation

#celcius temperature
celc_temp = float(input('Enter celcius temperature: '))

#farenheit temperature
faren_temp = ((celc_temp*9)/5) + 32

print('{:.1f}ºC equals to {:.1f}ºF'.format(celc_temp, faren_temp))