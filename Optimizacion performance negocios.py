#BASES A TRABAJAR 
DIRECCIONRFC='RFC/rfcmayo.csv'
DIRECCIONRISK='RISK_LEVEL/MAYO.csv'
FECHACOMPARACION='201905'
NOMBRETABLA='Conteos/ALTOSPRUEBA.csv'
tipo1=['RFC','rfcencrypt','PI']
tipo2=['RFC','rfcencrypt','PI','Pf1','Pf2']

def Performance():
    #LECTURA DE LOS RFC´S DEL MES
    RFCMES = pd.read_csv(DIRECCIONRFC, encoding='latin1')
    RFCMES.columns=['RFC','rfcencrypt']
    #LEAMOS LA BASE RISKLEVEL
    MESRISK = pd.read_csv(DIRECCIONRISK, encoding='latin1')
    #LECTURA DE CARTERA CREDITICIA
    file_key = "datalake/data/InteligenciaRiesgos/M&M/MCV/RSS/Octubre/Variables/BSEGN_UNIVERSO/000000_0"
    BSEGN_UNIVERSO1 = retrievs3(file_key)
    BSEGN_UNIVERSO1.columns = ['RFC',  'FECHA', 'DIAS_ATRASO', 'CARTERA_VENCIDA','mesesdc','LLAVE_UNIVERSAL_20']
    #btdc_universo.drop(['CLASIFICACION', 'MONTO_LINEA', 'MONTO_ORIGINAL'], axis=1, inplace=True)
    BSEGN_UNIVERSO1 = BSEGN_UNIVERSO1[BSEGN_UNIVERSO1['FECHA']>FECHACOMPARACION].reset_index(drop=True)
    BSEGN_UNIVERSO1.sort_values(['FECHA'], inplace=True, ascending=True)
    #BSEGN_UNIVERSO.set_index('RFC', inplace=True)

    #LECTURA DE CARTERA CREDITICIA
    file_key = "datalake/data/InteligenciaRiesgos/M&M/MCV/RSS/Octubre/Variables/BSEGN_UNIVERSO/000001_0"
    BSEGN_UNIVERSO2 = retrievs3(file_key)
    BSEGN_UNIVERSO2.columns = ['RFC',  'FECHA', 'DIAS_ATRASO', 'CARTERA_VENCIDA','mesesdc','LLAVE_UNIVERSAL_20']
    #btdc_universo.drop(['CLASIFICACION', 'MONTO_LINEA', 'MONTO_ORIGINAL'], axis=1, inplace=True)
    BSEGN_UNIVERSO2 = BSEGN_UNIVERSO2[BSEGN_UNIVERSO2['FECHA']>FECHACOMPARACION].reset_index(drop=True)
    BSEGN_UNIVERSO2.sort_values(['FECHA'], inplace=True, ascending=True)
    #union de 0001 y 0000
    BSEGN_UNIVERSO=pd.concat([BSEGN_UNIVERSO1,BSEGN_UNIVERSO2],axis=0)
    
    def proccessuniverso(BSEGN_UNIVERSO):
        features=BSEGN_UNIVERSO[['RFC', 'FECHA', 'DIAS_ATRASO', 'CARTERA_VENCIDA', 'mesesdc',
       'LLAVE_UNIVERSAL_20']]
        proccessuniverso = features.copy()
        alto=MESRISK[MESRISK['Clasificacion de Riesgo']=='ALTO'] #FILTRAR SOLO LOS ALTOS
        RFC = pd.merge(alto,RFCMES , how='left', on=['RFC'] )#obtener el rfc desencryptado
        RFC=RFC[tipo1]
        RFC.rename(columns={'RFC': 'rfcencrypt', 'rfcencrypt': 'RFC',' PI':  'PI'}, inplace=True) #CAMBIAR NOMBRE COLUMNAS
#RFC=RFC[tipo2]
#RFC.rename(columns={'RFC': 'rfcencrypt', 'rfcencrypt': 'RFC',' PI':  'PI','Pf1':'Pf1','Pf2':'Pf2'}, inplace=True) 
# Unimos las bases,
        universo = pd.merge(RFC, BSEGN_UNIVERSO, how='left', on=['RFC'])
        return universo 
    universo=proccessuniverso(BSEGN_UNIVERSO)
    def preprocess_features(universo):
        selected_features = universo[
        ['rfcencrypt', 'RFC', 'PI','FECHA', 'DIAS_ATRASO',
            'CARTERA_VENCIDA', 'mesesdc', 'LLAVE_UNIVERSAL_20']] #Apartir de agosto de agrega 'Pf1','Pf2'
        processed_features = selected_features.copy() #!!!!!!
  # Create a synthetic feature.
  #Tratamiento a los DA
        processed_features['IND_ATRASO']='0'
        cae_atraso = processed_features[processed_features['DIAS_ATRASO'] > '0']
        processed_features.loc[processed_features['DIAS_ATRASO'].isin(cae_atraso['DIAS_ATRASO']),'IND_ATRASO']='1'
  #Tratamiento a los CV
        processed_features['IND_CVENCIDA'] = '0'
        cae_cvencida=processed_features[processed_features['CARTERA_VENCIDA'] >'0.0']
        processed_features.loc[processed_features['CARTERA_VENCIDA'].isin(cae_cvencida['CARTERA_VENCIDA']),'IND_CVENCIDA']= '1'
  #Agrear atrasos
        x=secuenciafecha()
        processed_features[MESATRASO(x[0][4:7])] = np.where(((processed_features['IND_ATRASO']=='1') & (processed_features['FECHA']==x[0])),1,0)
        processed_features[MESATRASO(x[1][4:7])] = np.where(((processed_features['IND_ATRASO']=='1') & (processed_features['FECHA']==x[1])),1,0)
        processed_features[MESATRASO(x[2][4:7])] = np.where(((processed_features['IND_ATRASO']=='1') & (processed_features['FECHA']==x[2])),1,0)
        processed_features[MESATRASO(x[3][4:7])] = np.where(((processed_features['IND_ATRASO']=='1') & (processed_features['FECHA']==x[3])),1,0)
        processed_features[MESATRASO(x[4][4:7])] = np.where(((processed_features['IND_ATRASO']=='1') & (processed_features['FECHA']==x[4])),1,0)
        processed_features[MESATRASO(x[5][4:7])] = np.where(((processed_features['IND_ATRASO']=='1') & (processed_features['FECHA']==x[5])),1,0)
  #Agregar CVencido
        processed_features[MESCVENCIDA(x[0][4:7])] = np.where(((processed_features['IND_CVENCIDA']=='1') & (processed_features['FECHA']==x[0])),1,0)
        processed_features[MESCVENCIDA(x[1][4:7])] = np.where(((processed_features['IND_CVENCIDA']=='1') & (processed_features['FECHA']==x[1])),1,0)
        processed_features[MESCVENCIDA(x[2][4:7])] = np.where(((processed_features['IND_CVENCIDA']=='1') & (processed_features['FECHA']==x[2])),1,0)
        processed_features[MESCVENCIDA(x[3][4:7])] = np.where(((processed_features['IND_CVENCIDA']=='1') & (processed_features['FECHA']==x[3])),1,0)
        processed_features[MESCVENCIDA(x[4][4:7])] = np.where(((processed_features['IND_CVENCIDA']=='1') & (processed_features['FECHA']==x[4])),1,0)
        processed_features[MESCVENCIDA(x[5][4:7])] = np.where(((processed_features['IND_CVENCIDA']=='1') & (processed_features['FECHA']==x[5])),1,0)
        tabla=processed_features.groupby('RFC').sum()[[MESATRASO(x[0][4:7]),MESATRASO(x[1][4:7]),MESATRASO(x[2][4:7]),MESATRASO(x[3][4:7]),
                                                   MESATRASO(x[4][4:7]),MESATRASO(x[5][4:7]),MESCVENCIDA(x[0][4:7]),MESCVENCIDA(x[1][4:7]),MESCVENCIDA(x[2][4:7]),
                                                   MESCVENCIDA(x[3][4:7]),MESCVENCIDA(x[4][4:7]),MESCVENCIDA(x[5][4:7])]] 
        tabla.reset_index(level =['RFC'], inplace = True)
        TABLA = pd.merge(RFC,tabla , how='left', on=['RFC'])
        return TABLA
    UNIVERSO=preprocess_features(universo)
    return UNIVERSO[['rfcencrypt', 'RFC', 'PI', MESATRASO(x[0][4:7]), MESATRASO(x[1][4:7]), MESATRASO(x[2][4:7]),
           MESATRASO(x[3][4:7]), MESATRASO(x[4][4:7]), MESATRASO(x[5][4:7]), MESCVENCIDA(x[0][4:7]), MESCVENCIDA(x[1][4:7]),
           MESCVENCIDA(x[2][4:7]), MESCVENCIDA(x[3][4:7]), MESCVENCIDA(x[4][4:7]), MESCVENCIDA(x[5][4:7])]].to_csv(NOMBRETABLA,index=False)   

hola