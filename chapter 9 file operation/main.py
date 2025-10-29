# Ek hi file me 200 baar "new file 0ye" likhne ka code
with open("chapter 9 file operation/rason.txt", "w", ) as f:
    for i in range(1, 2001):
        f.write("I love you\n")  # \n se nayi line aayegi

