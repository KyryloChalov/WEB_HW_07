"""queries:
При запитах використовуємо механізм сесій SQLAlchemy.
 1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
 2. Знайти студента із найвищим середнім балом з певного предмета.
 3. Знайти середній бал у групах з певного предмета.
 4. Знайти середній бал на потоці (по всій таблиці оцінок).
 5. Знайти які курси читає певний викладач.
 6. Знайти список студентів у певній групі.
 7. Знайти оцінки студентів у окремій групі з певного предмета.
 8. Знайти середній бал, який ставить певний викладач зі своїх предметів.
 9. Знайти список курсів, які відвідує певний студент.
10. Список курсів, які певному студенту читає певний викладач.
11. Середній бал, який певний викладач ставить певному студентові.
12. Оцінки студентів у певній групі з певного предмета на останньому занятті.
"""
from sqlalchemy import func, desc, select, and_
from connect_db import session
from include.models import Teacher, Student, Subject, Grades, Group


def query_1():
    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    result = (
        session.query(
            Student.name, func.round(func.avg(Grades.score), 2).label("average_grade")
        )
        .select_from(Grades)
        .join(Student)
        .group_by(Student.id)
        .order_by(desc("average_grade"))
        .limit(5)
        .all()
    )
    return result


def query_2(subject_name):
    # Знайти студента із найвищим середнім балом з певного предмета.
    result = (
        session.query(
            Subject.title,
            Student.name,
            func.round(func.avg(Grades.score), 2).label("average_grade"),
        )
        .select_from(Grades)
        .join(Student)
        .join(Subject)
        .filter(Subject.title == subject_name)
        .group_by(Student.id, Subject.title)
        .order_by(desc("average_grade"))
        .limit(1)
        .all()
    )
    return result


def query_3(subject_name):
    # Знайти середній бал у групах з певного предмета.
    result = (
        session.query(
            Subject.title,
            Group.name,
            func.round(func.avg(Grades.score), 2).label("average_grade"),
        )
        .select_from(Grades)
        .join(Student)
        .join(Subject)
        .join(Group)
        .filter(Subject.title == subject_name)
        .group_by(Subject.title, Group.name)
        .all()
    )
    return result


def query_4():
    # Знайти середній бал на потоці (по всій таблиці оцінок).
    result = (
        session.query(func.round(func.avg(Grades.score), 2).label("average_grade"))
        .select_from(Grades)
        .all()
    )
    return result


def query_5(teacher_id):
    # Знайти які курси читає певний викладач.
    result = (
        session.query(Teacher.name, Subject.title)
        .select_from(Teacher)
        .join(Subject)
        .filter(Subject.teacher_id == teacher_id)
        .all()
    )
    return result


def query_6(group_id):
    # Знайти список студентів у певній групі.
    result = (
        session.query(Group.name, Student.name)
        .select_from(Student)
        .join(Group)
        .filter(Group.id == group_id)
        .order_by(Student.name)
        .all()
    )
    return result


def query_7(group_id, subject_id):
    # Знайти оцінки студентів у окремій групі з певного предмета
    result = (
        session.query(Group.name, Subject.title, Student.name, Grades.score)
        .select_from(Grades)
        .join(Subject)
        .join(Student)
        .join(Group)
        .filter(and_(Grades.subject_id == subject_id, Student.group_id == group_id))
        .order_by(Group.name, Subject.title, Student.name, Grades.score)
        .all()
    )
    return result


def query_8(teacher_id):
    # Знайти середній бал, який ставить певний викладач зі своїх предметів.
    result = (
        session.query(
            Teacher.name,
            func.round(func.avg(Grades.score), 2).label("average_grade"),
        )
        .select_from(Grades)
        .join(Subject)
        .join(Teacher)
        .filter(and_(Grades.subject_id == Subject.id, Subject.teacher_id == teacher_id))
        .group_by(Teacher.id)
        .all()
    )
    return result


def query_9(student_id):
    # Знайти список курсів, які відвідує певний студент.
    result = (
        session.query(Student.name, Subject.title)
        .select_from(Grades)
        .join(Subject)
        .join(Student)
        .filter(and_(Grades.subject_id == Subject.id, Grades.student_id == student_id))
        .group_by(Subject.id, Student.name)
        .all()
    )
    return result


def query_10(student_id, teacher_id):
    # Список курсів, які певному студенту читає певний викладач.
    result = (
        session.query(Student.name, Teacher.name, Subject.title)
        .select_from(Grades)
        .join(Student)
        .join(Subject)
        .join(Teacher)
        .filter(
            and_(
                Grades.student_id == Student.id,
                Grades.subject_id == Subject.id,
                Subject.teacher_id == teacher_id,
                Student.id == student_id,
            )
        )
        .group_by(Student.id, Teacher.id, Subject.id)
        .all()
    )
    return result


def query_11(teacher_id, student_id):
    # Середній бал, який певний викладач ставить певному студентові.
    result = (
        session.query(
            Student.name,
            Teacher.name,
            func.round(func.avg(Grades.score), 2).label("average_grade"),
        )
        .select_from(Grades)
        .join(Subject)
        .join(Teacher)
        .join(Student)
        .filter(
            and_(
                Grades.subject_id == Subject.id,
                Subject.teacher_id == teacher_id,
                Grades.student_id == student_id,
            )
        )
        .group_by(Teacher.id, Student.id)
        .all()
    )
    return result


def query_12(subject_id, group_id):
    # Оцінки студентів у певній групі з певного предмета на останньому занятті.
    subquery = (
        select(Grades.date)
        .join(Student)
        .join(Group)
        .where(and_(Grades.subject_id == subject_id, Group.id == group_id))
        .order_by(desc(Grades.date))
        .limit(1)
        .scalar_subquery()
    )

    result = (
        session.query(
            Subject.title, Group.name, Student.name, Grades.score, Grades.date
        )
        .select_from(Grades)
        .join(Student)
        .join(Subject)
        .join(Group)
        .filter(
            and_(
                Subject.id == subject_id,
                Group.id == group_id,
                Grades.date == subquery,
            )
        )
        .order_by(Student.name, desc(Grades.date))
        .all()
    )
    return result
