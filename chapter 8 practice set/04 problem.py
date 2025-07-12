# Write a recursive function to calculate the sum of first n natural numbers.


n = int(input("Enter the value: "))

def first_n_number(n):
    if n == 1:
        return 1
    else:
        return n + first_n_number(n - 1)

# print(f"the value is  : {first_n_number(n)}")


b=first_n_number(n)
print(f"the value is  : {b}")





