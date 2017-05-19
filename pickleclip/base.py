# -*- coding: utf-8 -*-

from functools import partial
from six.moves import cPickle as pickle
import dill
import pyperclip
import six


def copy(obj, protocol=None, serializer=pickle):
    protocol = protocol or (2 if six.PY2 else 3)
    dump = serializer.dumps(obj, protocol=protocol)
    pyperclip.copy(dump.decode('latin1'))


def paste(serializer=pickle):
    obj = six.binary_type(
        pyperclip.paste().encode('latin1')
    )
    return serializer.loads(obj)


dillcopy = partial(copy, serializer=dill)
dillpaste = partial(paste, serializer=dill)
