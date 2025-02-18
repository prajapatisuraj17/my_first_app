import streamlit as st
import pandas as pd
df=pd.read_csv('data.
category=df[company]
values=df[mileage]
plt.bar(category,values,color='blue')