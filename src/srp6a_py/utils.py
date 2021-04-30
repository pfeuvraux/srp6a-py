from hashlib import sha384
import six

# Thanks https://github.com/cocagne for that
def bytes_to_long(s):
    n = 0
    for b in six.iterbytes(s):
        n = (n << 8) | b
    return n

def long_to_bytes(n):
    l = list()
    x = 0
    off = 0
    while x != n:
        b = (n >> off) & 0xFF
        l.append( chr(b) )
        x = x | (b << off)
        off += 8
    l.reverse()
    return six.b(''.join(l))

def bytes_to_int(data: bytes):
  return int.from_bytes(data, byteorder="big", signed=False)

def int_to_bytes(data: int):
  print(data.bit_length())
  return data.to_bytes(
    length=data.bit_length(),
    byteorder="big"
  )


def H(*args):

  shasum = sha384()
  for arg in args:
    shasum.update(arg)
  return shasum.digest()
