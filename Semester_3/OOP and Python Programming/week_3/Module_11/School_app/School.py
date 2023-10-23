class School:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        # Composition "has a"
        self.teachers = {}
        self.classrooms = {}

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self, subject, teacher):
        if (subject in self.teachers):
            self.teachers[subject] = teacher

    def student_admission(self, student):
        if (student.classroom.name in self.classrooms):
            self.classrooms[student.classroom.name].add_student(student)
        else:
            print(f"No classroom as named {student.classroom.name}")

    def __repr__(self) -> str:
        print("----------- Classrooms ----------")
        for key, value in self.classrooms.items():
            print(key)

        for key, value in self.classrooms.items():
            print("------------", key, "--------------", end="\n")
            print("---- Students -----")
            for student in value.students:
                print(student.name)

            print("---- Teacher -----")
            for subject in value.subjects:
                print(
                    f"subject name : {subject.name} and teacher : {subject.teacher.name}")
        return ""


class Classroom:
    def __init__(self, name) -> None:
        self.name = name
        self.subjects = []
        # Composition "has a"
        self.students = []

    def add_student(self, student):
        serial_id = f"{self.name}-{len(self.students) + 1}"
        student.id = serial_id
        student.classroom = self.name
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def __str__(self) -> str:
        return f"{self.name}-{len(self.students)}"

    def get_top_students(self):
        pass


class Subject:
    def __init__(self, name, teacher) -> None:
        self.name = name
        self.teacher = teacher
        self.max_marks = 100
        self.pass_marks = 33
