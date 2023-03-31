import sqlite3
from validators import check_pin, check_pass, check_mail, check_name


# Настраиваем подключение к базе данных:
conn = sqlite3.connect('DATA.db')
# Настраиваем "курсор", с помощью которого будем обращаться к БД:
cursor = conn.cursor()

# Вытаскиваем из БД нужные нам данные:
user1_query = cursor.execute(f"SELECT * FROM 'users' WHERE id='1'").fetchall()
user2_query = cursor.execute(f"SELECT * FROM 'users' WHERE id='2'").fetchall()
user3_query = cursor.execute(f"SELECT * FROM 'users' WHERE id='3'").fetchall()
user4_query = cursor.execute(f"SELECT * FROM 'users' WHERE id='4'").fetchall()
user5_query = cursor.execute(f"SELECT * FROM 'users' WHERE id='5'").fetchall()

# Проверяем ПИН-коды:
print(user1_query[0][1], check_pin(user1_query[0][1])) # 1239 True
print(user2_query[0][1], check_pin(user2_query[0][1])) # 3333 False
print(user3_query[0][1], check_pin(user3_query[0][1])) # 1234 False
print(user4_query[0][1], check_pin(user4_query[0][1])) # 00011 False
print(user5_query[0][1], check_pin(user5_query[0][1])) # 8765 True
print("\n")

# Проверяем пароли:
print(user1_query[0][2], check_pass(user1_query[0][2])) # secretd00r True
print(user2_query[0][2], check_pass(user2_query[0][2])) # huskyeye5 True
print(user3_query[0][2], check_pass(user3_query[0][2])) # secret False
print(user4_query[0][2], check_pass(user4_query[0][2])) # m3wm3wm3w True
print(user5_query[0][2], check_pass(user5_query[0][2])) # fh43j_! False
print("\n")

# Проверяем почтовые адреса:
print(user1_query[0][3], check_mail(user1_query[0][3])) # local@skypro False
print(user2_query[0][3], check_mail(user2_query[0][3])) # you(at)sky.pro False
print(user3_query[0][3], check_mail(user3_query[0][3])) # me@sky.pro True
print(user4_query[0][3], check_mail(user4_query[0][3])) # @lizaveta False
print(user5_query[0][3], check_mail(user5_query[0][3])) # alarm@gmail.com True
print("\n")

# Проверяем имена:
print(user1_query[0][4], check_name(user1_query[0][4])) # Данил True
print(user2_query[0][4], check_name(user2_query[0][4])) # Р_и_т_а False
print(user3_query[0][4], check_name(user3_query[0][4])) # КОнстантин True
print(user4_query[0][4], check_name(user4_query[0][4])) # А Ф True
print(user5_query[0][4], check_name(user5_query[0][4])) # Елена True
