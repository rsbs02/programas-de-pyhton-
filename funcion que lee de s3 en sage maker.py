# Importamos las librerias necesarias
import boto3

import pandas as pd
import numpy as np
import io
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from pandas.tseries.offsets import MonthEnd
from itertools import product
#from pypika import Query, Table, Field , Parameter ,Criterion
t1 = datetime.now()
print(t1)

bucket = 'boi-banregio'
s3_bucket_resource = boto3.resource('s3').Bucket(bucket)


def retrievs3(file_key, index_col=None, sep=',', header=None):
        obj = s3_bucket_resource.Object(file_key).get()
        df = pd.read_csv(
            io.BytesIO(obj['Body'].read()),
            header=header,
            index_col=index_col,
            sep='|',
            dtype=str
        )
        return df
