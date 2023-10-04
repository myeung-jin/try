import streamlit as st
st.write('# Hello World')
st.write('# 이제 스트림릿으로 인터넷 페이지 공유시작')

view = [100,150,30]
st.write('# Youtube view')
view
st.write('# bar chart')
st.bar_chart(view)
import pandas as pd
sview = pd.Series(view)

