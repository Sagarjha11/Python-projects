students_marks = {
    'Alice' : 90,
    'Bob' : 80,
    'Carol' : 70,
    'David' : 60,
}

students_name = str(input("Enter student name: "))
if students_name in students_marks:
    print(f"{students_name}'s marks  is : {students_marks[students_name]}")
else:
    print(f"{students_name} not found")