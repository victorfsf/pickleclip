# -*- coding: utf-8 -*-

from six.moves import cPickle as pickle
import pyperclip
import six


def copy(obj, protocol=None):
    dump = pickle.dumps(
        obj, protocol=protocol or (
            2 if six.PY2 else 3
        )
    )
    pyperclip.copy(dump.decode('latin1'))


def paste():
    obj = six.binary_type(
        pyperclip.paste().encode('latin1')
    )
    return pickle.loads(obj)
