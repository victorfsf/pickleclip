# Pickleclip

[![PyPI version](https://badge.fury.io/py/pickleclip.svg)](https://badge.fury.io/py/pickleclip)
[![Build Status](https://circleci.com/gh/victorfsf/pickleclip/tree/master.svg?style=shield)](https://circleci.com/gh/victorfsf/pickleclip)
[![Coverage Status](https://coveralls.io/repos/github/victorfsf/pickleclip/badge.svg)](https://coveralls.io/github/victorfsf/pickleclip)
[![Code Health](https://landscape.io/github/victorfsf/pickleclip/master/landscape.svg?style=flat)](https://landscape.io/github/victorfsf/pickleclip/master)

*A Simple clipboard tool for Python (2.7+ and 3.4+) pickled objects.*

## Installation

If you're using **Linux**, be sure to install [pyperclip](https://github.com/asweigart/pyperclip)'s dependency, xclip:
```
sudo apt-get install xclip
```

Then, install via pip:
```
pip install pickleclip
```

## Usage:

Using `pickleclip` is as simple as copying and pasting text:

```python
In [1]: import pickleclip as picklec

In [2]: picklec.copy({'hello': 'world'})

In [3]: picklec.paste()
Out[3]: {'hello': 'world'}
```

To copy functions or any object that the native pickle package can't handle, use dillcopy/dillpaste (it'll use [dill](https://github.com/uqfoundation/dill) instead of pickle):

```python
In [1]: import pickleclip as picklec

In [2]: def add(x, y):
   ...:     return x + y

In [3]: picklec.dillcopy(add)

In [4]: picklec.dillpaste()
Out[4]: <function __main__.add>

In [5]: picklec.dillpaste()(5, 10)
Out[5]: 15
```

Pickleclip will copy any python object supported by pickle (or dill) into your clipboard. You can paste it anywhere you'd like (in another shell, for instance), as long as you use the `pickleclip.paste` function.

### Copying from Python 3 to Python 2 using pickle

To get Python 3 objects to unpickle on Python 2, specify `protocol=2` when copying. Although pickle will try to map the new Python 3 names to the old module names used in Python 2, so that the pickle data stream is readable with Python 2, this does not come without limitations.

Going from Python 2 to Python 3 is even less trivial, and will mostly only work for the simplest cases. See also [pickle-compat](https://pypi.org/project/pickle-compat/).

By default, the highest [pickle protocol](https://docs.python.org/3/library/pickle.html#pickle-protocols) available to the interpreter is used. The higher the protocol used, the more recent the version of Python needed to read the pickle produced.

##### Python 3 shell:

```python
In [1]: import pickleclip as picklec

In [2]: picklec.copy({'hello': 'world'}, protocol=2)
```

##### Python 2 shell:

```python
In [1]: import pickleclip as picklec

In [2]: picklec.paste()
Out[2]: {'hello': 'world'}
```

### Copying from different Python versions using dill

It should work fine with basic objects (str, int, float, list, set, dict...), but it won't work with nothing too "fancy", (functions, custom objects...).
