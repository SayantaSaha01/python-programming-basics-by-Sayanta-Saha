''' Create a class with a class attribute a; create an object from it and set ‘a’ 
 directly using ‘object.a = 0’. Does this change the class attribute?'''

class step1:
    a = 4  #  Class attribute 'a', sabhi objects ke liye common hoga

# Object 'o' create kiya class 'step1' se
o = step1()

# Pehle class attribute 'a' ko print kiya (object ke through access ho raha hai)
print(o.a)  #  Output: 4

# Ab object 'o' ke andar attribute 'a' ko 10 se overwrite kiya
# Yeh class attribute ko change nahi karega, balki object-level pe naya 'a' ban jaayega
o.a = 10

# Object-level attribute 'a' print ho raha hai
print(o.a)  #  Output: 10

# Class-level attribute 'a' ab bhi unchanged hai
print(step1.a)  #  Output: 4

# ANS is : NO
