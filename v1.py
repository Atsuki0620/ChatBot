import streamlit as st
import random
import time

# ページ設定
st.set_page_config(page_title="シンプルチャットボット", page_icon="🤖")

# セッション状態の初期化
if "messages" not in st.session_state:
    st.session_state.messages = []

# チャットボットの応答パターン
responses = {
    "こんにちは": ["こんにちは！", "やあ！", "お元気ですか？"],
    "元気": ["それは良かったです！", "私も元気です！"],
    "さようなら": ["さようなら！", "また会いましょう！", "良い一日を！"],
    "天気": ["今日は良い天気ですね！", "天気の話題は好きですか？"],
    "趣味": ["私は会話をすることが好きです！", "新しいことを学ぶのが趣味です。"],
}

# デフォルトの応答
default_responses = [
    "なるほど、そうなんですね。",
    "もう少し詳しく教えていただけますか？",
    "興味深いお話ですね。",
    "そうなんですか！",
]

def get_bot_response(user_input):
    # 入力を小文字化して検索
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(default_responses)

# タイトルの表示
st.title("🤖 シンプルチャットボット")
st.write("簡単な会話ができるチャットボットです。「こんにちは」「天気」「趣味」などについて話しかけてみてください。")

# チャット履歴の表示
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ユーザー入力
if prompt := st.chat_input("メッセージを入力してください"):
    # ユーザーのメッセージを表示
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 少し待機してボットの応答を表示
    with st.chat_message("assistant"):
        response = get_bot_response(prompt)
        with st.spinner("考え中..."):
            time.sleep(0.5)  # 応答に少し遅延を入れる
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
