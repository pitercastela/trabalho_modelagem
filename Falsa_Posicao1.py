import sympy as sp
from sympy.plotting import *

#função
def fx(x):
    return (x - (x)*(sp.log(x).evalf()))

#calculo do erro
def erro_calc(xat ,xant):
    return abs((xat - xant)/ (xat))

#calculo do xi
def calcxatual(a,fa,b,fb):
    return ((a*fb) - (b*fa))/(fb - fa)

N_interacoes = 100

erro = 0.00000001


xanteiror = 0


def Falsa_Posicao(valor1, valor2):
    i = 1
    a = valor1
    b = valor2

    xanteiror = 0
    while i <= N_interacoes:

        fa = fx(a)
        fb = fx(b)

        xatual = calcxatual(b, fb, a,fa)

        if erro_calc(xatual, xanteiror) < erro:
            break

        print(f"a = {a} b = {b}")

        if xatual < 0 and fa <0:
            a = xatual
        elif xatual > 0 and fa > 0:
            a = xatual
        elif xatual > 0 and fb > 0:
            b = xatual
        elif xatual < 0 and fb < 0:
            b = xatual

        print(f"i = {i}")
        print(f"xi = {xatual:.13f}")
        print(f"fxi = {fx(xatual):.13f}")
        print(f"erro = {100 *erro_calc(xatual,xanteiror):.13f}%\n")
        xanteiror = xatual
        i += 1

Falsa_Posicao(2, 3)
