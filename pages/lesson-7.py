import streamlit as st
import random

#unsei={"1:大吉"
#       "2:中吉"
#       "3:中吉"
#       "4:小吉"
#       "5:小吉"
#       "6:小吉"
#       "7:小吉"
#       "8:"
#}

st.title("ランダム数字表示")
a=st.number_input(label="数字を表示する個数を選んでください",min_value=0)
if st.button("ランダムな数字を表示する"):
    for i in range(a):
        x=random.randint(1,100)
        st.write(x)