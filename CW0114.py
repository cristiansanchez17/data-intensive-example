#Cristian Sanchez
def my_name_is(name = "Cristian", message = "Hello, my name is"):
    """This function prints hello message and my name"""
    print(message, name)

my_name_is()
my_name_is("Paul")
help(my_name_is)

names = ["Steve", "Phil","Matt","Jeff","Kevin"]

for value in names:
    result = f"Hello {value}, welcome to my class!"
    print(result)

for value in names:
    starts_with_p = lambda s: s.startswith("P")
    print(starts_with_p(value))
    ends_with_p = lambda s: s.endswith("f")
    print(ends_with_p(value))





















