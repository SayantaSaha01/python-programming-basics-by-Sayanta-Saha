class grandfather():
    def __init__(self):
        print("good morning")
    def a(self):
        print("yo dadaji")
class father(grandfather):
    def __init__(self):
        super().__init__()
        print("good afternoon")
    def b(self):
        print("yo papaji")
class son(father):
    def __init__(self):
        super().__init__()
        print("good night")
        
    def c(self):
     print("yo betaji")


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
