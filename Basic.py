
students = []

for i in range(100):
    print("Enter data for student", i + 1)

    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    student = {
        "Name": name,
        "Roll No": roll,
        "Marks": marks
    }

    students.append(student)

print("\nStored Student Data:\n")

for s in students:
    print(s)
