class Fish():

    def swim(self):
        print("Я плаваю!")


class Girl():
    
    def sing(self):
        print("Я пою!")


class Mermaid(Girl, Fish):

    pass


ariel = Mermaid()
ariel.swim()
ariel.sing()
