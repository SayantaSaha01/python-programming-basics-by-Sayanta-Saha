# Create a class “Programmer” for storing information of few programmers working at Microsoft.
class programmer:
    company="Microsoft"
    

    def __init__(self,age,salary,location,language):
        self.age=age
        self.salary=salary
        self.location=location
        self.language=language


sayanta=programmer(20,100000,"kolkata","python")
print(f"company is{sayanta.company}")
print(f"sayanta's age is {sayanta.age}")
print(f"sayanta's salary is {sayanta.salary}")
print(f"sayanta's location is {sayanta.location}")
print(f"sayanta's language  is {sayanta.language}")

arka=programmer(17,90000,"kolkata","java")
print(f"company is{arka.company}")
print(f"arka's age is {arka.age}")
print(f"arka's salary is {arka.salary}")
print(f"arka's location is {arka.location}")
print(f"arka's language  is {arka.language}")

zaid=programmer(19,100000,"kolkata","js")
print(f"company is{zaid.company}")
print(f"zaid's age is {zaid.age}")
print(f"zaid's salary is {zaid.salary}")
print(f"zaid's location is {zaid.location}")
print(f"zaid's language  is {zaid.language}")

koyena=programmer(19,100000,"kolkata","c++")
print(f"company is{koyena.company}")
print(f"koyena's age is {koyena.age}")
print(f"koyena's salary is {koyena.salary}")
print(f"koyena's location is {koyena.location}")
print(f"koyena's language  is {koyena.language}")

