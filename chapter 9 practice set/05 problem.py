

words=["ganda","kamchor","faltu"]
with open("chapter 9 practice set/poems.txt") as f:
    content=f.read()
for word in words:
    content = content.replace(word, "#" * len(word))



with open("chapter 9 practice set/poems.txt","w") as f:
    f.write(content)