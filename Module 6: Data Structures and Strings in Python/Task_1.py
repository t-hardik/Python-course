# Step 1: Create a dictionary with student names and their marks
student_marks = {
    "Alice": 85,
    "Sai": 92,
    "Anshul": 78,
    "Deeksha": 90,
    "Lalitha": 88
}

# Step 2: Ask the user to input a student's name
student_name = input("Enter the student's name: ")

# Step 3 and 4: Retrieve and display marks or an appropriate message
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"Student not found.")
