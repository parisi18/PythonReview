#generate random queue from the students list

from random import shuffle

std_one = input('Enter the student name: ')
std_two = input('Enter the student name: ')
std_three = input('Enter the student name: ')
std_four = input('Enter the student name: ')

#getting together all students for queue structuring
list = [std_one, std_two, std_three, std_four]

#shuffle the queue
shuffle(list)

print('The queue is: {}'.format(list))