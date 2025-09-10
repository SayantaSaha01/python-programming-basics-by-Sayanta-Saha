# ------------------------------------------
# 📍 LIST METHODS START
# ------------------------------------------
lst = [3, 1, 4, 1, 5]

lst.append(9)               # Add one item
lst.extend([2, 6])          # Add multiple items
lst.insert(0, 100)          # Insert at index 0
lst.pop()                   # Remove last item
lst.remove(1)               # Remove first matching 1
lst.sort()                  # Sort in place
lst.reverse()               # Reverse the list

print("Count of 3:", lst.count(3))      # Count occurrences
print("Index of 9:", lst.index(9))      # Get index
copy_lst = lst.copy()                   # Copy the list
print("Copy:", copy_lst)

# ------------------------------------------
# 📍 LIST METHODS END
# ------------------------------------------

# ------------------------------------------
# 📍 BUILT-IN FUNCTIONS START
# ------------------------------------------

print("Length:", len(lst))              # Total items
print("Sum:", sum(lst))                 # Total sum
print("Max:", max(lst))                 # Largest value
print("Min:", min(lst))                 # Smallest value
print("Sorted (copy):", sorted(lst))    # Sorted new list
print("Is 5 in list?", 5 in lst)        # Membership check

# ------------------------------------------
# 📍 BUILT-IN FUNCTIONS END
# ------------------------------------------

# ------------------------------------------
# 📍 LIST COMPREHENSION
# ------------------------------------------

squares = [x*x for x in range(6)]
print("Squares:", squares)

# ------------------------------------------
