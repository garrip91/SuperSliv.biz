#class Hero:
#
#    def __init__(self):
#        self.name = "Печенька"
#        print("Я", self.name)

#class Hero:
#
#    def __init__(self, name):
#        self.name = name
#        print("Я", self.name)

#class Hero:
#
#    def __init__(self, name, size):
#        self.name = name
#        self.size = size
#        print("Я", self.name, "размером", self.size)
#    
#    def go_right(self):
#        print(self.name, "идёт направо")
#    
#    def go_left(self):
#        print(self.name, "идёт налево")
#    
#    def observe(self):
#        print(self.name, "осматривается")

class Hero:

    def __init__(self, name, things):
        self.name = name
        self.things = things
        print("Я", self.name, "у меня есть", self.things)
    
    def iterate_things(self):
        for thing in self.things:
            print(thing)


#hero = Hero("Печений", 7)
#hero1 = Hero("Test", 7)

#hero.go_right()
#hero.go_left()
#hero1.go_left()
#hero.observe()

hero_1 = Hero("Кусантий", ["Голова", "Лапки", "Пуговичка", "Масочка"])
hero_1.iterate_things()
