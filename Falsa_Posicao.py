def fx(x):
    return (x**3 - 9*x + 3)

def erro_calc(xat ,xant):
    return abs((xat - xant)/ (xat))

def calcxatual(a,fa,b,fb):
    return ((a*fb) - (b*fa))/(fb - fa)

N_interacoes = 10
i = 1
a = 0

b = 1
fa = fx(a)
fb = fx(b)

erro = 0.001


xatual = calcxatual(b, fb, a,fa)
xanteiror = 0

print(f"i = {i} a = {a} b = {b} xi = {xatual} fa = {fa} fb = {fb} fxi = {fx(xatual)}")
while i <= N_interacoes:



    if erro_calc(xatual, xanteiror) < erro:
        break

    if xatual < 0 and fa <0:
        a = xatual
    elif xatual > 0 and fa > 0:
        b = xatual
    elif xatual > 0 and fb > 0:
        b = xatual
    elif xatual < 0 and fb < 0:
        b = xatual

    fa = fx(a)
    fb = fx(b)
    xanteiror = xatual

    xatual = calcxatual(b, fb, a,fa)
    print(f"i = {i} a = {a} b = {b} xi = {xatual} fa = {fa} fb = {fb} fxi = {fx(xatual)} erro = {erro_calc(xatual,xanteiror)}")

    if erro_calc(xatual, xanteiror) < erro:
        break
    i += 1


if i == N_interacoes + 1:
    print("Número máximo de interações atingidas")



