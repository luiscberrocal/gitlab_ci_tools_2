import pathlib

import hypothesis.strategies as st
import pytest
from hypothesis import given

from gitlab_ci_tools_2.b64_util import encode, decode, write_clipboard


@pytest.fixture(scope="module")
def my_test_folder():
    folder = pathlib.Path(__file__).parent.parent / 'output' / 'pytests'
    folder.mkdir(exist_ok=True, parents=True)
    return folder


@given(st.text(), st.sampled_from(['utf-8']))
def test_encode_decode(clear_text, encoding):
    encrypted = encode(clear_text, encoding)
    decrypted = decode(encrypted, encoding)
    assert decrypted == clear_text


@given(environment=st.sampled_from(['prod', 'staging']),
       action=st.sampled_from(['encrypt', 'decrypt']),
       source_type=st.sampled_from(['encrypt', 'decrypt']),
       content=st.text())
def test_write_clipboard(environment, action, source_type, content, my_test_folder):
    filename = write_clipboard(environment, action, source_type, content, my_test_folder)
