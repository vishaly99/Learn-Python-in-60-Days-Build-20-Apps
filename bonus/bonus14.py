from bonus.conveter14 import convert
from bonus.parser14 import parse

feet_inches=input("Enter the feet and inches:")

parsed=parse(feet_inches)

result= convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

if result<1:
    print("Kis is too small")
else:
    print("Kid can use the slide")
