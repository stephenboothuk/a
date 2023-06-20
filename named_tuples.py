from collections import namedtuple

# Ordinary, positional, Tuples
vision = (9.5, 8.8)
print('Ordinary Tuples')
print('Whole Tuple', vision)
print('Position zero', vision[0])
print('Position one', vision[1])

# Named Tuples
print('----------------------------------------------------------------------------------------------------')
Vision = namedtuple('Vision', ['left', 'right'])
nvision = Vision(9.5, 8.8)
print('Named Tuple')
print('Whole Tuple', nvision)
print('Position zero', nvision[0])
print('Position left', nvision.left)
print('Position right', nvision.right)

# Add extra element in the middle
print('----------------------------------------------------------------------------------------------------')
eVision = namedtuple('eVision', ['left', 'combined', 'right'])
print('Named Tuple with extra element in the middle')
envision = eVision(9.5, 9.2, 8.8)
print('Whole Tuple', envision)
print('Position zero', envision[0])
print('Position left', envision.left)
print('Position right', envision.right)
print('Position combined', envision.combined)

