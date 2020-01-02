#Te muestra la fecha actual y las valor fechas que necesites .
def siguiente(fecha:str,valor:int):
    
    if int(fecha[4:7]) + valor <= 12 :
        mes=int(fecha[4:7]) + valor
        anio=fecha[0:4]
        return str(anio)+str(mes).zfill(2)
    elif int(fecha[4:7]) + valor > 12 :
        valoranio=1
        valorfecha= (int(fecha[4:7]) + valor) % 12
        anio=int(fecha[0:4]) + valoranio
        return str(anio)+str(valorfecha).zfill(2)

def secuenciafecha():
    i=1
    lista=[]
    while i < 7:
        X=siguiente(FECHACOMPARACION,7-i)
        lista.append(X)
        i+=1
    return lista[::-1]


#x=secuenciafecha()

