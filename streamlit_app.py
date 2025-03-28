
import streamlit as st
import random
import base64

st.set_page_config(page_title="シューティングミニゲーム", layout="centered")

# パスワード入力
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    password = st.text_input("パスワードを入力してください", type="password")
    if password == "hamster123":
        st.success("認証成功！ゲームスタート！")
        st.session_state.authenticated = True
    else:
        st.stop()

# 初期化
if "score" not in st.session_state:
    st.session_state.score = 0

st.title("🎯 シューティングミニゲーム")

# 敵画像クリックで撃破
st.markdown("敵をクリックして撃退しよう！")

col1, col2, col3 = st.columns(3)
clicked = False

with col1:
    if st.button("💀 敵1"):
        clicked = True
with col2:
    if st.button("💀 敵2"):
        clicked = True
with col3:
    if st.button("💀 敵3"):
        clicked = True

# 撃破処理
if clicked:
    st.session_state.score += 1
    st.audio("sounds/hit.wav", format="audio/wav")

# スコア表示
st.subheader(f"スコア: {st.session_state.score}")

# スコア10でファンファーレ
if st.session_state.score >= 10 and "celebrated" not in st.session_state:
    st.session_state.celebrated = True
    st.balloons()
    st.success("🎉 おめでとう！スコア10達成！")
    st.audio("sounds/clear.wav", format="audio/wav")

# リセットボタン
if st.button("リセット"):
    for key in ["score", "celebrated"]:
        if key in st.session_state:
            del st.session_state[key]
    st.rerun()
