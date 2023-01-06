import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
df = pd.read_csv('test.csv')
st.set_page_config(page_title="effervescent tablets Dashboard",  layout="wide")
st.title(":bar_chart: Efficacy of effervescent tablets Dashboard")
st.sidebar.header("Herb_Relieve")
st.sidebar.title("Please click Here:")
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

if st.sidebar.button('กราฟประสิทธิภาพของยา'):
    fig = px.bar(df, x="อายุ", y="ประสิทธิภาพ",
                 color="ประสิทธิภาพ", barmode="group")
    st.plotly_chart(fig)
else:
    st.write('')

# 2 รสชาติของยา
if st.sidebar.button('กราฟเวลาในการออกฤทธิ์'):
    fig = px.bar(df, x="อายุ", y="เวลาในการออกฤทธิ์",
                 color="เวลาในการออกฤทธิ์", barmode="group")
    st.plotly_chart(fig)
else:
    st.write('')

# #3 เวลาในการออกฤทธิ์
if st.sidebar.button('กราฟรสชาติของยา'):
    fig = px.bar(df, x="อายุ", y="รสชาติของยา",
                 color="รสชาติของยา", barmode="group")
    st.plotly_chart(fig)
else:
    st.write('')

st.sidebar.selectbox("ลำดับข้อคิดเห็นของผู้ทดสอบ", options=df["ที่"].unique())


st.subheader("เลือกกราฟก่อนดูข้อมูล(ซ้ายมือ)")


st.caption('Code')
code = '''
import pandas as pd  //import module ที่จะใช่
import streamlit as st
import plotly.express as px
df = pd.read_csv('test.csv')  //สรุปใบประเมินแล้วใส่ใน file csv
st.set_page_config(page_title="effervescent tablets Dashboard",  layout="wide")
st.title(":bar_chart: Efficacy of effervescent tablets Dashboard")
st.sidebar.header("Herb_Relieve")
st.sidebar.title("Please click Here:")
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)     //กำหนดstyleของเว็บ

#สรุปกราฟประสิทธิภาพของยาโดยใช้ if,else
if st.sidebar.button('กราฟประสิทธิภาพของยา'):
    fig = px.bar(df, x="อายุ", y="ประสิทธิภาพ",
                 color="ประสิทธิภาพ", barmode="group")
    st.plotly_chart(fig)                              //แสดงกราฟโดยใช้ Program streamlit
else:
    st.write('')

# 2 รสชาติของยา
if st.sidebar.button('กราฟเวลาในการออกฤทธิ์'):
    fig = px.bar(df, x="อายุ", y="เวลาในการออกฤทธิ์",
                 color="เวลาในการออกฤทธิ์", barmode="group")
    st.plotly_chart(fig)
else:
    st.write('')

# #3 เวลาในการออกฤทธิ์
if st.sidebar.button('กราฟรสชาติของยา'):
    fig = px.bar(df, x="อายุ", y="รสชาติของยา",
                 color="รสชาติของยา", barmode="group")
    st.plotly_chart(fig)
else:
    st.write('')

st.sidebar.selectbox("ลำดับข้อคิดเห็นของผู้ทดสอบ", options=df["ที่"].unique())
st.subheader("เลือกกราฟก่อนดูข้อมูล")
'''
st.code(code, language='python')
image = Image.open('cdDV.png')
st.image(image, caption='repo code in github ,Scan here',width=500)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
