from sympy.parsing.sympy_parser import parse_expr
import sympy as sp
from sympy.plotting import *

# Definição das variaveis
x = sp.symbols('x')
erro_max = 0.001
xi = 0
i = 1
num_interacoes = 0
num_interacoes_max = int(input())
expressao = sp.exp(-(x)) - x
derivada_xi = sp.diff(expressao) #parse_expr(string,evaluate=True)


# Calculo de Newton Raphson
while num_interacoes <= num_interacoes_max:
    f_xi = expressao.subs(x,xi).evalf()
    derivada_f_xi = derivada_xi.subs(x,xi).evalf()
    xi2 = xi - (f_xi / derivada_f_xi)
    erro = abs((xi2 - xi)/xi2)

    print(f"Xi= {xi:.5f} - Xi+1= {xi2:.5f}")
    print(f"Porcentagem de erro atual = {100 * erro:.10f}%")

    xi = xi2

    num_interacoes += 1

    if (erro < erro_max):
        print("Última iteração")
        break

if(num_interacoes == num_interacoes_max + 1):
    print("Número maxímo de interações atingido")




