#Exercise 1

"""def water_state(temperature):
    if temperature<=0:
        return "Solid"
    elif temperature>0 and temperature<100:
        return "Liquid"
    else:
        return "Gas"
print(water_state(-1))"""

#Exercise 2

""""# Define constants for freezing point and boiling point of water
FREEZING_POINT = 0
BOILING_POINT = 100


# Define a function named water_state that takes one parameter: temperature
def water_state(temperature):
    # Check if the temperature is less than or equal to the freezing point
    if temperature <= FREEZING_POINT:
        return "Solid"
        # Check if the temperature is between the freezing point and boiling point
    elif FREEZING_POINT < temperature < BOILING_POINT:
        return "Liquid"
        # Return "Gas" for all other cases
    else:
        return "Gas"
"""
#Exercise 3
def foo(temperature):
    if temperature>25:
        return "Hot"
    elif 25 >= temperature >=15:
        return "Warm"
    else:
        return "Cold"

print(foo(10))