from .utils import (
  bytes_to_long,
  long_to_bytes,
  H
)

def computeM(N, g, uname, salt, K, u, B, A):
  __N_h = H(long_to_bytes(N))
  __g_h = H(long_to_bytes(g))
  __xored_Ng = bytes_to_long(__N_h) ^ bytes_to_long(__g_h)
  x = [long_to_bytes(__xored_Ng)]


  x.append(H(uname))
  x.append(salt)

  x.append(long_to_bytes(A))
  x.append(B)
  x.append(K)

  M = b''

  for i in x:
    M += i[:]
  return M
