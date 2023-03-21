#def can_i_buy(money, price):
#
#    if money >= price:
#        return True
#    else:
#        return False
#
#
#i_have = 400
#cookie_price = 350
#
#print(can_i_buy(i_have, cookie_price))

class Hero:

    def __init__(self, money):
        self.money = money
    
    def can_i_buy(self, price):
        return self.money >= price


hero = Hero(400)

print(hero.can_i_buy(350))
print(hero.can_i_buy(250))
print(hero.can_i_buy(550))
