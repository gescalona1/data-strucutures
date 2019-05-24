from people import Course
from people import Person


if __name__ == "__main__":
    course = Course("Data Structures")
    test_subjects = [Person(first=s[0], last=s[1]) for s in
                     [["apple", "awef"], ["ppppppp", "gfgag"], ["wdawdaw", "naef"], ["tefefefe", "fwef"]]]
    for b in test_subjects:
        course.add_student(b)
    for s in course.sort_students_alphabetically():
        print(s.name)
