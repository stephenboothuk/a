small_primes = set()
print(small_primes)
small_primes.add(2)
print(small_primes)
small_primes.add(3)
small_primes.add(5)
print(small_primes)
small_primes.add(1)
print(small_primes)
small_primes.remove(1)
print(small_primes)
print(3 in small_primes)
print(4 in small_primes)
print("Try to add another instance of 3")
small_primes.add(3)
print(small_primes)
print("create another set")
bigger_primes = set([5, 7, 11, 13])
print(bigger_primes)
print("find intersection with intersection operator &")
print(small_primes & bigger_primes)
print("subtract second set from first")
print(small_primes - bigger_primes)
print("Create set with curly brace operaror")
more_small_primes = {2, 3, 5, 5, 3}
print(more_small_primes)

small_primes.clear()
bigger_primes.clear()

fsmall_primes = frozenset([2, 3, 5, 7])
fbigger_primes = frozenset([5, 7, 11])
print(fsmall_primes)
print(fbigger_primes)
#fsmall_primes.add(11)
#print(fsmall_primes)
#fsmall_primes.remove(2)
#print(fsmall_primes)
print(fsmall_primes & fbigger_primes)