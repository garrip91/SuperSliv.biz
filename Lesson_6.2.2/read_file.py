# file = open("test.txt", "rt") # read, text

# content = file.read(5)
# print(content)

# for line in file:
#     print(line)

# file.close()


guests_count = 0
with open("guests.txt", "rt") as file:
    #guests_count = len(file.readlines())
    for line in file:
        print(line)
        guests_count += 1


print(f"Количество гостей = {guests_count}")
