#string treatment

#This lesson demonstrate how to work with strings
phrase = 'Curso em Vídeo Python'

#The split concept
print(phrase[9])

#Vídeo -> always excluding the last iteration value
print(phrase[9:14])

#Printing while jumping 2 by 2
print(phrase[9:21:2])

#Printing from the beginning
print(phrase[:5])

#Printing from position to final char
print(phrase[15:])

#Print from position 9 jumping 3 by 3
print(phrase[9::3])

#THe phrase lenght
print(len(phrase))

#Count how muchs O's exists into the string Curso em Vídeo Python
print(phrase.count('o'))

#Between char number 0 and 13, how much Os exists?
print(phrase.count('o', 0, 13))

#Tells 'deo' starting position
print(phrase.find('deo'))

