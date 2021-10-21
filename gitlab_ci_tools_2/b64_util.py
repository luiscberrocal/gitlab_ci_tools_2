import argparse
import base64
import os
import pathlib
from datetime import datetime
from typing import Tuple

import pyperclip


def encode(clear_text: str, encoding: str) -> str:
    encrypted_content = base64.b64encode(clear_text.encode(encoding)).decode(encoding)
    return encrypted_content


def decode(encrypted_text: str, encoding: str) -> str:
    clear_content = base64.b64decode(encrypted_text.encode(encoding)).decode(encoding)
    return clear_content


def write_files(encrypted_text: str, clear_content: str, environment: str, action: str,
                encoding: str, target_folder: str) -> Tuple[str, str]:
    enc_filename = write_clipboard(environment, action, 'enc', encrypted_text, target_folder)
    clear_filename = write_clipboard(environment, action, 'dec', clear_content, target_folder)
    return enc_filename, clear_filename


def encode_decode(args):
    encoding = 'utf-8'
    if args.action == 'decrypt':
        clipboard_content = pyperclip.paste()
        clear_content = decode(clipboard_content, encoding)
        enc_filename, clear_filename = write_files(clipboard_content, clear_content, args.environment,
                                                   args.action, encoding, args.folder)
        print(f'Encrypted file: {enc_filename}')
        print(f'Decrypted file: {clear_filename}')
    else:
        clipboard_content = pyperclip.paste()
        encrypted_content = encode(clipboard_content, encoding)
        print(encrypted_content)
        pyperclip.copy(encrypted_content)
        enc_filename = write_clipboard(args.environment, args.action, 'enc', encrypted_content, args.folder)
        print(f'Encrypted file: {enc_filename}')


def write_clipboard(environment, source, source_type, content, target_path):
    # target_path = pathlib.Path(__file__).parent
    times_stamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    clip_file = os.path.join(target_path, f'{times_stamp}-{source}-{environment}-{source_type}.txt')
    with open(clip_file, 'w') as c_file:
        c_file.write(content)
    return clip_file
