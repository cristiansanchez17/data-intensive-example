# Cristian Sanchez
from typing import Callable

# set
speed_set = set()
speed_set.add(43)
speed_set.add(65)
speed_set.add(28)
speed_set.add(74)

num_set = len(speed_set)
item_set = list(speed_set)
print(num_set)
print(item_set)

# if-elif-else
speed = int(input("Enter a number: "))
if speed < 25:
    print("You're too slow!")
elif 25 <= speed <= 50:
    print("Right speed!")
else:
    print("You're too fast!")

#loop with break and continue
for i in range(10):
    if i == 7:
        break
    elif i % 2 == 1:
        print(i)
        continue

# Truthiness
r = int(input("Enter a number: "))
less_than_45 = r < 45
if less_than_45:
    print("This number is less than 45!")
else:
    print("This number is not less than 45!")

# Sort
x = sorted([21,35,94,54,33,10,53,64], key = abs, reverse = False)
print(x)

# List Comprehension
acceptable_speed_limit = [x for x in range(25,50) if x % 5 == 0]
print(acceptable_speed_limit)

#zip
driver_names = ["Kevin","Joe","Phil","Andy"]
actual_speed = [29,32,43,48]
driver_speed = [pair for pair in zip(driver_names, actual_speed)]
print(driver_speed)

# Type annotation

from typing import Callable

def twice(repeater: Callable[[str, int], str], message: str) -> str:
    return repeater(message, 2)

def warning_repeater(message: str, n: int) -> str:
    warnings = [message for _ in range(n)]
    return " | ".join(warnings)

assert twice(warning_repeater, "Slow down!") == "Slow down! | Slow down!"
