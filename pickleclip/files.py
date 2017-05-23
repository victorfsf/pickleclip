# -*- coding: utf-8 -*-

from pickleclip.base import paste
import pyperclip


def dump(path, mode='wb'):
    with open(path, mode) as f:
        f.write(
            pyperclip.paste().encode('latin1')
        )


def load(path, mode='rb', fn=paste):
    with open(path, mode) as f:
        pyperclip.copy(
            f.read().decode('latin1')
        )
    return fn()
