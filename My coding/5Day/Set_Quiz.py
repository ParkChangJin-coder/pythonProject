a = set([1,2,3,4,5,6])
b = set([4,5,6,7,8,9])
c = set([5,6,7,8,9,10])
print(a & b & c)
print(a | b | c)
print(a - b - c)
a = [1,1,5,5,4,3,6,7,2,1,5,5,8,5]
print(list(set(a)))
d = set([1,2,3,4,5,6])
e = set([1,2,6,7,8,9])
f = set([1,2,6,7,8,9,10])
print(d - e - f)