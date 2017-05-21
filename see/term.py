"""
Terminal info.

"""
import platform
import struct

# pylint: disable=invalid-name

try:
    if platform.system() == 'Windows':  # pragma: no cover (windows)
        from ctypes import windll, create_string_buffer
        fcntl, termios = None, None
    else:
        import fcntl
        import termios
        windll, create_string_buffer = None, None
except ImportError:
    fcntl, termios = None, None
    windll, create_string_buffer = None, None


DEFAULT_LINE_WIDTH = 78
MAX_LINE_WIDTH = 120


def term_width():
    """
    Return the column width of the terminal, or ``None`` if it can't be
    determined.
    """
    if fcntl and termios:
        try:
            winsize = fcntl.ioctl(0, termios.TIOCGWINSZ, '    ')
            _, width = struct.unpack('hh', winsize)
            return width
        except IOError:
            pass
    elif windll and create_string_buffer:  # pragma: no cover (windows)
        stderr_handle, struct_size = -12, 22
        handle = windll.kernel32.GetStdHandle(stderr_handle)
        csbi = create_string_buffer(struct_size)
        res = windll.kernel32.GetConsoleScreenBufferInfo(handle, csbi)
        if res:
            (_, _, _, _, _, left, _, right, _,
             _, _) = struct.unpack('hhhhHhhhhhh', csbi.raw)
            return right - left + 1
        else:
            return 0  # console screen buffer not available


def line_width(default_width=DEFAULT_LINE_WIDTH, max_width=MAX_LINE_WIDTH):
    """
    Return the ideal column width for the output from :func:`see.see`, taking
    the terminal width into account to avoid wrapping.
    """
    width = term_width()
    if width:  # pragma: no cover (no terminal info in Travis CI)
        return min(width, max_width)
    else:
        return default_width
