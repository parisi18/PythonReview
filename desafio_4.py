#Show primitive type and all possible informations of it

something = input('Put something here: ')

print('The input is: {}'.format(something))
print('This value primitive type is: {}'.format(type(something)))
print('Is something alfanum? {}'.format(something.isalnum()))
print('Is something alfa? {}'.format(something.isalpha()))
print('Is something ascii? {}'.format(something.isascii()))
print('Is something title? {}'.format(something.istitle()))
print('Is something decimal? {}'.format(something.isdecimal()))
print('Is something digit? {}'.format(something.isdigit()))
print('Is something identifier? {}'.format(something.isidentifier()))
print('Is something lower? {}'.format(something.islower()))
print('Is something numeric? {}'.format(something.isnumeric()))
print('Is something space? {}'.format(something.isspace()))
print('Is something printable? {}'.format(something.isprintable()))
print('Is something upper? {}'.format(something.isupper()))
