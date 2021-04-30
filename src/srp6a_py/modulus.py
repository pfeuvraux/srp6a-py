
KNOWN_GROUPS = {
  1024: {
    "N": """
      00:a4:17:27:87:93:33:48:78:2e:e6:41:be:74:98:
      c2:22:e6:af:00:42:f3:22:e7:1c:f3:06:c2:ce:e7:
      18:63:c6:a2:68:e9:48:90:49:80:42:31:ef:50:2d:
      9d:92:9b:ce:87:f6:2b:0c:63:c8:ab:6f:16:4b:db:
      07:f4:32:18:d1:f5:a2:ff:bb:93:e9:d3:93:21:74:
      50:bb:1a:88:7b:2b:41:73:0b:67:cc:eb:d3:76:fd:
      f8:7f:b2:28:01:0d:54:cc:18:b3:b2:68:95:94:c4:
      f1:a6:d9:3a:c5:17:9a:58:2e:1b:e8:f7:f7:0c:02:
      8a:d9:ce:6a:a2:82:90:9c:23
    """,
    "g": 2
  }
}

def get_params(group: int):
  g = KNOWN_GROUPS[group]['g']
  N = KNOWN_GROUPS[group]['N']
  N = N.split()
  N = "".join(N).replace(":", "")
  return int(N, 16), g
