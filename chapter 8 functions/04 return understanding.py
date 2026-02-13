def avg():  # This is the function definition
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    average4 = (a + b + c) / 3
    print("Average is:", average4)
    print("Yay")
    return average4  # Return the calculated average
    
b=avg()
print(b)  #Ye returned value variable b me store ho jati hai ,print(b) → wahi value dubara print hoti ha



avg() #Return value ignore ho jati hai (kisi variable me store nahi hui)



# output
# Enter the first number: 1
# Enter the second number: 2
# Enter the third number: 3
# Average is: 2.0
# Yay
# 2.0        HERE 2.0 AGAIN PRINTS , BECAUSE B VARIABLE MEI RETURN KA VALUE STORE HUA HAI AND USKO CALL KIYA GAYA HAI CODE MEI.
# Enter the first number: 1
# Enter the second number: 2
# Enter the third number: 3
# Average is: 2.0
# Yay




