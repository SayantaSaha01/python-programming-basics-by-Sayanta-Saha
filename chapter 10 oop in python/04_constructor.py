class employee:
    

    def __init__(self, language, age):  # Constructor / dunder method (object bante hi chalega)
        self.language = language        # Instance attribute (object specific)
        self.age = age                  # Instance attribute
        print("hi")                     # Object banne par "hi" print hoga

    def getinfo(self,company):  # Instance method
        # Object ke language aur age print karega
        print(f"favporite language is {self.language} ,  age is {self.age},{company} ")

    @staticmethod
    def greet():  # Static method (object ya class se directly call kar sakte ho)
        print("good morning")

# Object bana rahe hain, aur constructor me values de rahe hain
arka = employee("c++", "23")  # agar tu arka.language = "python" likhta to language change ho jata
# arka.language="python"
arka.greet()      # Static method call, "good morning" print hoga
arka.getinfo("oracle")    # Instance method call, language & age print karega

# object ke attributes ko print kar rahe ho
print(f" arka's favourite language is {arka.language}, arka's age is {arka.age}")

zaid=employee("ruby","17",)
zaid.greet()
zaid.getinfo("microsoft")
print(f" zaid's favourite language is {zaid.language}, zaid's age is {zaid.age}") 




# output
# hi
# good morning
# favporite language is c++ ,  age is 23
#  arka's favourite language is c++, arka's age is 23
# hi
# good morning
# favporite language is ruby ,  age is 17
#  zaid's favourite language is ruby, zaid's age is 17


