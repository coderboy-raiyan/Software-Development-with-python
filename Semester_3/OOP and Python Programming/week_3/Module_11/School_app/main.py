from School import School, Classroom, Subject
from Persons import Student, Teacher


def main():
    school = School("Nawab habibullah", "UTTARA")
    eight = Classroom("eight")
    nine = Classroom("nine")
    ten = Classroom("ten")

    school.add_classroom(eight)
    school.add_classroom(nine)
    school.add_classroom(ten)

    abul = Student("abul khan", eight)
    babul = Student("babul khan", eight)
    kabul = Student("kabul khan", eight)
    school.student_admission(abul)
    school.student_admission(babul)
    school.student_admission(kabul)

    # Subjects
    accounting_teacher = Teacher("Miraz Hossain")
    accounting = Subject("Accounting", accounting_teacher)
    eight.add_subject(accounting)

    print(school)


if __name__ == "__main__":
    main()
