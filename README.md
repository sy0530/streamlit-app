# streamlit.app
このアプリは乱数を生成します。
次のコマンドで起動します

```
streamlit run C:\Users\sanas\OneDrive\ドキュメント\github\streamlit-app\pages\lesson-7.py
```

---

**使い方**
* 乱数をいくつ生成するか選んで、数字を入力して下さい
* 数字を入力した後にボタンを押すと、乱数が数字個ぶん生成されます


**注意**
* 乱数を生成する数は整数のみ入力できます
* 乱数は1~100の整数を生成します
* 乱数は重複することもあります

---
**コード**
```py

import streamlit as st
import random

st.title("ランダム数字表示")
a=st.number_input(label="数字を表示する個数を選んでください",min_value=0)
if st.button("ランダムな数字を表示する"):
    for i in range(a):
        x=random.randint(1,100)
        st.write(x)
