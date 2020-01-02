Esta función nos permite cambiar la posición de fecha con terminación 00 al nombre del mes 
def datameses(campo):
    for n,i in enumerate(campo):
        if i=='01':
            campo[n]='Enero'
        elif i=='02':
            campo[n]='Febrero'
        elif i=='03':
            campo[n]='Marzo'
        elif i=='04':
            campo[n]='Abril'
        elif i=='05':
            campo[n]='Mayo'
        elif i=='06':
            campo[n]='Junio'
        elif i=='07':
            campo[n]='Julio'
        elif i=='08':
            campo[n]='Agosto'
        elif i=='09':
            campo[n]='Septiembre'
        elif i=='10':
            campo[n]='Octubre'
        elif i=='11':
            campo[n]='Noviembre'
        elif i=='12':
            campo[n]='Dicimebre'
    return campo
