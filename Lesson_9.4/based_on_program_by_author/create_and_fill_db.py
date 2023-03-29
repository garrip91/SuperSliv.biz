import sqlite3


# Настраиваем подключение к базе данных:
conn = sqlite3.connect('DATA.db')
# Настраиваем "курсор", с помощью которого будем обращаться к БД:
cursor = conn.cursor()

# Создаём таблицу по идентификатору, если её нет, а также нужные нам поля в ней:
cursor.execute(
    f"CREATE TABLE IF NOT EXISTS 'words_and_subwords' ("
    "id INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 1,"
    "word TEXT,"
    "sub_word TEXT)"
)
# Записываем изменения:
conn.commit()

# Добавляем в БД нужные нам записи:
cursor.execute(f"INSERT INTO 'words_and_subwords' (word, sub_word) VALUES (?, ?)", ["питон", "пони, тон, ион, опт, пот, тип, топ, пион, понт"])
cursor.execute(f"INSERT INTO 'words_and_subwords' (word, sub_word) VALUES (?, ?)", ["набор", "бар, бон, бор, раб, бра, боа, нора, роба, барон"])
cursor.execute(f"INSERT INTO 'words_and_subwords' (word, sub_word) VALUES (?, ?)", ["строка", "акр, акт, кот, рак, орк, оса, сок, ток, тор, кора, коса, сота, торс, роса, скат"])
# Снова записываем изменения:
conn.commit()
