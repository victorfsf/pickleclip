# -*- coding: utf-8 -*-

import pickleclip as picklec


def test_copy_paste():
    obj = [
        {'this': 'is', 'a': 'test'},
        (1, 2, {3, 4}), object
    ]
    picklec.copy(obj)
    assert picklec.paste() == obj


def test_deep_copy_paste():
    obj = [
        {'this': 'is', 'a': 'test'},
        (1, 2, {3, 4}), object
    ]
    picklec.copy(obj)
    assert picklec.paste() == obj
