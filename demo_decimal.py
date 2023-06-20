from decimal import Decimal as D
print(D(3.14)) # Decimal from float, has rounding error
print(D('3.14')) # Decimal from string, no rounding error
print(D(0.1) * D(3) - D(0.3)) # Rounding error
print(D('0.1') * D('3') - D('0.3')) # No rounding error