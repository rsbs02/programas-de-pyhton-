fmes1 = buro1['fecha']
faño1 = buro1['fecha']
#Se crea un for por compresión para tomar los primeros dígitos del dato fecha o los dos últimos .
mes1 = [(i[4:]) for i in fmes1 if i != None]
año1 = [(i[:4]) for i in faño1 if i != None]

mesp1 = datameses(mes1)
#Recuerda las listas son inmutables por eso se debe trabajar sobre la serie pandas .
año2017p1 = dataños([(i[:4]) for i in faño1 if i != None],'2017')
año2018p1 = dataños([(i[:4]) for i in faño1 if i != None],'2018')
año2019p1 = dataños([(i[:4]) for i in faño1 if i != None],'2019')

dfburo1 = pd.DataFrame ({ 'mes':  mesp1,
                          'anio2017': año2017p1,
                          'anio2018': año2018p1,
                          'anio2019': año2019p1 })

burocuenta1 = dfburo1.groupby('mes').sum()[['anio2017', 'anio2018', 'anio2019']]
#no trabajar con muchos datos lo mejor es partirlos y en el punto donde sean mas cortos unirlos .
burocuenta = burocuenta1 + burocuenta2 
print(burocuenta)


#numero de elmento que no estan coincidiendo .
total = burocuenta - negocioscuenta
print(total)

No_coinciden = total['anio2017'] + total['anio2018'] + total['anio2019']
sum(No_coinciden)



