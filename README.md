

---

# Grade Book Application

Welcome to the Grade Book Application, a Python-based program designed to manage student records and course enrollments. This application utilizes Object-Oriented Programming (OOP) principles to organize data and provide functionalities for students and courses within an educational context.

## Features Implemented

1. **Add Student**
   - Allows the user to add a new student by providing their email and names.

2. **Add Course**
   - Enables the addition of new courses, including specifying the course name, trimester, and credits.

3. **Register Student for Course**
   - Facilitates the enrollment of a student into a course with a specified grade.

4. **Calculate Ranking**
   - Computes and displays the ranking of students based on their GPA (Grade Point Average), sorted in descending order.

5. **Search by Grade**
   - Allows users to filter and display students whose GPA falls within a specified range (minimum and maximum grade).

6. **Generate Transcript**
   - Creates and displays a transcript for each student, listing all courses they are registered in, along with respective grades and overall GPA.

7. **Exit**
   - Provides an option to gracefully exit the application.

## Programming Techniques Used

- **Object-Oriented Programming (OOP):** Implemented classes (`Student`, `Course`, `GradeBook`) to represent entities and their interactions.
  
- **Data Structures:** Utilized lists and dictionaries to store and manipulate student and course data efficiently.
  
- **Control Structures:** Employed loops (for and while) to iterate over data and provide interactive menu options for user input.
  
- **Exception Handling:** Incorporated error handling to manage potential issues such as invalid inputs or missing data.

## Installation and Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/grade-book.git
   cd grade-book
   ```

2. **Run the Application:**
   ```bash
   python3 main.py
   ```

3. **Follow on-screen prompts to interact with the Grade Book Application.**
   - Use the menu options to add students, courses, register students for courses, calculate rankings, search by grade, generate transcripts, and exit the application.

## Future Enhancements

While the current version of the Grade Book Application provides essential functionalities, here are some potential improvements for future development:

- **Edit and Delete Functionality:** Allow editing and deleting of student and course records.
  
- **User Authentication:** Implement user authentication to secure access and protect student data.
  
- **Database Integration:** Introduce database storage to persist data between sessions and handle larger datasets.

## Challenges Faced

During the development of this application, several challenges were encountered:

- **GPA Calculation:** Ensuring accurate GPA calculation while handling edge cases such as zero credits.
  
- **Input Validation:** Validating user inputs to prevent errors and ensure data integrity.
  
- **User Interface Design:** Designing a clear and intuitive command-line interface (CLI) for user interaction.

## Resources Used

- **Python Documentation:** Referenced for language syntax and built-in functions.
  
- **Stack Overflow:** Used for troubleshooting specific programming challenges and errors encountered during development.
  
- **Educational Tutorials:** Leveraged online tutorials and educational content for best practices in OOP and data management.

---

Feel free to customize this README based on your specific project details and requirements. This document serves as a comprehensive guide for users and developers interacting with the Grade Book Application.
