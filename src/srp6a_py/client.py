import os
import restless.crypto
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
    secret: bytes,
    srp_group: dict,
    salt: bytes,
    username: str
  ):
    self.salt = salt
    self.secret = bytes_to_long(secret)
    self.N = srp_group['N']
    self.g = srp_group['g']
    self.a = None
    self.A = None
    self.k = None
    self.S = None
    self.username = username.encode('utf-8')


  @staticmethod
  def generate_secret(passphrase: str, salt=None):
    key, salt = restless.crypto.kdf(
      passphrase=passphrase.encode('utf-8'),
      salt=salt,
      kdf_func="scrypt"
    )
    return key, salt

  @staticmethod
  def generate_verifier(group, secret):
    g = group['g']
    N = group['N']
    secret = bytes_to_long(secret)
    vkey = pow(g, secret, N)
    return long_to_bytes(vkey)

  def computeA(self) -> bytes:
    self.a = bytes_to_long(os.urandom(8))
    A = pow(self.g, self.a, self.N)
    self.A = A
    return long_to_bytes(A)

  def computeM1(self, B):

    if bytes_to_long(B) % self.N == 0:
      raise SRPAuthenticationFailed('Error while asserting B % N != 0')

    self.k = bytes_to_long(
      H(long_to_bytes(self.N), long_to_bytes(self.g))
    )

    u = bytes_to_long(
      H(long_to_bytes(self.A), B)
    )
    K = self.__computeK(u, B)
    M = computeM(
      N=self.N,
      g=self.g,
      uname=self.username,
      salt=self.salt,
      K=K,
      u=u,
      B=B,
      A=self.A
    )
    return M


  def __computeK(self, u, B) -> bytes:
    S = pow(
      bytes_to_long(B) - self.k * pow(self.g, self.secret, self.N),
      self.a + (u * self.secret),
      self.N
    )
    return H(long_to_bytes(S))
