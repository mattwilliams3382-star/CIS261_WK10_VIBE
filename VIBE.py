# Matthew Williams
# CIS261
# Vibe Coding
# Student Grade Calculator


class Student:
    def __init__(self, name, student_id, test1, test2, test3):
        self.name = name
        self.student_id = student_id
        self.test_scores = [test1, test2, test3]

    def calculate_average(self):
        return sum(self.test_scores) / len(self.test_scores)

    def calculate_grade(self):
        average = self.calculate_average()

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"


def get_valid_score(test_number):
    while True:
        try:
            score = float(input(f"Enter test score {test_number}: "))

            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100.")

        except ValueError:
            print("Invalid entry. Please enter a number.")


def add_student(students):
    print("\n--- ADD STUDENT ---")

    name = input("Enter student name: ").strip()
    student_id = input("Enter student ID: ").strip()

    # Check for duplicate student ID
    for student in students:
        if student.student_id == student_id:
            print("A student with that ID already exists.")
            return

    test1 = get_valid_score(1)
    test2 = get_valid_score(2)
    test3 = get_valid_score(3)

    student = Student(
        name,
        student_id,
        test1,
        test2,
        test3
    )

    students.append(student)

    print(f"\n{name} was added successfully.")


def view_student_record(students):
    print("\n--- VIEW STUDENT RECORD ---")

    student_id = input("Enter student ID: ").strip()

    for student in students:
        if student.student_id == student_id:
            print("\nStudent Record")
            print("-" * 40)
            print(f"Name: {student.name}")
            print(f"Student ID: {student.student_id}")
            print(f"Test 1: {student.test_scores[0]:.2f}")
            print(f"Test 2: {student.test_scores[1]:.2f}")
            print(f"Test 3: {student.test_scores[2]:.2f}")
            print(f"Average: {student.calculate_average():.2f}")
            print(f"Letter Grade: {student.calculate_grade()}")
            return

    print("Student not found.")


def display_all_students(students):
    print("\n--- ALL STUDENT RECORDS ---")

    if len(students) == 0:
        print("No student records available.")
        return

    print(
        f"{'Name':<20}"
        f"{'ID':<12}"
        f"{'Test 1':>10}"
        f"{'Test 2':>10}"
        f"{'Test 3':>10}"
        f"{'Average':>10}"
        f"{'Grade':>8}"
    )

    print("-" * 80)

    for student in students:
        print(
            f"{student.name:<20}"
            f"{student.student_id:<12}"
            f"{student.test_scores[0]:>10.2f}"
            f"{student.test_scores[1]:>10.2f}"
            f"{student.test_scores[2]:>10.2f}"
            f"{student.calculate_average():>10.2f}"
            f"{student.calculate_grade():>8}"
        )


def class_statistics(students):
    print("\n--- CLASS STATISTICS ---")

    if len(students) == 0:
        print("No student records available.")
        return

    highest_student = max(
        students,
        key=lambda student: student.calculate_average()
    )

    lowest_student = min(
        students,
        key=lambda student: student.calculate_average()
    )

    class_average = sum(
        student.calculate_average()
        for student in students
    ) / len(students)

    print(
        f"Highest Average: "
        f"{highest_student.name} - "
        f"{highest_student.calculate_average():.2f}"
    )

    print(
        f"Lowest Average: "
        f"{lowest_student.name} - "
        f"{lowest_student.calculate_average():.2f}"
    )

    print(f"Class Average: {class_average:.2f}")


def search_student_by_name(students):
    print("\n--- SEARCH STUDENT ---")

    search_name = input("Enter student name: ").strip().lower()

    found = False

    for student in students:
        if search_name in student.name.lower():
            print("\nStudent Found")
            print("-" * 40)
            print(f"Name: {student.name}")
            print(f"Student ID: {student.student_id}")
            print(f"Test 1: {student.test_scores[0]:.2f}")
            print(f"Test 2: {student.test_scores[1]:.2f}")
            print(f"Test 3: {student.test_scores[2]:.2f}")
            print(f"Average: {student.calculate_average():.2f}")
            print(f"Grade: {student.calculate_grade()}")
            found = True

    if not found:
        print("Student not found.")


def save_records(students):
    try:
        with open("student_grades.txt", "w") as file:
            for student in students:
                file.write(
                    f"{student.name}|"
                    f"{student.student_id}|"
                    f"{student.test_scores[0]:.2f}|"
                    f"{student.test_scores[1]:.2f}|"
                    f"{student.test_scores[2]:.2f}|"
                    f"{student.calculate_average():.2f}|"
                    f"{student.calculate_grade()}\n"
                )

        print("\nRecords saved successfully.")

    except OSError:
        print("Error saving student records.")


def load_records():
    students = []

    try:
        with open("student_grades.txt", "r") as file:
            for line in file:
                line = line.strip()

                if line:
                    data = line.split("|")

                    if len(data) >= 5:
                        name = data[0]
                        student_id = data[1]
                        test1 = float(data[2])
                        test2 = float(data[3])
                        test3 = float(data[4])

                        student = Student(
                            name,
                            student_id,
                            test1,
                            test2,
                            test3
                        )

                        students.append(student)

    except FileNotFoundError:
        pass

    except (ValueError, OSError):
        print("There was a problem loading previous records.")

    return students


def display_menu():
    print("\n" + "=" * 50)
    print("STUDENT GRADE CALCULATOR")
    print("=" * 50)
    print("1. Add Student")
    print("2. View Student Record")
    print("3. Display All Students")
    print("4. Class Statistics")
    print("5. Search Student by Name")
    print("6. Save Records")
    print("7. Exit")
    print("=" * 50)


def main():
    students = load_records()

    print("=" * 50)
    print("WELCOME TO THE STUDENT GRADE CALCULATOR")
    print("=" * 50)

    while True:
        display_menu()

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_student_record(students)

        elif choice == "3":
            display_all_students(students)

        elif choice == "4":
            class_statistics(students)

        elif choice == "5":
            search_student_by_name(students)

        elif choice == "6":
            save_records(students)

        elif choice == "7":
            save_records(students)
            print("\nThank you for using the Student Grade Calculator.")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()