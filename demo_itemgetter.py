from operator import itemgetter

a = [(5,3), (1,3), (1, 2), (2, -1), (4, 9)]
print('unsorted ', a)
print('Sort ', sorted(a))
#print(a)
print('Sort only on first element (0) of each tuple ', sorted(a, key=itemgetter(0)))
print('Sort on first (0) and second (1) element of each tuple ', sorted(a, key=itemgetter(0, 1)))
print('Sort just on second element (1) of each tuple ', sorted(a, key=itemgetter(1)))
print('Reverse sort on only second element (1) of each tuple ', sorted(a, key=itemgetter(1), reverse=True))
a.append((3,4))
print('add new tuple ', a)
print('Sort on second (1) then first (0) element of each tuple ', sorted(a, key=itemgetter(1, 0)))