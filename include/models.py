"""Реалізуйте свої моделі SQLAlchemy, для таблиць:
- Таблиця студентів;
- Таблиця груп;
- Таблиця викладачів;
- Таблиця предметів із вказівкою викладача, який читає предмет;
- Таблиця де кожен студент має оцінки з предметів із зазначенням коли оцінку отримано;
"""
from sqlalchemy import Integer, String, ForeignKey, Date

from sqlalchemy.orm import (
    declarative_base,
    Mapped,
    mapped_column,
    relationship,
)

Base = declarative_base()


class Group(Base):
    __tablename__ = "groups"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)


class Student(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    group_id: Mapped[str] = mapped_column("group_id", Integer, ForeignKey("groups.id"))
    group: Mapped["Group"] = relationship(Group)


class Teacher(Base):
    __tablename__ = "teachers"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)


class Subject(Base):
    __tablename__ = "subjects"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    teacher_id: Mapped[str] = mapped_column(
        "teacher_id", Integer, ForeignKey("teachers.id")
    )
    user: Mapped["Teacher"] = relationship(Teacher)


class Grades(Base):
    __tablename__ = "grades"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    student_id: Mapped[str] = mapped_column(
        "student_id", Integer, ForeignKey("students.id", ondelete="CASCADE")
    )
    student: Mapped["Student"] = relationship(Student)
    subject_id: Mapped[str] = mapped_column(
        "subject_id", Integer, ForeignKey("subjects.id", ondelete="CASCADE")
    )
    subject: Mapped["Subject"] = relationship(Subject)
    score: Mapped[int] = mapped_column(Integer, nullable=False, index=True)
    date: Mapped[Date] = mapped_column(Date, nullable=False)


# Base.metadata.create_all(engine)

if __name__ == "__main__":
    print("OK")
