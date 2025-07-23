class employee:
    language="java"
    age=20

    def getinfo(self):
        print(f"arka's favporite language is {self.language} , arka's age is {self.age}")

    @staticmethod
    def greet():
        print("good morning")

arka=employee()
# arka.language= "python"

arka.greet()
arka.getinfo()







