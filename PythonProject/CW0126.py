#Cristian Sanchez

minutesRead = {"Kevin": 20, "Oliver": 36, "Mike": 23, "Sean": 52, "Jose": 37, "Tom": 75}

print(minutesRead)

# Adding items
def add_person():
    while True:
        person = input("Please enter your name (Type 'stop' to exit): ")
        if person.lower() == 'stop':
            break

        add_minutes = input(f"Please enter your minutes for {person}: ")
        minutesRead[person.lower()] = int(add_minutes)
        print(f"Added: {{'{person}', '{add_minutes}'}}")

    print("Dictionary: ", minutesRead)

add_person()

# Check item
def check_key(minutesRead, key):
    if key in minutesRead:
        print("Present, ", key)
        print("value =", minutesRead[key])
    else:
        print("Not present")

key1 = "Jake"
key2 = "Kevin"
check_key(minutesRead, key1)
check_key(minutesRead, key2)

# Delete item
def delete_person():
    should_delete = lambda k: minutesRead[k] <= 43
    for key in list(minutesRead.keys()):
        if should_delete(key):
            del minutesRead[key]
    print("Dictionary after deletion:", minutesRead)

delete_person()

# Function returning multiple values
def get_avg(minutesRead):
    total = sum(minutesRead.values())
    avg = total / len(minutesRead) if minutesRead else 0
    return total, avg

# Unpacking list to assign variables
total, avg = get_avg(minutesRead)
print("Total", total)
print("Average", avg)

# Slicing to access list elements
keys_list = list(minutesRead.keys())
print(keys_list[:3])
print(keys_list[-2:])
print(keys_list[:1])