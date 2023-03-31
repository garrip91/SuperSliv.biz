virus_code = 'print("Я вирус!")'

with open('answers.py', 'a') as file:
    file.write(f"\n{virus_code}\n")
