import pandas as pd
from datetime import datetime
import os
def seconds(time):
        t0=datetime(1970,1,1)
        delta=time-t0
        return delta.total_seconds()
def json_to_csv(i):
    jsonfile='./Desktop/nckh_sv/dataset/EMA/response/Stress'+f'/Stress_u{i:02d}.json'
    csvfile=f'/Users/khangphan/Desktop/Stress_csv_new/Stress_u{i:02d}.csv'
    print(csvfile)
    df=pd.read_json(jsonfile)
    df=df[['level','resp_time']]
    df['resp_time']=df['resp_time']
    df['time']=df['resp_time'].apply(lambda time: seconds(time))
    if i==0:
        print(df)

    df=df.dropna()
 
    df.to_csv(csvfile)
for i in range(60):
    try:
        json_to_csv(i)
    except:
        pass

print(1)
print(os.getcwd())
