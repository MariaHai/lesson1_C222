class Soda :
    lemonade = 0
    gazovane = 0
    def __init__(self,g , l):
        self.gazovane = g
        self.lemonade = l
    def add(self):
        self.g += 10
        self.l += 1
        print(self.g)
        print(self.l)
    def show_my_drink(self):
        if self.l > 0 :
            print("«Газована вода з {ДОБАВКА}")
        else: print("Звичайна газована вода")
    def printinfo(self,name):
        print(f"{name:^10}")
        print("«Газована вода з {ДОБАВКА}",self.lemonade)
        print("Звичайна газована вода",self.gazovane)
        show_my_drink = (self)
        print(show_my_drink,self)
print("Робимо ваш напій ")









