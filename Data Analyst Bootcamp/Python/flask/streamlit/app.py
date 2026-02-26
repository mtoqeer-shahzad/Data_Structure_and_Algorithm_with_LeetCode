import streamlit as st
import pandas as pd
import numpy as np


st.title("My first App")

df=(
    {
        "first_column":[1,2,3,4,5],
        "2nd_column":[6,7,8,9]
        
    }
)

st.write("Hy Dear")
st.write(df)


st.slider("AGE",0,100,25)

#create a charts

chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)

st.line_chart(chart_data)