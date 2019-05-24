from .person import Person
from typing import List


class Course:
    def __init__(self, name: str):
        self.name = name
        self.mentors: List[Person] = []
        self.students: List[Person] = []

    @property
    def class_size(self) -> int:
        return len(self.students)

    @property
    def mentor_size(self) -> int:
        return len(self.mentors)

    def add_student(self, person: Person):
        self.students.append(person)

    def remove_student(self, person: Person):
        self.students.remove(person)

    # do not call
    def _set_mentor(self, mentor: Person):
        self.mentors = mentor

    def add_mentor(self, mentor: Person):
        self.mentors.append(mentor)

    def set_mentors(self, *mentors: Person):
        self.mentors = mentors

    def remove_mentor(self, mentor: Person):
        self.mentors.remove(mentor)

    def is_nano_in_class(self, student: Person) -> bool:
        if student in self.students:
            return True
        return False

    def sort_students_alphabetically(self) -> List[Person]:
        s = {ord(student.name[0]): student for i, student in enumerate(self.students)}
        initials_full = [[ord(student.name[0]), student] for i, student in enumerate(self.students)]
        for t in initials_full:
            for index, li in enumerate(initials_full):
                try:
                    if li[0] > initials_full[index + 1][0]:
                        temp = initials_full[index]
                        initials_full[index] = initials_full[index + 1]
                        initials_full[index + 1] = temp
                except IndexError:
                    pass
        return [s[student[0]] for student in initials_full]
