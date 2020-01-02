def MESATRASO(mes:str):
    switcher = {
        '01':'DA_ENERO',
        '02':'DA_FEBRERO',
        '03':'DA_MARZO',
        '04':'DA_ABRIL',
        '05':'DA_MAYO',
        '06':'DA_JUNIO',
        '07':'DA_JULIO',
        '08':'DA_AGOSTO',
        '09':'DA_SEPTIEMBRE',
        '10':'DA_OCTUBRE',
        '11':'DA_NOVIEMBRE',
        '12':'DA_DICIEMBRE',
    }
    return switcher.get(mes,None)


ef MESCVENCIDA(mes:str):
    switcher = {
        '01':'CV_ENERO',
        '02':'CV_FEBRERO',
        '03':'CV_MARZO',
        '04':'CV_ABRIL',
        '05':'CV_MAYO',
        '06':'CV_JUNIO',
        '07':'CV_JULIO',
        '08':'CV_AGOSTO',
        '09':'CV_SEPTIEMBRE',
        '10':'CV_OCTUBRE',
        '11':'CV_NOVIEMBRE',
        '12':'CV_DICIEMBRE',
    }
    return switcher.get(mes,None)
