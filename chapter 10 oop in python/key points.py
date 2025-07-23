class Employee:
    company = "Google"  # ✅ Class variable → sab employee ka common

    def __init__(self, name, age):  # ✅ Constructor (dunder method)
        self.name = name           # ✅ Instance variable → har employee ka alag
        self.age = age             # ✅ Instance variable
        print("Constructor called!")

    def show(self):  # ✅ Instance method
        # self se instance variable & class variable dono access ho sakte hain
        print(f"Name: {self.name}, Age: {self.age}, Company: {self.company}")


# ✅ Creating objects (instances)
emp1 = Employee("Arka", 23)   # emp1 object bana
emp2 = Employee("Zaid", 25)   # emp2 object bana

# ✅ Calling method
emp1.show()  # ➤ Output: Name: Arka, Age: 23, Company: Google
emp2.show()  # ➤ Output: Name: Zaid, Age: 25, Company: Google

# ✅ Class variable can also be accessed like this:
print(Employee.company)  # ➤ Google

# ✅ Overriding class variable for emp2 only
emp2.company = "Microsoft"
emp2.show()  # ➤ Company: Microsoft
emp1.show()  # ➤ Still Google


                    #OUTPUT
# Constructor called!
# Constructor called!
# Name: Arka, Age: 23, Company: Google
# Name: Zaid, Age: 25, Company: Google
# Google
# Name: Zaid, Age: 25, Company: Microsoft
# Name: Arka, Age: 23, Company: Google
