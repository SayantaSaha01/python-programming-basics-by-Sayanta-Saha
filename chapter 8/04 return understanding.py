def avg():  # This is the function definition
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    average4 = (a + b + c) / 3
    print("Average is:", average4)
    print("Yay")
    return average4  # Return the calculated average
    

b=avg()  # Function call
print("Returned average:", b)
b=avg()  # Function call
print("Returned average:", b)
b=avg()  # Function call
print("Returned average:", b)

