see
===

An alternative to `dir()`, for humans only.
Easy to type; easy to read!

**Requirements**

* Python (tested with 2.4 and 2.5)


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

The easiest way to use `see()` is to place the code somewhere Python will
find it, and have it imported whenever you launch an interactive session,
using a [startup file](http://www.python.org/doc/1.5.2p2/tut/node4.html).

1. `mkdir -p ~/lib/python`

2. Copy `see.py` to `~/lib/python`

3. Set the following environment variables (e.g. in `~/.bashrc`):

        export PYTHONPATH="$HOME/lib/python"
        export PYTHONSTARTUP="$HOME/.pythonrc.py"

4. Create `~/.pythonrc.py` and add to it the following line:

        from see import see

Now let's see if it works!

    bash$ python
    Python 2.5.1 (your lottery numbers)
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
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
