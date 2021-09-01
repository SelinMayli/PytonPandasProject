import pandas as pd 

df=pd.read_parquet('./ornek_dosya.parquet')

result=df
result=result.astype({"latitude":str,"longitude":str})#change colums type

result["lat_long"] = result["latitude"] + result["longitude"]#merge columns 


result =result[result.duplicated("lat_long")==False]#control duplicate or not 
result1 = result['lat_long'].value_counts()#count values
result2 =result.head(3)#return first 3 rows 

print (result2)#print result2


result3 =result[(result['lat_long']=='41.020928.9217') |(result['lat_long']=='41.064428.9228') |(result['lat_long']=='41.053828.9374')]['id'].value_counts()
#control id 
# result3=result3.head(9)

print(result3)

