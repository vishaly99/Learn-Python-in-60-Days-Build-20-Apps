#Exercise 1
"""try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    area = value / total_value * 100
    print(f'That is {area}%')

except ValueError:
    print("Please enter a number")"""

#Exercise 2

"""try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    area = value / total_value * 100
    print(f'That is {area}%')

except ZeroDivisionError:
    print("Your total value cannot be zero")"""

#Exercise 3

"""colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:
    if color>50:
        print(color)"""

#Exercise 4

"""passwords = ["acasd9983k", "34aiufaac99", "98jjanf", "afjj879"]
for password in passwords:
    if len(password)<8:
        print(password)"""

#Exercise 5

"""filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]

for filename in filenames:
    data=filename.replace(".txt","")
    print(data)"""

#Exercise 6

"""filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]

for filename in filenames:
    data=filename.replace(".txt","")
    print(data.capitalize())"""

"""filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]

for filename in filenames:
    print(filename[:-4].capitalize())"""