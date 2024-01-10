import pandas as pd
from datetime import datetime
import os
def seconds(time):
        t0=datetime(1970,1,1)
        delta=time-t0
        return delta.total_seconds()
def to_date_time(x):
    return datetime.fromtimestamp(x)
def json_to_csv(i):
    jsonfile='./dataset/EMA/response/Stress'+f'/Stress_u{i:02d}.json'
    csvfile=f'./Stress_csv_new1/Stress_u{i:02d}.csv'
    print(csvfile)
    df=pd.read_json(jsonfile)
    df=df[['level','resp_time']]
    df['resp_time']=df['resp_time']
    df['time']=df['resp_time'].apply(lambda time: seconds(time))-3600*5
    df['resp_time']=df['time'].apply(lambda x: to_date_time(x))
    if i==0:
        print(df)

    df=df.dropna()
 
    df.to_csv(csvfile)
for i in range(60):
    try:
        json_to_csv(i)
    except:
        print('error')

        pass

print(1)
print(os.getcwd())
