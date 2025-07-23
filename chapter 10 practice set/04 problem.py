# Add a static method in problem 2, to greet the user with hello.

class calculator:

    def __init__(self,n):
        self.n=n
    def square (self):
        print(f"the square is {self.n*self.n}")
    def cube (self):
        print(f"the cube is {self.n*self.n*self.n}")
    def sqareroot (self):
        print(f"the square root is {self.n**0.5}")
    @staticmethod
    def greet():
        print("HELLO")


num = int(input("Enter a number: "))

a=calculator(num)  # num == n iha par object n ko value derahe hai jo user se input liya gaya hai
a.greet()
a.square()
a.cube()
a.sqareroot()
