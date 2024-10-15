a = 3
b = 4
print(f"{a},{b}")
t = a
a = b
b = t
print(f"{a},{b}")
a,b = b,a
print(f"{a},{b}")