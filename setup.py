from distutils.core import setup

import pretty_errors  # noqa: F401
from Cython.Build import cythonize

setup(ext_modules=cythonize("cmain.pyx"))
