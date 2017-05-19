# -*- coding: utf-8 -*-

from functools import partial
from six.moves import cPickle as pickle
import dill
import pyperclip
import six


def copy(obj, protocol=None, deep=False):
    protocol = protocol or (2 if six.PY2 else 3)
    dump_fn = dill.dumps if deep else pickle.dumps
    dump = dump_fn(obj, protocol=protocol)
    pyperclip.copy(dump.decode('latin1'))


def paste(deep=False):
    obj = six.binary_type(
        pyperclip.paste().encode('latin1')
    )
    loads_fn = dill.loads if deep else pickle.loads
    return loads_fn(obj)


deepcopy = partial(copy, deep=True)
deeppaste = partial(paste, deep=True)
