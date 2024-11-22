feet_inches=input("Enter the feet and inches:")

def parse(feetinches):
    parts=feetinches.split(" ")
    feet=float(parts[0])
    inches=float(parts[1])
    return {"feet":feet,"inches":inches}

def convert(feet,inches):
    meters=feet * 0.3048 + inches * 0.0254
    return meters

parsed=parse(feet_inches)

result=convert(parsed['feet'],parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

if result<1:
    print("Kis is too small")
else:
    print("Kid can use the slide")
