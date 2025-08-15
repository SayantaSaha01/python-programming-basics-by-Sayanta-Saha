''' Create a class ‘Employee’ and add salary and increment properties to it. 
Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter 
which changes the value of increment based on the salary. '''

class employee():
    salary=234
    increment=20

    @property
    def salaryafterincrement(self):
        return ((self.salary*(self.increment/100))+self.salary)
    @salaryafterincrement.setter
    def salaryafterincrement(self,salarryy):
        self.increment=((salarryy/self.salary)-1)*100


a=employee()
print(a.salaryafterincrement)
a.salaryafterincrement=280.8
print(f"salary hike is {a.increment}")

# output
# 280.8
# salary hike is 19.999999999999996


                        # by not using property decorators

class Employee:
    def __init__(self):
        self.salary = 234
        self.increment = 20

    # Method to calculate salary after increment
    def get_salary_after_increment(self):
        return self.salary + self.salary * (self.increment / 100)

    # Method to set increment using new salary
    def set_salary_after_increment(self, new_salary):
        self.increment = ((new_salary / self.salary) - 1) * 100


# ---- Testing ----
e = Employee()

# Get salary after increment (instead of e.salaryAfterIncrement)
print("Salary after increment:", e.get_salary_after_increment())

# Set salary after increment (instead of e.salaryAfterIncrement = 280.8)
e.set_salary_after_increment(280.8)

print("Increment percentage:", e.increment)

# output
# Salary after increment: 280.8
# Increment percentage: 19.999999999999996