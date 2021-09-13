import pandas as pd 

df=pd.read_parquet('./ornek_dosya.parquet')

result=df.astype({"latitude":str,"longitude":str})#change colums type

result["lat_long"] = result["latitude"] +','+ result["longitude"]#merge columns 


result =result[result.duplicated("lat_long")]["lat_long"].value_counts()#control duplicate or not 

print (result)#print result
