class PythonClass:
    school = "GGC"
    degree = "IT"
    classname = "ITEC 3160"
    members = []

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.member = "student"
        PythonClass.members.append(self)

    def __str__(self):
        return self.fname + " " + self.lname + " (" + self.member + ")"

class myStudent(PythonClass):
    def __init__(self, fname, lname, graduationYear, creditHours):
        super().__init__(fname, lname)
        self.graduationYear = graduationYear
        self.creditHours = creditHours

    def __str__(self):
        return (f"Hello, my name is {self.fname} {self.lname}.\nI'm currently a student at {self.school} "
                f"who'll graduate in {self.graduationYear}.\nI'm pursuing an {self.degree} degree "
                f"and currently attend {self.classname}.\nI currently have {self.creditHours} credit hours.")

student1 = myStudent("Cristian", "Sanchez", "2027", "75")
print(student1)