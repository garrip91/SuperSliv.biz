import sqlite3


# Настраиваем подключение к базе данных:
conn = sqlite3.connect('DATA.db')
# Настраиваем "курсор", с помощью которого будем обращаться к БД:
cursor = conn.cursor()

# Создаём таблицу по идентификатору, если её нет, а также нужные нам поля в ней:
cursor.execute(
    f"CREATE TABLE IF NOT EXISTS 'questions' ("
    "id INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 1,"
    "question TEXT,"
    "level TEXT,"
    "answer TEXT)"
)
# Записываем изменения:
conn.commit()

# Добавляем в БД нужные нам записи:
cursor.execute(f"INSERT INTO 'questions' (question, level, answer) VALUES (?, ?, ?)", ["How many days do we have in a week?", "1", "7"])
cursor.execute(f"INSERT INTO 'questions' (question, level, answer) VALUES (?, ?, ?)", ["How many letters are there in the English alphabet?", "3", "26"])
cursor.execute(f"INSERT INTO 'questions' (question, level, answer) VALUES (?, ?, ?)", ["How many sides are there in a triangle?", "2", "3"])
cursor.execute(f"INSERT INTO 'questions' (question, level, answer) VALUES (?, ?, ?)", ["How many years are there in one Millennium?", "2", "1000"])
cursor.execute(f"INSERT INTO 'questions' (question, level, answer) VALUES (?, ?, ?)", ["How many sides does hexagon have?", "4", "6"])
# Снова записываем изменения:
conn.commit()
