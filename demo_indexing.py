a = list(range(10)) # list of 10 elements, autopopulated 0-9
print(a)
print(len(a)) # length of a
print(a[len(a)-1]) # last element

print(a[-1]) # equivalent to [len(a)-1]
print(a[-2])
print(a[-3])

for b in range(len(a)):
    print(a[b])

for b in range(len(a)):
    print(a[-b])

