# app to test student class
#

from Student import Student

student1 = Student("Jim", "Business", 3.5, False)
student2 = Student("Peter", "Science", 2, True)

print(student1.gpa)
print(student2.name)

print(student2.on_honor_roll())
