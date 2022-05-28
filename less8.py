
import  colorama
class BuildingError(Exception):
    def __str__(self):
        return f"With so much material the house can not built!"
def check_material(amount_of_material , limit_value):
    if amount_of_material > limit_value:
        return  "enough material"
    else:
        raise  BuildingError(amount_of_material)
check_material(int(input()),300)
a = int(input())
f = open("8.txt","w")
try:
    f.write("Some text")
    print(10 / 0)
    print("sucssesful")
except ZeroDivisionError:
    print(colorama.Fore.RED + 'It is not possible to divide by 0')
except TypeError:
    print(colorama.Fore.RED + 'It is not possible to divide by "str"')
except NameError:
    print(colorama.Fore.YELLOW + 'You are accessing an object that does not exist')
else:
    print(colorama.Fore.GREEN + 'Nothing went wrong')
finally:
    f.close()
    print(colorama.Fore.GREEN + 'The "Try except"is finished')
input()












































# a = 5
# b = 7
# c = 9
# a,b,c = 5,7,8
#import random
#l = [random.randint(-10,10) for i in range(10)]
# for i in range(10):
#     l.append(random.randint(-10,10))
#print(l)