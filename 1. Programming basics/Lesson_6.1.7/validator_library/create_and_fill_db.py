import sqlite3


# Настраиваем подключение к базе данных:
conn = sqlite3.connect('DATA.db')
# Настраиваем "курсор", с помощью которого будем обращаться к БД:
cursor = conn.cursor()

# Создаём таблицу по идентификатору, если её нет, а также нужные нам поля в ней:
cursor.execute(
    f"CREATE TABLE IF NOT EXISTS 'users' ("
    "id INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 1,"
    "pin TEXT,"
    "password TEXT,"
    "email TEXT,"
    "name TEXT)"
)
# Записываем изменения:
conn.commit()

# Добавляем в БД нужные нам записи:
cursor.execute(f"INSERT INTO 'users' (pin, password, email, name) VALUES (?, ?, ?, ?)", ["1239", "secretd00r", "local@skypro", "Данил"])
cursor.execute(f"INSERT INTO 'users' (pin, password, email, name) VALUES (?, ?, ?, ?)", ["3333", "huskyeye5", "you(at)sky.pro", "Р_и_т_а"])
cursor.execute(f"INSERT INTO 'users' (pin, password, email, name) VALUES (?, ?, ?, ?)", ["1234", "secret", "me@sky.pro", "КОнстантин"])
cursor.execute(f"INSERT INTO 'users' (pin, password, email, name) VALUES (?, ?, ?, ?)", ["00011", "m3wm3wm3w", "@lizaveta", "А Ф"])
cursor.execute(f"INSERT INTO 'users' (pin, password, email, name) VALUES (?, ?, ?, ?)", ["8765", "fh43j_!", "alarm@gmail.com", "Елена"])
# Снова записываем изменения:
conn.commit()
