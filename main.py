import folium
import pandas as pd
import numpy as np
import requests
import json

covid19_json = requests.get("https://dashboards-dev.sprinklr.com/data/9043/global-covid19-who-gis.json").text
covid19_json = json.loads(covid19_json)
data_covid19=covid19_json["rows"]
data_columns=["day","Country","Region","Deaths","Cumulative Deaths","Confirmed","Cumulative Confirmed"]
covid19_df=pd.DataFrame(data_covid19,columns=data_columns)
m=folium.Map()
geourl = "https://www.bobobk.com/wp-content/uploads/2020/05/world-countries.json"
geodata=requests.get(geourl).text
df_abb=pd.read_csv("4country_abb.csv")
dic_abb = {df_abb.iloc[i, 1]: df_abb.iloc[i, 0] for i in range(np.shape(df_abb)[0])}
covid19_df['fullname'] = covid19_df['Country'].map(dic_abb)
covid19_df['log_Cumulative_Confirmed']=np.log(covid19_df['Cumulative Confirmed']+1)
folium.Choropleth(geo_data=geodata, name="covid-19 total confirm map", data=covid19_df,
                  columns=["fullname", "log_Cumulative_Confirmed"], key_on="feature.properties.name",
                  fill_color='PuRd', nan_fill_color='white').add_to(m)
folium.map.Marker(
    location=[0, 0],  # 具体位置
    icon=folium.DivIcon(html='<div style="font-size: 24px; color: red;">杨承宇 6020224625</div>')  # 姓名信息
).add_to(m)
m.save("2.html")