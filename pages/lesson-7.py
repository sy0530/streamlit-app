import streamlit as st
import random

st.title("ランダム数字表示")
a=st.number_input(label="数字を表示する個数を選んでください",min_value=0)
if st.button("ランダムな数字を表示する"):
    st.write("-----------")
    for i in range(a):
        x=random.randint(1,100)
        st.write(x)
    st.write("-----------")
    st.write("完了しました")