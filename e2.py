import csv
with open("file/data.csv","r") as file:
    data=list(csv.reader(file))

print(data)

city=input("Enter the city: ")

for row in data[1:]:
    if row[0] == city:
        print(row[1])