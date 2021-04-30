from src.srp6a_py.client import SRP
from src.srp6a_py.modulus import get_params

class Test_generate_secret_and_verifier:

  def test_e2e(self):

    N, g = get_params(group=1024)
    srp_group = {
      "N": N,
      "g": g
    }

    secret, secret_salt = SRP.generate_secret("toto")
    print(secret_salt) # public param
    print(secret) # must be encrypted before getting stored onto the server

    vkey = SRP.generate_verifier(
      group=srp_group,
      secret=secret
    )
    print(vkey) # verifier key, must be sent to the server

    srp_client = SRP(
      secret=secret,
      srp_group=srp_group
    )

    A = srp_client.computeA()
    print('')
    print(A)

