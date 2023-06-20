from collections import defaultdict
# Setting default in .get
d = { }
d['age'] = d.get('age', 0) + 1
print(d.get('age'))

d = {'age': 39}
d['age'] = d.get('age', 0) + 1
print(d.get('age'))
print('--------------------------------------------------------------------------------------------------------')
# Using defaultdict
# Specify datatype at declaration
dd = defaultdict(int)
dd['age'] += 1 # same as dd['age'] = dd['age'] + 1
print(dd.get('age'))
dd['age']= 39
dd['age'] += 1 # same as dd['age'] = dd['age'] + 1
print(dd.get('age'))