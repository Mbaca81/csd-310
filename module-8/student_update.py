import json
import os
import sys
import tkinter as tk
from tkinter import messagebox

# -------------------------------
# Function to print student list
# -------------------------------
def print_students(student_list):
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : "
              f"ID = {student['Student_ID']} , "
              f"Email = {student['Email']}")


# -------------------------------
# Resolve JSON path relative to this script
# -------------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))
json_file = os.path.join(script_dir, "Student.json")

try:
    with open(json_file, "r") as file:
        students = json.load(file)
except FileNotFoundError:
    print(f"Error: Student.json not found at {json_file}")
    print(f"Current working directory: {os.getcwd()}")
    sys.exit(1)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON in {json_file}: {e}")
    sys.exit(1)

# -------------------------------
# Print Original List
# -------------------------------
print("\n===== ORIGINAL STUDENT LIST =====\n")
print_students(students)

# -------------------------------
# Append New Student (Your Info)
# -------------------------------
new_student = {
    "F_Name": "Martin",
    "L_Name": "Baca",
    "Student_ID": 81657,  # fictional ID
    "Email": "mbaca@my365.bellevue.edu"
}

# Check if student already exists by ID or email
student_exists = any(
    student["Student_ID"] == new_student["Student_ID"] or 
    student["Email"] == new_student["Email"]
    for student in students
)

if not student_exists:
    students.append(new_student)
    print(f"\n✓ Added new student: {new_student['F_Name']} {new_student['L_Name']}")
else:
    print(f"\n✗ Student already exists: {new_student['F_Name']} {new_student['L_Name']}")

# -------------------------------
# Print Updated List
# -------------------------------
print("\n===== UPDATED STUDENT LIST =====\n")
print_students(students)

# -------------------------------
# Write Updated List Back to File
# -------------------------------
# Create a hidden Tkinter window for the dialog
root = tk.Tk()
root.withdraw()  # Hide the window

# Ask user for confirmation
result = messagebox.askyesno(
    "Update Student List",
    f"Do you want to update Student.json with the modified student list?"
)

root.destroy()

if result:
    with open(json_file, "w") as file:
        json.dump(students, file, indent=4)
    print("\nThe Student.json file has been updated successfully.")
else:
    print("\nUpdate cancelled. No changes were made to Student.json.")