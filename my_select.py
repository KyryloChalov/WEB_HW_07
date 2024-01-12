'''Для запитів оформити окремий файл my_select.py, 
де будуть 10 функцій від select_1 до select_10. 
Виконання функцій повинно повертати результат аналогічний попередньої домашньої роботи. 
'''
from random import randint, choice
from include.colors import GREEN_BACK, GREEN, RESET, GRAY, CYAN
from include.date_to_str import datetime_to_str
import my_queries


NUMBER_STUDENTS = 50
NUMBER_TEACHERS = 5
NUMBER_SCORES = 20

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

query_name = [
"Знайти 5 студентів із найбільшим середнім балом з усіх предметів",
"Знайти студента із найвищим середнім балом з певного предмета",
"Знайти середній бал у групах з певного предмета",
"Знайти середній бал на потоці (по всій таблиці оцінок)",
"Знайти які курси читає певний викладач",
"Знайти список студентів у певній групі",
"Знайти оцінки студентів у окремій групі з певного предмета",
"Знайти середній бал, який ставить певний викладач зі своїх предметів",
"Знайти список курсів, які відвідує певний студент",
"Список курсів, які певному студенту читає певний викладач",
"Середній бал, який певний викладач ставить певному студентові",
"Оцінки студентів у певній групі з певного предмета на останньому занятті",
]

marker = f"  {GRAY}•{RESET}"

def select_1():
    res = list("")
    while not res:
        res = my_queries.query_1()
    print("5 студентів із найбільшим середнім балом з усіх предметів:")
    for s in res:
        print(marker, f"{s[0]} {((21-len(s[0]))*".")} {CYAN}{s[1]}{RESET}")

def select_2():
    res = list("")
    while not res:
        res = my_queries.query_2(choice(SUBJECTS))
    print(f"Найвищий середній бал з предмету '{CYAN}{res[0][0]}{RESET}'", end="")
    print(f"у студента {CYAN}{res[0][1]}{RESET}: {CYAN}{res[0][2]}{RESET}")

def select_3():
    res = list("")
    while not res:
        res = my_queries.query_3(choice(SUBJECTS))
    print(f"Середній бал з предмету '{CYAN}{res[0][0]}{RESET}' у групах:")
    for gr in res:
        print(marker, gr[1], "=", gr[2])

def select_4():
    res = list("")
    while not res:
        res = my_queries.query_4()
    print(f"Середній бал на потоці: {CYAN}{res[0][0]}{RESET}")

def select_5():
    res = list("")
    while not res:
        res = my_queries.query_5(randint(1, NUMBER_TEACHERS))
    print(f"Викладач {CYAN}{res[0][0]}{RESET} викладає наступні предмети:")
    for d in res:
        print(marker, d[1])

def select_6():
    res = list("")
    while not res:
        res = my_queries.query_6(randint(1, len(GROUPS)))
    print(f"Список студентів групи '{CYAN}{res[0][0]}{RESET}':")
    count = 1
    for s in res:
        if count < 10:
            print(end=" ")
        print(GRAY, count, RESET, s[1])
        count += 1

def select_7():
    res = list("")
    while not res:
        res = my_queries.query_7(randint(1, len(GROUPS)), randint(1, len(SUBJECTS)))
    print(f"Оцінки студентів в групі {CYAN}{res[0][0]}{RESET} з '{CYAN}{res[0][1]}{RESET}:")
    repeats = {}
    for r in res:
        if r[2] not in repeats:
            grades = []
        grades.append(r[3])
        repeats[r[2]] = grades
    for key, value in repeats.items():
        # print(marker, key, (21-len(key))*".", CYAN, value, RESET)
        print(marker, key, (21-len(key))*".", CYAN, end="")
        # print(" ".join(str(value)))
        for val in value:
            if val < 10:
                print(end=" ")
            print(val, end="  ")
        print("")

def select_8():
    res = list("")
    while not res:
        # print(f"{res = }")
        res = my_queries.query_8(randint(1, NUMBER_TEACHERS))
    print(f"Середній бал, який ставить викладач {CYAN}{res[0][0]}{RESET} ", end="")
    print(f"зі своїх предметів = {CYAN}{res[0][1]}{RESET}")

def select_9():
    res = list("")
    while not res:
        res = my_queries.query_9(randint(1, NUMBER_STUDENTS))
    print(f"Список курсів, які відвідує {CYAN}{res[0][0]}{RESET}:")
    for d in res:
        print(marker, d[1])

def select_10():
    res = list("")
    while not res:
        res = my_queries.query_10(randint(1, NUMBER_STUDENTS), randint(1, NUMBER_TEACHERS))
    print(f"Студенту {CYAN}{res[0][0]}{RESET} викладач {CYAN}{res[0][1]}{RESET}", end="")
    print(" читає наступні предмети:")
    for d in res:
        print(marker, d[2])

def select_11():
    res = list("")
    while not res:
        res = my_queries.query_11(randint(1, NUMBER_STUDENTS), randint(1, NUMBER_TEACHERS))
    print(f"Середня оцінка студента {CYAN}{res[0][0]}{RESET} ", end="")
    print(f"у викладача {CYAN}{res[0][1]}{RESET} становить: {CYAN}{res[0][2]}{RESET}")

def select_12():
    res = list("")
    while not res:
        res = my_queries.query_12(randint(1, len(SUBJECTS)), randint(1, len(GROUPS)))
    print(f"Оцінки студентів у групі {CYAN}{res[0][1]}{RESET} ", end="")
    print(f"з предмету '{CYAN}{res[0][0]}{RESET}' ", end="")
    print(f"на останньому занятті {CYAN}{datetime_to_str(res[0][4])}{RESET}:")
    for r in res:
        print(marker, r[2], "-", r[3])


if __name__ == "__main__":
    print("\n")

    for i in range(1, 13):
        print(f"{GREEN_BACK}  Запит {i}:  {RESET}", end="")
        print(f"{GREEN} --- {query_name[i-1]} {RESET}")
        print(end="  ")

        globals()[f"select_{i}"]()

        print("\n")
