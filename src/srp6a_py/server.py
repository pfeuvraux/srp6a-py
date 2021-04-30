import os
from .utils import (
  bytes_to_long,
  long_to_bytes,
  H
)
from .exceptions import SRPAuthenticationFailed
from .common import computeM

class SRP:

  def __init__(
    self,
    vkey: bytes,
    srp_group: dict,
    A: bytes,
    salt: bytes,
    username: str
  ):
    self.vkey = vkey
    self.k = None
    self.g = srp_group['g']
    self.N = srp_group['N']
    self.u = None
    self.A = bytes_to_long(A)
    self.salt = salt
    self.username = username.encode('utf-8')
    self.B = None
    self.b = None

    if self.A % self.N == 0:
      raise SRPAuthenticationFailed("Error while asserting A % N != 0")

  def computeB(self) -> bytes:
    vkey = bytes_to_long(self.vkey)
    self.k = bytes_to_long(
      H(long_to_bytes(self.N), long_to_bytes(self.g))
    )
    b = bytes_to_long(os.urandom(8))
    self.b = b

    B = (self.k * vkey + pow(self.g, b, self.N)) % self.N
    self.B = B
    return long_to_bytes(B)

  def verifyM1(self, M1):

    u = bytes_to_long(
      H(long_to_bytes(self.A), long_to_bytes(self.B))
    )
    K = self.__computeK(u)
    M = computeM(
      N=self.N,
      g=self.g,
      uname=self.username,
      salt=self.salt,
      K=K,
      u=long_to_bytes(u),
      B=long_to_bytes(self.B),
      A=self.A
    )

    if M != M1:
      raise SRPAuthenticationFailed
    return M

  def __computeK(self, u) -> bytes:

    S = pow(
      self.A * pow(bytes_to_long(self.vkey), u, self.N),
      self.b,
      self.N
    )
    return H(long_to_bytes(S))
