# Write a class “Calculator” capable of finding square, cube and square root of a 
# number. 
class calculator:

    def __init__(self,n):
        self.n=n
    def square (self):
        print(f"the square is {self.n*self.n}")
    def cube (self):
        print(f"the cube is {self.n*self.n*self.n}")
    def sqareroot (self):
        print(f"the square root is {self.n**0.5}")


num = int(input("Enter a number: "))

a=calculator(num)  # num == n iha par object n ko value derahe hai jo user se input liya gaya hai

a.square()
a.cube()
a.sqareroot()
