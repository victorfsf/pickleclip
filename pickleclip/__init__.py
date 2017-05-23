# -*- coding: utf-8 -*-

from .base import copy
from .base import dillcopy
from .base import dillpaste
from .base import paste
from .files import load
from .files import dump


__all__ = [
    'copy', 'paste', 'dillcopy',
    'dillpaste', 'load', 'dump'
]
