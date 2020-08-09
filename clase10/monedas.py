from random import randint

def lanza_moneda():
    # 0 es Aguila
    # 1 es Sol
    return randint(0 ,1)

def sale_sol():
    return lanza_moneda() == 1

lanzamientos = 1000
soles = 0
for i in range(lanzamientos):
    if sale_sol():
        soles += 1

proba_sol = 100 / lanzamientos * soles
print(proba_sol)
