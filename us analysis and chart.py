import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

#json資料來源:https://api.covid19api.com/
with open('covid19_us_confirm.json', 'r') as read_file:
    data = json.load(read_file)  #注意json.load()轉成python後,會變成dict資料型態

confirmed_df = pd.DataFrame(data,columns=['Date','Cases'])
confirmed_df.rename(columns={'Cases':'Confirmed'}, inplace = True)


with open('covid19_us_death.json','r') as read_us_death:
    death_data = json.load(read_us_death)

death_df = pd.DataFrame(death_data,columns=['Cases'])
death_df.rename(columns={'Cases':'Deaths'}, inplace = True)

with open('covid19_us_recoverd.json','r') as read_us_recovered:
    recovered_data = json.load(read_us_recovered)

recovered_df = pd.DataFrame(recovered_data,columns=['Cases'])
recovered_df.rename(columns={'Cases':'Recovered'},inplace = True)

#合併雙ＤataFrame, axis = 0 直項合併, axis = 1 橫向合併
res = pd.concat([confirmed_df,death_df,recovered_df],axis=1)

rate = res.loc[:,['Date','Confirmed','Deaths','Recovered']]
rate.eval('Death_Rate =  Deaths/Confirmed',inplace=True)
rate.eval('Recoverd_Rate = Recovered/Confirmed',inplace = True)

#取出繪圖所需資訊
Time=res.loc[:,'Date']
Confirmed_Cases=res.loc[:,'Confirmed']
Deaths_Cases=res.loc[:, 'Deaths']
Recovered_Cases=res.loc[:, 'Recovered']
#繪圖
plt.plot(Time, Confirmed_Cases,'s-',color='r',label='Confirmed Cases')
plt.plot(Time, Deaths_Cases, 'o-',color='g',label='Deaths Cases')
plt.plot(Time, Recovered_Cases, '.-', color='b',label='Recovered Cases')
#設定折線圖名稱與標題
plt.title('3-Months Trend for US Cases')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.savefig('US_Cases_Trend.png')
