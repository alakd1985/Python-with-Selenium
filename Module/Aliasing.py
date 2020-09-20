#import ReturnMultiple as rm
import math
# Member aliasing::
from AlakMath import add as a, prod as p
print(a(12,23))
print(p(12,23))

# if one function is preesnt in more than one module then the most recent module will be called
print(dir(math))
