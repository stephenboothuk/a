a = dict(A=1, Z=-1)
print(a)
b = {'A': 1, 'Z': -1}
print(b)
c = dict(zip(['A', 'Z'], [1, -1]))
print(c)
d = dict([('A', 1), ('Z', -1)])
print(d)
e = dict({'Z': -1, 'A': 1})
print(e)
print(a == b == c == d == e)