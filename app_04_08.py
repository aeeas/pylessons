class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


rolf = Student('Rolf', 'MIT')

rolf.marks.append(78)
rolf.marks.append(99)

print(rolf.average())

Student.average('hello')
