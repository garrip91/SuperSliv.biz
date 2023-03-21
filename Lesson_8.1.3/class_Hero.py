class Hero:

    def go_right(self):
        print("Я иду направо")
    
    def go_left(self):
        print("Я иду налево")
    
    def observe(self):
        print("Я осматриваюсь")


hero = Hero()
hero1 = Hero()
hero2 = Hero()
hero3 = Hero()

hero.go_right()
hero1.go_left()

hero.go_left()
hero.go_left()
hero.go_left()
hero.observe()
hero.go_right()
hero.go_right()
hero.observe()
