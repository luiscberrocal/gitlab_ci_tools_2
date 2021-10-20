import argparse
import base64
import pathlib
from datetime import datetime

import pyperclip


def encode(clear_text):
    pass


def decode(encrypted_text, encoding):
    clear_content = base64.b64decode(encrypted_text.encode(encoding))
    return clear_content


def write_files(encrypted_text, clear_content, environment, action, encoding):
    enc_filename = write_clipboard(environment, action, 'enc', encrypted_text)
    clear_filename = write_clipboard(environment, action, 'dec', clear_content.decode(encoding))
    return enc_filename, clear_filename


def encode_decode(args):
    encoding = 'utf-8'
    if args.action == 'decrypt':
        clipboard_content = pyperclip.paste()
        clear_content = decode(clipboard_content, encoding)
        enc_filename, clear_filename = write_files(clipboard_content, clear_content, args.environment,
                                                   args.action, encoding)
        print(f'Encrypted file: {enc_filename}')
        print(f'Decrypted file: {clear_filename}')
    else:
        clipboard_content = pyperclip.paste()
        encrypted_content = base64.b64encode(clipboard_content.encode(encoding)).decode(encoding)
        print(encrypted_content)
        pyperclip.copy(encrypted_content)
        enc_filename = write_clipboard(args.environment, args.action, 'enc', encrypted_content)
        print(f'Encrypted file: {enc_filename}')


def write_clipboard(environment, source, source_type, content):
    target_path = pathlib.Path(__file__).parent
    times_stamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    clip_file = target_path / f'{times_stamp}-{source}-{environment}-{source_type}.txt'
    with open(clip_file, 'w') as c_file:
        c_file.write(content)
    return clip_file
