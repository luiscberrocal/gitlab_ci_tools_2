from gitlab_ci_tools_2.b64_util import encode, decode


def test_encode_decode():
    source_data = 'This is a test'
    encrypted = encode(source_data, 'utf-8')
    decrypted = decode(encrypted, 'utf-8')
    assert decrypted == source_data