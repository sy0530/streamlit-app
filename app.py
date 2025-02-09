import streamlit as st
import random

if "count" not in st.session_state:
    st.session_state.count=0
if "gamecount" not in st.session_state:
    st.session_state.gamecount=0
user_hands=["グー","チョキ","パー"]
computure_hand=random.randint(1,3)
if computure_hand==1:
    computure_hand=("グー")
elif computure_hand==2:
    computure_hand=("チョキ")
elif computure_hand==3:
    computure_hand=("パー")

def hanntei(user_hand):
    if user_hand=="グー":
        if computure_hand=="グー":
            st.write("あいこ!")
        if computure_hand=="チョキ":
            st.write("あなたの勝ち!")
            st.session_state.count+=1
        if computure_hand=="パー":
            st.write("コンピュータの勝ち!")
    if user_hand=="チョキ":
        if computure_hand=="グー":
            st.write("コンピュータの勝ち!")
        if computure_hand=="チョキ":
            st.write("あいこ!")
        if computure_hand=="パー":
            st.write("あなたの勝ち!")
            st.session_state.count+=1
    if user_hand=="パー":
        if computure_hand=="グー":
            st.write("あなたの勝ち!")
            st.session_state.count+=1
        if computure_hand=="チョキ":
            st.write("コンピュータの勝ち!")
        if computure_hand=="パー":
            st.write("あいこ!")
    return st.session_state.count

st.title("じゃんけんアプリ")
st.header("じゃんけんをしよう！")
st.write("グー、チョキ、パーのどれかを出してね")

user_hand=st.selectbox(label="選択肢",options=user_hands)
if st.button("決定"): 
    st.session_state.gamecount=st.session_state.gamecount+1
    st.write("結果は…")
    st.write("あなたの手:"+user_hand)
    st.write("コンピュータの手:"+computure_hand)
    hanntei(user_hand)
    st.button("もう一度じゃんけんをする")  
    st.write("-じゃんけんした回数："+str(st.session_state.gamecount)+"-")
    st.write("-あなたが勝った回数："+str(st.session_state.count)+"-")
    syouritu=int(st.session_state.count)/int(st.session_state.gamecount)*100
    syouritu=round(syouritu,1)
    st.write("-勝率："+str(syouritu)+"%-")
elif st.button("成績をリセットする"):
    st.session_state.count=0
    st.session_state.gamecount=0
    syouritu=0
    st.write("-成績がリセットされました-")