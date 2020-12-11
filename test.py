import timeit

n = 1000
i = 1000

py = timeit.timeit("main.test(%i)" % i, setup="import main", number=n)
cy = timeit.timeit("cmain.test(%i)" % i, setup="import cmain", number=n)

print("Python: %.*fns" % (7, py))
print("Cython: %.*fns" % (7, cy))
print("=" * 22)
print("Cython is %.*fx faster" % (0, py/cy))
