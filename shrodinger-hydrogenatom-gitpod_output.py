# pip install sympy


import math
import sympy


sympy.init_printing()

sympy.var("qi qj")


S = (math.pi/(qi+qj))**(3/2)
H = 0.5*6*qi*qj/(qi+qj)*S - 2*math.pi/(qi+qj)


s = sympy.simplify(S)
H = sympy.simplify(H)


print(S)
print(H)


print(sympy.latex(S))
print(sympy.latex(H))
