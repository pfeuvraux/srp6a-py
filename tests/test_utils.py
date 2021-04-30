import pytest
from src.srp6a_py.utils import bytes_to_int

class Test_bytes_to_int:

  sample = b'e\x9f\xd4\x17\x1e'

  valid_result = 436473173790
  invalid_result = 0

  @pytest.mark.parametrize("sample, given_result, expected",
    [
      (sample, valid_result, True),
      (sample, invalid_result, False)
    ]
  )
  def test_with_multiple_values(self, sample, given_result, expected):

    result = bytes_to_int(sample)
    print(result)

    assert (result == given_result) is expected
