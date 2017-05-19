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

To copy functions, use deepcopy/deeppaste (it'll use [dill](https://github.com/uqfoundation/dill) instead of pickle):

```python
In [1]: import pickleclip as picklec

In [2]: def add(x, y):
   ...:     return x + y

In [3]: picklec.deepcopy(add)

In [4]: picklec.paste()
Out[4]: <function __main__.add>

In [5]: picklec.paste()(5, 10)
Out[5]: 15
```

Pickleclip will copy any python object supported by pickle or dill into your clipboard. You can paste it anywhere you'd like (in another shell, for instance), as long as you use the `pickleclip.paste` or `pickleclip.deeppaste` function.
