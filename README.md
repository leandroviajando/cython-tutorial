# Cython Tutorial

Speed up Python code with C/Cython

Following [Python Programming Tutorial](https://pythonprogramming.net/introduction-and-basics-cython-tutorial/)

## Requirements

Python and Cython

## Instructions

Make shell file executable: `chmod +x run.sh`

Run: `./run.sh`

**Individual steps:**

- Build C file (`.c`) and Shared Object file (`.so`): `python setup.py -q build_ext --inplace`
- Test performance: `python test.py`
- View potential improvements: `cython -3 -a cmain.pyx && open cmain.html`

## Further Information

[Official docs](https://cython.readthedocs.io/en/latest/index.html)
