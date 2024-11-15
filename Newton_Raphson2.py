#Imports 
from sympy.parsing.sympy_parser import parse_expr
import sympy as sp
from sympy.plotting import *

# Definição das variaveis globais
#NOTA: erro_max e num_interações são globais pois são as mesmas para os dois casos 
x = sp.symbols('x') #metodo da biblioteca sympy que reconhece o x string como uma variavel matematica e realiza operacoes
erro_max = 0.00001
num_interacoes = 0
num_interacoes_max = 100



#Funcao que realiza o calculo de newton raphson
def newton_raphson(expressao,xi,):
    derivada_xi = sp.diff(expressao)
    num_interacoes = 1

    while num_interacoes <= num_interacoes_max:
        f_xi = expressao.subs(x,xi).evalf() #subs calcula o valor de uma funcao dado o ponto e evalf converte para float
        derivada_f_xi = derivada_xi.subs(x,xi).evalf() #calculando o valor da derivada de xi
        xi2 = xi - (f_xi / derivada_f_xi) # Calculo do Xi+1
        erro = abs((xi2 - xi)/xi2) #Calculo do erro 

        print(f"interação = {num_interacoes}")
        print(f"Xi= {xi:.13f} - Xi+1= {xi2:.13f}")
        print(f"Porcentagem de erro atual = {100 * erro:.13f}%\n")

        xi = xi2

        num_interacoes += 1

        if (erro < erro_max):
            print("Última iteração")
            break

if(num_interacoes == num_interacoes_max + 1):
    print("Número maxímo de interações atingido")



#Chamando a função com as duas expressões passadas 
newton_raphson(x - (x)*(sp.log(x)),2) #RESULTADO: Xi+1= 2.7182818285
newton_raphson((x**3) - (9*(x**2)) + 3,1)





