import seaborn as sns
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Titanic Data Analysis - streamlit')

df = sns.load_dataset('titanic')
#st.dataframe(df)


st.sidebar.header('User Input Parameter')
#c = st.sidebar.selectbox('Select The Class', df['class'].unique())
#g = st.sidebar.selectbox('Select The Class', df['sex'].unique())

plot_type = st.sidebar.radio('Select The Plot Type',('bar','line','hist','box','kde'))

if plot_type == 'bar':
    st.write('Bar plot')
    fig, ax = plt.subplots()
    df.groupby(['class', 'sex'])['survived'].mean().unstack().plot(kind='bar', ax=ax)
    st.pyplot(fig)

elif plot_type == 'line':
    st.write('Line plot')
    fig, ax = plt.subplots()
    df.groupby(['class', 'sex'])['survived'].mean().unstack().plot(kind='line', ax=ax)
    st.pyplot(fig)



elif plot_type == 'hist':
    st.write('Hist plot')
    fig, ax = plt.subplots()
    df.groupby(['class', 'sex'])['survived'].mean().unstack().plot(kind='hist', ax=ax)
    st.pyplot(fig)

elif plot_type == 'box':
    st.write('Box plot')
    fig, ax = plt.subplots()
    df.groupby(['class', 'sex'])['survived'].mean().unstack().plot(kind='box', ax=ax)
    st.pyplot(fig)

elif plot_type == 'kde':
    st.write('Kde plot')
    fig, ax = plt.subplots()
    df.groupby(['class', 'sex'])['survived'].mean().unstack().plot(kind='kde', ax=ax)
    st.pyplot(fig)

hide_menu = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)
