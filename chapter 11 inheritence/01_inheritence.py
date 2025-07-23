class employee:
    company="GOOGLE"
    def __init__(self):
        print("hello world")
    def sam(self,number):
        self.number=number
        print(f"the number is {self.number} , and company is {self.company}")
    
class programmer(employee):
    company="IBM"


a= employee()
a.sam(42)
b=programmer()
b.sam(89)

# output
# hello world
# the number is 42 , and company is GOOGLE
# hello world
# the number is 89 , and company is IBM