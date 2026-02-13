class grandfather():
    def __init__(self):
        print("constructer of godfather")
    def a(self):
        print("yo dadaji")
class father(grandfather):
    def __init__(self):
        super().__init__()  
        print("constructer of father")
    def b(self):
        print("yo papaji")
class son(father):
    def __init__(self):
        super().__init__()
        print("constructer of son")
        
    def c(self):
     print("yo betaji")


# Dunder method mei vi agar super nahi chalaya mulple/multilevel inheritence mei parent calss ka dunder method automatic call nahi hota


# x =grandfather()
# x.a()
# print("")
# y =father()
# y.a()
# y.b()
# print("")
z=son()
z.a()
z.b()
z.c()

# output
# constructer of godfather
# constructer of father
# constructer of son
# yo dadaji
# yo papaji
# yo betaji



# understanding of super
# super() parent (base) class ka method child class ke andar se call karta hai.
# Isse parent ka code reuse hota hai aur multiple inheritance me sahi order (MRO) follow hota hai.
# Matlab: bina parent ka naam likhe, parent ka function chala dena.


#                     NEXT EASY EXAMPLE
# class Parent:
#     def show(self):
#         print("Parent class")

# class Child(Parent):
#     def show2(self):
#         super().show()   # parent ka show() call #dobara niche parent class ka function call karne ki zarorat nahi parti
#         print("Child class")

# a = Child()
# a.show2()

# OUTPUT
# Parent class
# Child class
