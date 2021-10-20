import argparse
import base64
import pathlib
from datetime import datetime

import pyperclip


def encode(clear_text):
    pass


def decode(encrypted_text):
    pass


def encode_decode(args):
    encoding = 'utf-8'
    if args.action == 'decrypt':
        clipboard_content = pyperclip.paste()
        enc_filename = write_clipboard(args.environment, args.action, 'enc', clipboard_content)
        print(f'Encrypted file: {enc_filename}')
        clear_content = base64.b64decode(clipboard_content.encode(encoding))
        clear_filename = write_clipboard(args.environment, args.action, 'dec', clear_content.decode(encoding))
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
