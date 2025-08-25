# Tuple creation
t = (1, 2, 3, 2, 5)

# ✅ Methods
print("count(2):", t.count(2))      # ➜ 2
print("index(5):", t.index(3))      # ➜ 

# ✅ Functions
print("len:", len(t))               # ➜ 5
print("sum:", sum(t))               # ➜ 13
print("max:", max(t))               # ➜ 5
print("min:", min(t))               # ➜ 1
print("sorted:", sorted(t))         # ➜ [1, 2, 2, 3, 5]
print("Is 3 in tuple?", 3 in t)     # ➜ True
