import sympy as sp
from sympy.plotting import *

def fx(x):
    return (x - (x)*(sp.log(x)))

def erro_calc(xat ,xant):
    return abs((xat - xant)/ (xat))

def calcxatual(a,fa,b,fb):
    return ((a*fb) - (b*fa))/(fb - fa)

N_interacoes = 100
i = 0

a = 1
b = 3

fa = fx(a)
fb = fx(b)

erro = 0.00000001


xatual = calcxatual(a, fa, b,fb)
xanteiror = 0

print(f"i = {i} a = {a} b = {b} xi = {xatual} fa = {fa} fb = {fb} fxi = {fx(xatual)}")
i+= 1

while i <= N_interacoes:

    xatual = calcxatual(b, fb, a,fa)

    if i != 1:
        if erro_calc(xatual, xanteiror) < erro:
            break

    if xatual < 0 and fa <0:
        a = xatual
    elif xatual > 0 and fa > 0:
        a = xatual
    elif xatual > 0 and fb > 0:
        b = xatual
    elif xatual < 0 and fb < 0:
        b = xatual

    fa = fx(a)
    fb = fx(b)


    print(f"i = {i}")
    print(f"xi = {xatual:.13f}")
    print(f"fxi = {fx(xatual):.13f}")
    print(f"erro = {100 *erro_calc(xatual,xanteiror):.13f}%")
    xanteiror = xatual
    i += 1



if i >= N_interacoes + 1:
    print("Número máximo de interações atingidas")



