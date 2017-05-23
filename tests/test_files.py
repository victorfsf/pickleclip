# -*- coding: utf-8 -*-

import os
import pickleclip as picklec


def test_dump_load():
    obj = [
        {'this': 'is', 'a': 'test'},
        (1, 2, {3, 4}), object
    ]
    picklec.copy(obj)
    picklec.dump('test.pkl')
    assert os.path.isfile('test.pkl') is True

    picklec.copy(None)
    load = picklec.load('test.pkl')
    assert picklec.paste() is not None
    assert load == picklec.paste()

    os.remove('test.pkl')
