#!/usr/bin/python3

class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = 0.0

    def calculate_GPA(self):
        total_credits = sum(course['credits'] for course in self.courses_registered)
        if total_credits == 0:
            self.GPA = 0.0
        else:
            total_points = sum(course['credits'] * course['grade'] for course in self.courses_registered)
            self.GPA = total_points / total_credits

    def register_for_course(self, course, grade):
        print(f"Registering {self.names} for course {course.name} with grade {grade}")  # Debug
        self.courses_registered.append({'course': course, 'credits': course.credits, 'grade': grade})
        self.calculate_GPA()


class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits


class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, email, names):
        student = Student(email, names)
        self.student_list.append(student)

    def add_course(self, name, trimester, credits):
        course = Course(name, trimester, credits)
        self.course_list.append(course)

    def register_student_for_course(self, student_email, course_name, grade):
        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            student.register_for_course(course, grade)
        else:
            print(f"Student or course not found. Student: {student_email}, Course: {course_name}")  # Debug

    def calculate_ranking(self):
        students = self.student_list
        for student in students:
            student.calculate_GPA()  # Calculate GPA for each student
        students.sort(key=lambda x: x.GPA, reverse=True)
        return students

    def search_by_grade(self, min_grade, max_grade):
        filtered_students = [student for student in self.student_list if min_grade <= student.GPA <= max_grade]
        return filtered_students

    def generate_transcript(self):
        transcripts = []
        for student in self.student_list:
            transcript = f"Transcript for {student.names} ({student.email}):"
            for course in student.courses_registered:
                transcript += f"\n - {course['course'].name} ({course['credits']} credits): Grade {course['grade']}"
            transcript += f"\nOverall GPA: {student.GPA}\n"
            transcripts.append(transcript)
        return transcripts


def main():
    gradebook = GradeBook()
    print("Welcome to the Grade Book Application!")

    while True:
        print("\nGrade Book Menu:")
        print("\n1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate Ranking")
        print("5. Search by Grade")
        print("6. Generate Transcript")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            gradebook.add_student(email, names)
            print(f"Student {names} with email {email} added successfully.")
        elif choice == '2':
            name = input("Enter course name: ")
            trimester = input("Enter trimester: ")
            credits = int(input("Enter course credits: "))
            gradebook.add_course(name, trimester, credits)
            print(f"Course {name} for trimester {trimester} with {credits} credits added successfully.")
        elif choice == '3':
            email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            gradebook.register_student_for_course(email, course_name, grade)
            print(f"Student {email} registered for course {course_name} with grade {grade}.")
        elif choice == '4':
            rankings = gradebook.calculate_ranking()
            for rank, student in enumerate(rankings, start=1):
                print(f"{rank}. {student.email} - GPA: {student.GPA}")
        elif choice == '5':
            min_grade = float(input("Enter minimum grade: "))
            max_grade = float(input("Enter maximum grade: "))
            students = gradebook.search_by_grade(min_grade, max_grade)
            for student in students:
                print(f"{student.email} - GPA: {student.GPA}")
            print(f"Found {len(students)} students.")
        elif choice == '6':
            transcripts = gradebook.generate_transcript()
            for transcript in transcripts:
                print(transcript)
            print("Transcripts generated successfully.")
        elif choice == '7':
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()

