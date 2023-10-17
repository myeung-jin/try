
import streamlit as st
import pandas as pd

st.title('2021 서울교통공사 지하철 월별 하차 인원')

df = pd.read_csv('/content/drive/MyDrive/경영_dashboard/data/서울교통공사_월별 하차인원_20211231.csv', encoding='cp949')
df.set_index = df['연번']

if st.button('data copyright link'):
    st.write('https://www.data.go.kr/data/15044247/fileData.do')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)

st.subheader('역별 하차 인원')
option = st.selectbox(
    'Select Line',
    (df['역명']))

station_data = df.loc[(df['역명'] == option)]
station_data = station_data[station_data.columns.difference(['연번', '호선', '역번호', '역명'])]
s_index = station_data.index.tolist()
st.area_chart(station_data.loc[s_index[0]], use_container_width=True)

st.subheader('전체 역별 하차 인원')
e_station = df[['역명', '2021년1월', '2021년2월', '2021년3월', '2021년4월',
       '2021년5월', '2021년6월', '2021년7월', '2021년8월', '2021년9월', '2021년10월', '2021년11월']].transpose()
e_station.rename(columns=e_station.iloc[0], inplace=True)
e_station = e_station.drop(e_station.index[0])
st.line_chart(e_station)

st.subheader('호선별 하차 인원')
df_line = df.groupby('호선').sum()
lines = df_line.index.tolist()
option = st.selectbox(
    'Select Line',
    (lines))

line_data = df_line.loc[(df_line.index == option)]
line_data = line_data[line_data.columns.difference(['연번', '호선', '역번호', '역명'])]
l_index = line_data.index.tolist()
st.area_chart(line_data.loc[l_index[0]], use_container_width=True)
