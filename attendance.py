
from datetime import date

students = {}

# Add Student
def add_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ")

    students[roll] = {
        "name": name,
        "attendance": []
    }

    print("Student added successfully!")


# View Students
def view_students():
    if not students:
        print("No students found!")
        return

    print("\n--- Student Details ---")

    for roll, details in students.items():
        print("Roll Number:", roll)
        print("Name:", details["name"])
        print("----------------------")


# Mark Attendance
def mark_attendance():
    roll = input("Enter Roll Number: ")

    if roll not in students:
        print("Student not found!")
        return

    status = input("Enter P for Present or A for Absent: ").upper()

    if status == "P":
        students[roll]["attendance"].append("Present")
        print("Attendance marked: Present")

    elif status == "A":
        students[roll]["attendance"].append("Absent")
        print("Attendance marked: Absent")

    else:
        print("Invalid attendance status!")


# View Attendance
def view_attendance():
    roll = input("Enter Roll Number: ")

    if roll not in students:
        print("Student not found!")
        return

    attendance = students[roll]["attendance"]

    print("\nStudent Name:", students[roll]["name"])
    print("Total Classes:", len(attendance))
    print("Present:", attendance.count("Present"))
    print("Absent:", attendance.count("Absent"))

    if len(attendance) > 0:
        percentage = attendance.count("Present") / len(attendance) * 100
        print("Attendance Percentage:", round(percentage, 2), "%")
    else:
        print("No attendance records found!")


# Main Menu
while True:
    print("\n===== COLLEGE ATTENDANCE MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Mark Attendance")
    print("4. View Attendance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        mark_attendance()

    elif choice == "4":
        view_attendance()

    elif choice == "5":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice! Please try again.")
