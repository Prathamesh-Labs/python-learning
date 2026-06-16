students = []

while True:
    print("\n===== Student Performance Analyser =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Show Average")
    print("4. Show Topper")
    print("5. Show Lowest Scorer")
    print("6. Student Count")
    print("7. Exit")

    choice = input("Enter command (1-7): ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = float(input("Enter marks obtained: "))

        student = {
            "name": name,
            "marks": marks
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            for student in students:
                print(student["name"], "-", student["marks"])

    elif choice == "3":
        if len(students) == 0:
            print("No students found.")
        else:
            total = 0
            for student in students:
                total += student["marks"]

            average = total / len(students)
            print("Average Marks:", average)

    elif choice == "4":
        if len(students) == 0:
            print("No students found.")
        else:
            topper = max(students, key=lambda x: x["marks"])
            print("Topper:", topper["name"])
            print("Marks:", topper["marks"])

    elif choice == "5":
        if len(students) == 0:
            print("No students found.")
        else:
            lowest = min(students, key=lambda x: x["marks"])
            print("Lowest Scorer:", lowest["name"])
            print("Marks:", lowest["marks"])

    elif choice == "6":
        print("Total Students:", len(students))

    elif choice == "7":
        print("Thank you for using Student Performance Analyser!")
        break

    else:
        print("Invalid choice. Please enter 1-7.")