#NaN - Not a Number
#NaN noes sensible a mayusculas minusculas
#NaN es un tipo de dato numérico indefinido
import math
from decimal import Decimal

print("\n con float")
a = float('NaN')
print(f"a: {a}")
print(f"a es NAN?: {math.isnan(a)}")

print("\n con decimal")
a = Decimal('NaN')
print(f"a: {a}")
print(f"a es NAN?: {math.isnan(a)}")