class grandfather():
    def a(self):
        print("yo dadaji")
class father(grandfather):
    def b(self):
        print("yo papaji")
class son(father):
    def c(self):
     print("yo betaji")


x =grandfather()
x.a()
print("")
y =father()
y.a()
y.b()
print("")
z=son()
z.a()
z.b()
z.c()

# output
# yo dadaji

# yo dadaji
# yo papaji

# yo dadaji
# yo papaji
# yo betaji