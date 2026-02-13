class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):  # here __add__ is  special method for addition.
        return self.n + num.n

n = Number(1)
m = Number(6)

print(n + m)

