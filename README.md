# see: dir for humans

[![](https://img.shields.io/pypi/v/see.svg)](https://pypi.org/project/see/)

**see** is an alternative to `dir()`, for Python 2.7 and 3.4+.

It neatly summarises what you can do with an object.
Use it to inspect your code or learn new APIs.


## Example

<!-- For examples, use a 64-column terminal and set sys.ps1 = '>>> ' -->

Say you have an object which you'd like to know more about:

```
>>> from datetime import timedelta
```

Try inspecting the object with `see`:

```
>>> see(timedelta)
    isclass             +                   -
    *                   /                   //
    %                   +obj                -obj
    <                   <=                  ==
    !=                  >                   >=
    abs()               bool()              dir()
    divmod()            hash()              help()
    repr()              str()               .days
    .max                .microseconds       .min
    .resolution         .seconds            .total_seconds()
```

Here we can discover some things about it, such as:

- The object is a class.
- You can add something to it with the `+` operator.
- It has a `seconds` attribute.
- It has a `total_seconds` attribute which is a function.

Compare with the output of `dir`:

```
>>> dir(timedelta)
['__abs__', '__add__', '__bool__', '__class__', '__delattr__', '
__dir__', '__divmod__', '__doc__', '__eq__', '__floordiv__', '__
format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '
__init__', '__init_subclass__', '__le__', '__lt__', '__mod__', '
__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__radd__',
 '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rf
loordiv__', '__rmod__', '__rmul__', '__rsub__', '__rtruediv__',
'__setattr__', '__sizeof__', '__str__', '__sub__', '__subclassho
ok__', '__truediv__', 'days', 'max', 'microseconds', 'min', 'res
olution', 'seconds', 'total_seconds']
```

You can filter the results of `see` using a wildcard pattern
or a regular expression:

```
>>> see(timedelta).filter('*sec*')
    .microseconds       .seconds            .total_seconds()

>>> see(timedelta).filter('/^d/')
    dir()       divmod()
```


## Documentation

Documentation is available at <https://ljcooke.github.io/see/>.

- [Installation](https://ljcooke.github.io/see/install.html)
- [Usage](https://ljcooke.github.io/see/usage.html)
- [Startup File](https://ljcooke.github.io/see/startup.html)
- [Developer Reference](https://ljcooke.github.io/see/dev/index.html)


## Contributing

The source code is available from the following locations:

- [Sourcehut](https://sr.ht/~ljc/see/):<br/>
  `git clone https://git.sr.ht/~ljc/see`

- [GitHub](https://github.com/ljcooke/see):<br/>
  `git clone https://github.com/ljcooke/see.git`

Contributions are welcome.

- [Change Log](https://github.com/ljcooke/see/blob/develop/CHANGELOG.rst)
- [Code of Conduct](https://github.com/ljcooke/see/blob/develop/CODE_OF_CONDUCT.md)
- [Authors](https://github.com/ljcooke/see/blob/develop/AUTHORS.rst)
- [License](https://github.com/ljcooke/see/blob/develop/LICENSE)
