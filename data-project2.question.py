# -*- coding: utf-8 -*-


import pandas as pd 

df=pd.read_parquet('./ornek_dosya.parquet')

result =df[(df.duplicated(['timestamp'])) & (df.duplicated(['latitude','longitude'])==False)& (df.duplicated('id')==False)]['id']#control id for this situations
                                          
print (result)