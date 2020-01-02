#Funcion te ayuda a obtener los elementos que no están en la otra lista
def doblar_valores(LISTA2,LISTA1):
    noigual = []
    for i,n in enumerate(LISTA2):
        if LISTA2[i] not in LISTA1 :
            noigual.append(LISTA2[i])
    return noigual
ns = doblar_valores(LISTA2,LISTA1)
print(ns)
LISTA1=['ab','an','ao','yu']
LISTA2=['ab','yu','ao','an','ox','op']

