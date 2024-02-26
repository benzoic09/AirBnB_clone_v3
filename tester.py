#!/usr/bin/python3

from importlib import import_module
import sys

m_imported = import_module(sys.argv[1])

if m_imported.__doc__ is None:
    print('no module doc')
else:
    print(f'ok, {m_imported.__doc__}')