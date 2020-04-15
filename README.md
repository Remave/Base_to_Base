# Base_to_Base
Functions for working with number systems, conversions and coding.

There are 2 main conversion functions,

from dec to other base:
`numtobase(n, to_alphabet):str`
```
print(numtobase(32, '01'))
> 100000
```
from a base to bec:
`basetodec(s, frtom_alphabet):str`
```
print(basetodec('ff', '0123456789abcdef'))
> 255
```
and conversion base with any alphabet to base with other alphabet:
`basetobase(s, in_alphabet, out_alphabet)`
```
print(basetobase('f745', '0123456789abcdef', '0123'))
> 33131011
```
Alphabet constants are provided in the package `b2, b4, b8, b10, b16, b32, b34`.

Other functions:

```
bectobin(n)
bectooct(n)
bectohex(n)
octtobin(n)
octtodec(n)
octtohex(n)
hextobin(n)
hextooct(n)
hextodec(n)
bintooct(n)
bintodec(n)
bintohex(n)
```

Also is function for converting ascii to base and back:
```
asciitobase(s, to)
and
basetoascii(s, from)
```
