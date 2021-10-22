import pathlib

import pytest
from hypothesis import given
import hypothesis.strategies as st

from gitlab_ci_tools_2.b64_util import encode, decode


@pytest.fixture(scope="module")
def my_test_folder():
    folder = pathlib.Path(__file__).parent.parent / 'output'
    folder.mkdir(exist_ok=True)
    return folder


@given(st.text(), st.sampled_from(['utf-8']))
def test_encode_decode(clear_text, encoding):
    encrypted = encode(clear_text, encoding)
    decrypted = decode(encrypted, encoding)
    assert decrypted == clear_text


@given(environment=st.sampled_from(['prod', 'staging']),
       action=st.sampled_from(['encrypt', 'decrypt']))
def test_write_clipboard(environment, my_test_folder):
    folder = my_test_folder / environment
    print(folder)

    #write_clipboard(environment, action, source_type, content, target_path):

