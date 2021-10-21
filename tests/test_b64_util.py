from hypothesis import given
import hypothesis.strategies as st

from gitlab_ci_tools_2.b64_util import encode, decode


@given(st.text(), st.sampled_from(['utf-8', 'ascii']))
def test_encode_decode(clear_text, encoding):
    encrypted = encode(clear_text, encoding)
    decrypted = decode(encrypted, encoding)
    assert decrypted == clear_text
