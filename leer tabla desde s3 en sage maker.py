#Con esta codigo podemos leer tablas desde s3 en sage maker
import numpy as np
import boto3
import pandas as pd
import io

bucket = 'boi-banregio'
s3_bucket_resource = boto3.resource('s3').Bucket(bucket)
try:
 obj = s3_bucket_resource.Object('datalake/data/InteligenciaRiesgos/M&M/RSS/YCS&RSS_SEGN/RSSYCS_SEGN_RFC_LINEA/000000_0').get()
 nn = obj['Body'].read()
 gzipfile = io.BytesIO(nn)

 BURO1 = gzipfile.read()
 BURO1 = BURO1.split(b'\n')
  
 BURO1 = pd.Series(BURO1).str.decode(encoding = 'latin-1').str.split(pat = '|', expand=True)

 BURO1 = BURO1.replace('',np.nan).replace('\\N',np.nan)
 #RSSYCS_MCV_CONTEOS.columns = pd.Series(RSSYCS_MCV_CONTEOS.loc[0,:])
 BURO1.columns = ['rfc','fecha','linea_muestra','folioconsultabc','foliorespuestabc','fechabc']
 BURO1 = BURO1[:]

except Exception as e:
 print(e)
