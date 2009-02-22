#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   $ python profiler.py >/dev/null
#   $ python profiler.py results | less
#
import see
import sys, os
import cProfile, pstats

def test():
    objs = ( [], 'test', os, {}, bool, 2, None, see, object )
    for i in xrange(1000):
        for o in objs:
            see.see(o)

if __name__ == '__main__':
    profile = '.seeprof'
    if 'results' in sys.argv:
        p = pstats.Stats(profile)
        p.strip_dirs().sort_stats('time').print_stats(20)
    else:
        sys.stderr.write('Testing see() v%s\n' % see.__version__)
        cProfile.run('test()', profile)
