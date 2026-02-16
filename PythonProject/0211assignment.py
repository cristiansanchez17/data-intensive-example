try:
    a = open('mytext.txt')
    b = a.readline()
except FileNotFoundError:
    file_path = 'mynewtext.txt'
    with open(file_path, "w") as f:
        f.write("Hello, since there was no file to open, I created a file "
                "for you.")
    print(f"File '{file_path}' has been created successfully")