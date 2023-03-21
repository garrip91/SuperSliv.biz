class Employee():
    """Класс Сотрудника, который описывает Фамилию, Имя и Отчество."""

    def __init__(self, f, i, o):
        self.f = f
        self.i = i
        self.o = o
    
    def __repr__(self):
        return f"{self.f} {self.i[0]}.{self.o[0]}."


employees = [
    Employee("Питерская", "Анисья", "Григорьевна"),
    Employee("Меньшова", "Изольда", "Александровна"),
    Employee("Кручинина", "Калерия", "Тимофеевна"),
]

print(employees)
#print(employees[0].__doc__)
