#Infinite values
import math
from decimal import Decimal

print('Con float')
positive_infinite = float('inf')
print(f"positive_infinite: {positive_infinite}")
print(f"positive_infinite es infinito?: {math.isinf(positive_infinite)}")

negative_infinite = float('-inf')
print(f"negative_infinite: {negative_infinite}")
print(f"negative_infinite es infinito?: {math.isinf(negative_infinite)}")

print()
print('Con math')

positive_infinite = math.inf
print(f"positive_infinite: {positive_infinite}")
print(f"positive_infinite es infinito?: {math.isinf(positive_infinite)}")
negative_infinite = -math.inf
print(f"negative_infinite: {negative_infinite}")
print(f"negative_infinite es infinito?: {math.isinf(negative_infinite)}")

print()
print('Con decimal')

positive_infinite = Decimal('Infinity')
print(f"positive_infinite: {positive_infinite}")
print(f"positive_infinite es infinito?: {math.isinf(positive_infinite)}")
negative_infinite = -Decimal('Infinity')
print(f"negative_infinite: {negative_infinite}")
print(f"negative_infinite es infinito?: {math.isinf(negative_infinite)}")