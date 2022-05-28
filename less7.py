class Client:
    #public - публічний
    #protected - захищений
    #privare - приватний
    def __init__(self , name , balance , creditBalance , passport):
        self.__name = name
        self.__balansOwnFunds = balance
        self.__balansCreditFunds = creditBalance
        self.__passport = passport
    def addOwnFunds(self , money):
        self.__balansOwnFunds =+ money
    def addCreditFunds(self , money):
        self.__balansCreditFundsFunds =+ money
    #def printProtectetDeta(self):
    #   print(self._name,self._balansOwnFunds,self._balansCreditFunds,self._passport)
    def __printPrivatDeta(self):
      print(self.__name,self.__balansOwnFunds,self.__balansCreditFunds,self.__passport)



account1 = Client("Bob" , 1000,300,56784390)

account1.addOwnFunds(1000)
account1._Client__printPrivatDeta()
 # print(account1.__name)
 # print(account1.__balansOwnFunds)
 # print(account1.__balansCreditFunds)
 # print(account1.__passport)

