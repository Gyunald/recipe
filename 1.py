import pandas as pd
import streamlit as st
import datetime
import requests
from streamlit_lottie import st_lottie

st.header('Club')
c1, c2, c3 = st.columns([1,1,1])

with c1:
    st.write('[![this is an image link](https://cdn.pixabay.com/photo/2021/03/02/19/26/snowshoes-6063630_960_720.jpg)](https://www.streamlit.io/)')
    st.success('배드민턴')
with c2:
    st.image('https://cdn.pixabay.com/photo/2019/01/21/13/58/table-tenis-3946115_960_720.jpg',use_column_width=True)
    st.success('[탁구](%s)' % 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=탁구')

with c3:
    st.image('https://cdn.pixabay.com/photo/2018/03/08/20/36/ball-3209809_960_720.jpg',use_column_width=True)
    st.success('[풋살](%s)' % 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=풋살')


c4, c5, c6 = st.columns([1,1,1])

with c4:
    st.image('https://cdn.pixabay.com/photo/2015/11/20/08/17/meat-1052571_960_720.jpg',use_column_width=True)
    st.success('[파티](%s)' % 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=파티')

with c5:
    st.image('https://cdn.pixabay.com/photo/2016/04/23/20/21/smart-1348189_960_720.jpg',use_column_width=True)
    st.success('[카풀](%s)' % 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=카풀')

