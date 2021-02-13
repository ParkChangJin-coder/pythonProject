x = list()
y = []
print(x)
print(y)

x = [1, 2, 3, 4]
y = ["Hello", "World"]

print(x + y)
print(x[2])

x[3] = 10
print(x)

num_elements = len(x)
print(num_elements)

z = sum(x)
print(z)

for n in x:
    print(n)
for m in y:
    print(m)

print(x.index(3))
print(y.index("Hello"))
print("Hello" in y)

if "Hello" in y:
    print("Hello is there")
else:
    print("Hello is not there")
    
