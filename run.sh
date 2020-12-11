#!/bin/bash

python3 setup.py -q build_ext --inplace && \
    python3 test.py && \
    cython -3 -a cmain.pyx && \
    open cmain.html
