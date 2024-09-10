txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)

txt = "Hello, welcome to my world."

x = txt.find("e")

print(x)

 

txt = "Hello, welcome to my world."

x = txt.find("e", 5, 10)

print(x)


txt = "Hello, welcome to my world."

print(txt.find("q"))
print(txt.index("q"))