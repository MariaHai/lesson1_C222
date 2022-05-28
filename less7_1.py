class Step:
    def __init__(self , name = "name" , age = 0):
        self.userName = name
        self.userAge = age
    def get_name(self):
        return self.userName
    def set_name(self , name):
        self.userName = name
    def get_age(self):
        return self.userAge
    def set_age(self , age):
        self.userAge = age
user = Step()
#print(user.userName)
print(user.get_name())
user.set_name("Jony")
print(user.get_name())
user.set_age("13")
print(user.get_age())

