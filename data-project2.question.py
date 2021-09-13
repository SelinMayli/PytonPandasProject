# -*- coding: utf-8 -*-


import pandas as pd 

df=pd.read_parquet('./ornek_dosya.parquet')

result=df.astype({"latitude":str,"longitude":str})#change colums type

result["lat_long"] = result["latitude"] +','+ result["longitude"]#merge columns 

result_id =result[(result.duplicated(['timestamp'])) & (result.duplicated("lat_long")==False)]['id'].value_counts()#control id for this situations
                                        
print (result_id)