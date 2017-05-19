# Pickleclip

A Simple clipboard tool for Python (2.7+ and 3.4+) pickled objects.

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

There are some known compatibility problems with copying and pasting code from Python 3 to Python 2, but some of those problems can be solved by using the `protocol` kwarg:

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

Since the PY2's pickle version can't handle the PY3's protocol number (which is 3), you'll need to force the PY3 pickle to use `protocol = 2`.

### Copying from different Python versions using dill

It should work fine with basic objects (str, int, float, list, set, dict...), but it won't work with nothing too "fancy", (functions, custom objects...).
