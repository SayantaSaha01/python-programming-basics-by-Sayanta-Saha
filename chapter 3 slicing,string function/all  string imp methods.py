s = "  Hello World  "

# 1. strip() → remove whitespace from both sides
print(s.strip())  # ➜ 'Hello World'

# 2. lower() / upper() → case conversion
print(s.lower())  # ➜ '  hello world  '
print(s.upper())  # ➜ '  HELLO WORLD  '

# 3. startswith() / endswith()
print(s.strip().startswith("Hello"))  # ➜ True
print(s.strip().endswith("World"))    # ➜ True

# 4. replace() → replace substring
print(s.replace("World", "Python"))  # ➜ '  Hello Python  '

# 5. split() → convert to list
text = "apple,banana,mango"
print(text.split(","))  # ➜ ['apple', 'banana', 'mango']

# 6. join() → convert list to string
fruits = ['apple', 'banana', 'mango']
print("-".join(fruits))  # ➜ 'apple-banana-mango'

# 7. find() → first index of substring
print(text.find("banana"))  # ➜ 6

# 8. in → membership test
print("apple" in text)   # ➜ True
print("grape" not in text)  # ➜ True

# 9. count() → how many times a word appears
print(text.count("a"))  # ➜ 4

# 10. format() / f-strings → dynamic strings
name = "Alice"
age = 30
print("Hi {}, you are {}.".format(name, age))  # ➜ Hi Alice, you are 30.
print(f"Hi {name}, you are {age}.")            # ➜ Hi Alice, you are 30.
