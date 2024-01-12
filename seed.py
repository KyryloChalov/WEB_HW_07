"""Заповніть отриману базу даних випадковими даними 
(~30-50 студентів, 3 групи, 5-8 предметів, 3-5 викладачів, 
до 20 оцінок у кожного студента з усіх предметів). 
Використовуйте пакет Faker для наповнення."""


from datetime import datetime, date, timedelta
from random import randint, choice
from faker import Faker

from include.models import Teacher, Student, Group, Subject, Grades
from connect_db import session

NUMBER_STUDENTS = 50
NUMBER_TEACHERS = 5
NUMBER_SCORES = 20
MAX_SCORE = 12

GROUPS = ["AA-91", "AA-92", "AA-93"]
SUBJECTS = [
    "Python Core",
    "Python WEB",
    "Python Development",
    "Патерни проєктування",
    "Реляційні бази даних",
    "Асинхронне програмування",
    "Штучний інтелект",
]


def date_range(start: date, end: date) -> list:
    """список днів навчання (прибрано вихідні зі списку дат)"""
    result = []
    current_date = start
    while current_date <= end:
        if current_date.isoweekday() < 6:
            result.append(current_date)
        current_date += timedelta(1)
    return result


def generate_fake_data() -> None:
    """generate fake data"""

    fake_data = Faker(locale="uk_UA")

    def seed_groups() -> None:
        for group in GROUPS:
            session.add(Group(name=group))
        session.commit()

    def seed_teachers() -> None:
        for _ in range(NUMBER_TEACHERS):
            session.add(Teacher(name=fake_data.unique.name()))
        session.commit()

    def seed_students() -> None:
        number_groups = len(GROUPS)
        for _ in range(NUMBER_STUDENTS):
            session.add(
                Student(
                    name=fake_data.unique.name(), group_id=randint(1, number_groups)
                )
            )
        session.commit()

    def seed_subjects() -> None:
        for subject in SUBJECTS:
            session.add(Subject(title=subject, teacher_id=randint(1, NUMBER_TEACHERS)))
        session.commit()

    def seed_grade() -> None:
        end_date = datetime.now().date()
        # calculate start date - 1 of September this year or year before
        offset = 1 if end_date.month <= 9 else 0
        start_date = datetime(datetime.now().year - offset, 9, 1).date()

        number_subjects = len(SUBJECTS)
        date_list = date_range(start_date, end_date)

        for _ in range(int(NUMBER_STUDENTS * NUMBER_SCORES)):
            grade = Grades(
                student_id=randint(1, NUMBER_STUDENTS),
                subject_id=randint(1, number_subjects),
                score=randint(1, 12),
                date=choice(date_list),
            )
            session.add(grade)
        session.commit()

    seed_groups()
    seed_teachers()
    seed_students()
    seed_subjects()
    seed_grade()

if __name__ == "__main__":
    print("generate_fake_data - ", end="")
    generate_fake_data()
    print("OK")
