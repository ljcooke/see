see
===

<code>dir()</code> for humans.

(A proper README will appear soon!)


Installation
------------

1. <code>mkdir -p ~/lib/python</code>

2. Copy <code>see.py</code> to <code>~/lib/python</code>

3. _(For bash users)_
   Add the following lines to your <code>.bashrc</code> file:

        export PYTHONPATH="$HOME/lib/python"
        export PYTHONSTARTUP="$HOME/.pythonrc.py"

4. Create <code>~/.pythonrc.py</code> and add the following line:

        from see import see
