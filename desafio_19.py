#pick a up a random bad luck student from four students to erase the black board

import random

std_one = input('Enter the student name: ')
std_two = input('Enter the student name: ')
std_three = input('Enter the student name: ')
std_four = input('Enter the student name: ')

#getting together all students on the hell's hall
list = [std_one, std_two, std_three, std_four]

#the one
bad_luck_student = random.choice(list)

print('The bad luck one is: {}'.format(bad_luck_student))