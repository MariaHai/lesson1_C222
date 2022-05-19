class cat:
    hp = 100
    eat = 100
    name = ""
    def __int__(self,n):
        self.name = n
        print(self.name,"hello")
        self.live()
        self.live()
        self.eating()
    def eating(self):
        self.eat += 10
        print(self.eat)
    def live(self):
        self.eat -= 5
        print(self.eat)
    def damage(self):
        self.hp -= 25
weywuxian = ("Wey Wuxin")
print(weywuxian,"hello")

