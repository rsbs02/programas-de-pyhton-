#Eliminamos los espacios nulos que se formar por procesar la información de s3 a sage maker
buro1 = BURO1[(BURO1['rfc'].notnull())][['rfc','fecha','linea_muestra','folioconsultabc','foliorespuestabc','fechabc']]
