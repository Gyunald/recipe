import streamlit as st
from PIL import  Image

img = Image.open('C:/Users/kdkim/Desktop/UNC.jpg') # 파일 경로
c1,c2 = st.columns([1,1]) # 컬럼을 2등분 한다는 뜻. 1은 비율 1:1 1:0.5 등 변경가능 
# c1,c2 = st.columns(2,gap='large') # gap = small,medium,large

with c1: # 분할 된 컬럼 사용시 with 컬럼명 :
    st.image(img,'unc')
    st.markdown( # '*' 
        '''
        * first line 
        * second line
        * third line
        '''
    )

    st.text_area('d')
with c2:
    st.image(img,"unc2")
    st.markdown( # '*' 
    '''
    * first line 
    * second line
    * third line
    '''
)
    st.text_area('f')