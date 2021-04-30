import restless.crypto
from .utils import (
  bytes_to_long,
  long_to_bytes
)
import os

class SRP:

  def __init__(
    self,
    secret: bytes,
    srp_group: dict
  ):
    self.secret = bytes_to_long(secret)
    self.N = srp_group['N']
    self.g = srp_group['g']
    self.a = None


  @staticmethod
  def generate_secret(passphrase: str, salt=None):
    key, salt = restless.crypto.kdf(
      passphrase=passphrase.encode('utf-8'),
      salt=salt
    )
    return key, salt

  @staticmethod
  def generate_verifier(group, secret):
    g = group['g']
    N = group['N']
    secret = bytes_to_long(secret)
    vkey = pow(g, secret, N)
    return long_to_bytes(vkey)

  def computeA(self):
    self.a = bytes_to_long(os.urandom(8))
    A = pow(self.g, self.a, self.N)
    return long_to_bytes(A)
