import streamlit as st

with st.sidebar:
    st.multiselect('multiselect',[1,2,3])
    st.selectbox('select',[1,2,3])
    st.date_input("date")
    st.time_input('time')

st.markdown('###### We are cooks! :+1:') # 마크다운 안에서는 # 갯수로 텍스트 굵기 설정
st.markdown('###### *From july 31st, 2022*')
st.markdown('###### made by kyudeok and jinju :heart:')