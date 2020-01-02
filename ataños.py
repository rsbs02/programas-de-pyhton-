#Esta funcion nos ayuda a cambiar  el año que queremos puros 1 de lo contrario 0's
def dataños(campo,año):
    for n,i in enumerate(campo):
        if i==año:
            campo[n]= 1
        else : campo[n]= 0
    return campo
