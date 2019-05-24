from .objects.course import Course
from .objects.person import Person


if __name__ == "__main__":
    course = Course("Data Structures")
    test_subjects = [Person(first=s[0], last=s[1]) for s in
                     [["apple", "awef"], ["ppppppp", "gfgag"], ["wdawdaw", "naef"], ["tefefefe", "fwef"]]]
    for subject in test_subjects:
        course.add_student(subject)
    for student in course.sort_students_alphabetically():
        print(student)
