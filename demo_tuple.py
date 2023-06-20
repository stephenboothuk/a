t=()
print(type(t))
print('########################################################################################')
one_element_tuple = (42, ) # comma is required
three_elements_tuple = (1, 3, 5)
print(3 in three_elements_tuple)
print('########################################################################################')
type_of_t = type(t)

is_3_there = 3 in three_elements_tuple

print(type_of_t)
print(is_3_there)

print('########################################################################################')

print(three_elements_tuple)

print('########################################################################################')
a, b, c = 1, 3, 5

print (a, b, c)
print('  ')
print('Swap first two items')
b, a = a, b
print (a, b, c)
print('########################################################################################')
#print('Will this be the second elment of  a tuple? - ' three_elements_tuple[2])
# apparently not



