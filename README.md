# Base_to_Base
Functions for working with number systems, conversions and coding.

There are 2 main conversion functions,
from dec to other base:
`numtobase(number, to_alphabet):str`
```
print(numtobase(32, '01'))
> 100000
```
and from a base to bec:
`basetodec(in, frtom_alphabet):str`
```
print(basetodec('ff', '0123456789abcdef'))
> 255
```
