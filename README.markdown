`see()`
=======

An alternative to Python's `dir()`.
Easy to type; easy to read!
For humans only.

* __Version__: 0.3

* __Requirements__: Python
    * Works with 2.4+
    * Not tested yet with 3.0, but some changes in this version
      have been taken into account


Sacrilege! Just what do you think you're doing?
----------

Don't get me wrong; `dir()` is a wonderful little function.
Always there to help you out when you chance upon something new and mysterious.
I would dare say it's one of my favourites.

But wait! There is a problem. Let's face it: `dir()` isn't
exactly easy on the eyes. Say you have a list of everyday items:

    pencil_case = ['pencils', 'protractor', 'ruler',
                   'a pair of compasses', 'razor blades',
                   'calculator', 'Garry Gum']
    pencil_case.append('Anti-Garry Gum')

And you want to see what you can do with this list. So you try:

<pre>&gt;&gt;&gt; dir(pencil_case)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delsli
ce__', '__doc__', '__eq__', '__ge__', '__getattribute__', '__getitem__', '__gets
lice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '
__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__r
educe_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__
', '__setslice__', '__str__', 'append', 'count', 'extend', 'index', 'insert', 'p
op', 'remove', 'reverse', 'sort']
</pre>

What a mess. Look at all that code! We didn't want the works &mdash;
we were just curious. Help us out here, Computer. This just will not cut it.

Enter `see()`.

    >>> see(pencil_case)
      ?   []   for   in   +   *   +=   *=   <   <=   ==   !=   >   >=   len()
      .append()   .count()   .extend()   .index()   .insert()   .pop()   .remove()
      .reverse()   .sort()

Blimey! There's something different about this one, isn't there?
Is this the same `pencil_case` we had before? I can _read_ it. There's
functions and operators and everything. No underscores or list separators
in sight. I am sorry I doubted you, Computer. We can still be friends, yes?


Okay, I'm convinced. How do I install this thing?
--------------------

If you're lucky enough to be using Linux, OS X, or anything similar,
simply type:

    sudo python setup.py install

Or, if you don't have root privileges:

    python setup.py install --home=~

(If you're using Windows, I can't help you out, I'm afraid.
 A Windows installer will appear soon!)

Now fire up a Python shell and try out this poetic little number:

    from see import see

With a bit of luck, nothing will explode, and you'll be skimming
through attributes like nobody's business.

To make things even more fun, you can make sure `see` is available
every time you run Python. How? you might ask. By using a [startup file](http://docs.python.org/tutorial/interpreter.html#the-interactive-startup-file).
Simply save the line above (`from see import see`) to a `.py` file
&mdash; let's use the file `~/.pythonrc.py`. Then, set the following
environment variable (e.g. in `.bashrc`):

    export PYTHONSTARTUP="$HOME/.pythonrc.py"

If you are using iPython, enabling `see` by default is slightly more
involved. Create a file `ipy_profile_see.py` in your `~/.ipython/`
directory and copy the following contents into the file:

    from IPython import ipapi

    def main():
        ip = ipapi.get()
        ip.ex('from see import see')

    main()

And then you can launch iPython with `see` already imported by giving
the command `ipython -profile see` or you can make it the default
choice by adding the line `import ipy_profile_see` anywhere inside the
`main()` function as given in the file `~/.ipython/ipy_user_conf.py`.

Now let's see if it works...

    bash$ python
    Python 2.5.1 (your lottery numbers)
    Type "help", "copyright", "credits" or "license" for more information.
    >>> foo = 'bar'
    >>> see(foo)
      ?   []   in   +   *   %   <   <=   ==   !=   >   >=   len()   .capitalize()
      .center()   .count()   .decode()   .encode()   .endswith()   .expandtabs()
      .find()   .index()   .isalnum()   .isalpha()   .isdigit()   .islower()
      .isspace()   .istitle()   .isupper()   .join()   .ljust()   .lower()
      .lstrip()   .partition()   .replace()   .rfind()   .rindex()   .rjust()
      .rpartition()   .rsplit()   .rstrip()   .split()   .splitlines()
      .startswith()   .strip()   .swapcase()   .title()   .translate()   .upper()
      .zfill()
    >>>
    >>> # success!
    ...


Acknowledgements
----------------

Some thanks are in order:

  * [akuhn](http://www.reddit.com/user/akuhn/)
    for the reddit linkage
  * [CommodoreGuff](http://www.reddit.com/user/CommodoreGuff/)
    for pointing out stuff that didn't work in Python 3
  * [ghoseb](http://github.com/ghoseb)
    for contributing iPython instructions
  * [igowen](http://ian.gowen.cc/)
    for fixing the link to the startup file documentation
    (Python 1.5 &mdash; what was I thinking?)
