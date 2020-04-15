# Base_to_Base
Functions for working with number systems, conversions and coding.

There are 3 main conversion functions,

from a dec to other base:
`numtobase(n, to_alphabet):str`
```
print(numtobase(32, '01'))
> 100000
```
from base to bec:
`basetodec(s, from_alphabet):str`
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
Alphabet constants are provided in the package `b2, b4, b8, b10, b16, b32, b62, b64`.

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

Also is function for converting ascii to a base and back:
`asciitobase(s, to)`,
`basetoascii(s, from)`
and
`hextoascii(s)`

```
asciitobase('Hello!', b2)
> 10010000110010101101100011011000110111100100001
hextoascii('48656c6c6f21')
> Hello!
```
