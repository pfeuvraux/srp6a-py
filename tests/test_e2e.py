from src.srp6a_py.client import SRP as SRPClient
from src.srp6a_py.server import SRP as SRPServer
from src.srp6a_py.modulus import get_params
from base64 import b64encode

USERNAME="TOTOLAFRITE"

class Test_generate_secret_and_verifier:

  def test_e2e(self):

    N, g = get_params()
    srp_group = {
      "N": N,
      "g": g
    }

    secret, salt = SRPClient.generate_secret("toto")

    vkey = SRPClient.generate_verifier(
      group=srp_group,
      secret=secret
    )

    srp_client = SRPClient(
      secret=secret,
      srp_group=srp_group,
      salt=salt,
      username=USERNAME
    )

    A = srp_client.computeA()
    print("\n\n\nThat's A")
    print(A)

    srp_server = SRPServer(vkey, srp_group, A, salt, USERNAME)
    B = srp_server.computeB()
    print("\n\n\nThat's B")
    print(B)

    M1 = srp_client.computeM1(B)
    M2 = srp_server.verifyM1(M1)

    print("")
    print(b64encode(M1).decode())
    print('')
    print(b64encode(M2).decode())
    print(len(M1), len(M2))

    assert M1 == M2
