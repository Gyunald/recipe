import streamlit as st
from PIL import Image
 
img = Image.open('C:/Users/kdkim/Desktop/UNC.jpg') # 파일 경로

tab1, tab2, tab3 = st.tabs(["A", "B", "C"])

with tab1: # 분할 된 컬럼 사용시 with 컬럼명 :
    st.image(img,'unc',width=300)
    st.markdown( # '*' 
        '''
        * first line 
        * second line
        * third line
        '''
    )

    st.text_area('d','ddd')

with tab2: # 분할 된 컬럼 사용시 with 컬럼명 :
    st.image(img,'unc1',width=300)
    st.markdown( # '*' 
        '''
        * first line 
        * second line
        * third line
        '''
    )

    st.text_area('d','dddd')

with tab3: # 분할 된 컬럼 사용시 with 컬럼명 :
    st.image(img,'unc2',width=300)
    st.markdown( # '*' 
        '''
        * first line 
        * second line
        * third line
        '''
    )

    st.text_area('d','ddddd')