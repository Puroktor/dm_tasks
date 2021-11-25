#pip install sympy
from sympy import *
import functools

def compFunc(f1, f2):
    lim = limit('({})/({})'.format(f1.split('=')[1], f2.split('=')[1]),
              symbols('n'), oo)
    print(lim)
    if lim<1:
        return -1
    elif lim == oo or lim>1:
        return 1
    else:
        return 0

with open('input.txt', 'r') as file:
    functions = file.read().splitlines()
functions.sort(key = functools.cmp_to_key(compFunc))
with open('output.txt', 'w') as file:
    file.write('\n'.join(functions))
