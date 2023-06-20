def local():
    m = 'This is the local value of M in the local() function.'
    print(m)

m = 'This is global value of M not in a function.'
print(m)

local()