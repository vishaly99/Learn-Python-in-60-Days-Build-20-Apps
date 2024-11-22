"""The code below tries to write the items of temperatures each in one line in the file.txt list.
However, the code has an error. Try to fix the error."""

#Solution

"""temperatures = [10, 12, 14]
temperatures=[str(temperature)+'\n' for temperature in temperatures]

file = open("../bugfixexercise/file.txt", 'w')

file.writelines(temperatures)
file.close()"""

"""The code below tries to convert all the numbers to integers. 
However, the code has an error. Try to fix the error."""

numbers = [10.1, 12.3, 14.7]
numbers = [int(item) for item in numbers]
print(numbers)