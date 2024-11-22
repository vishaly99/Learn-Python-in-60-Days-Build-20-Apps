#Exercise 1
"""def liters_to_m3(liters):
    m3=liters/1000
    return m3"""

#Exercise 2

"""def strength(password):
    count = 0
    res=any(chr.isdigit() for chr in password)
    res1=any(chr.isupper() for chr in password)
    res2=len(password) >= 8
    if res==True and res1==True and res2==True:
        return "Strong Password"
    else:
        return "Weak Password"

print(strength("Vishal123"))"""

#answer 2

"""def strength(password):

    result = {}

    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False
    print(result)
    digit = False
    uppercase = False

    for i in password:
        if i.isdigit():
            digit = True
        if i.isupper():
            uppercase = True

    result["digits"] = digit
    result["upper-case"] = uppercase
    print(result)
    if all(result.values()):
        return "Strong Password"
    else:
        return "Weak Password"

print(strength("Vishal123"))"""

#Exercise 3
"""def foo(list):
    average=sum(list)/len(list)
    print(average)

foo([10,20, 30, 40])"""

#Exercise 4

"""def foo(person):
    return f"Hi {person}"

print(foo("vishal"))"""

#Exercise 5

"""def foo(str1,str2):
    return f"{str1}{str2}"

print(foo('hello','hi'))"""

#Exercise 6
def foo(str1):
    return f"Hi {str1.capitalize()}"

print(foo('john'))