class Fish():

    def __init__(self, name):
        self.name = name
    
    def swim(self):
        print("Я плаваю")
    
    def __repr__(self):
        return "Рыбка " + self.name


fish = Fish("Дори")
print(fish)
