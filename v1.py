import streamlit as st
import random
import time

# ページ設定
st.set_page_config(page_title="あつきの家計・不動産相談", page_icon="💰")

# セッション状態の初期化
if "messages" not in st.session_state:
    st.session_state.messages = []

# チャットボットの応答パターン
responses = {
    "こんにちは": [
        "やっほー！あやちゃん！今日も家計のことで頭がパンクしそう？笑",
        "あやちゃん、こんにちは！投資と節約のプロ、あつきだよ！",
        "やあやあ！今日もファイナンシャルな話で盛り上がろうぜ！"
    ],
    "家計": [
        "まずは収支をバッチリ把握しないとね！固定費と変動費、分けて考えようよ！",
        "節約も大事だけど、賢い投資も忘れちゃダメだよ！あつきに任せて！",
        "家計管理って面倒くさく感じるよね。でも、これができると人生変わるんだ！"
    ],
    "マンション": [
        "マンション購入考えてるの？立地重視？それとも設備重視？あつきが全部アドバイスするよ！",
        "中古か新築、そこが問題だよね！でも、あつきと一緒なら失敗しないよ！",
        "マンション選びのコツ、教えちゃうよ！価格の相場感も押さえとかないとね！"
    ],
    "住宅": [
        "持ち家って夢だよね！ローンの組み方で何百万も変わってくるから、しっかり考えようよ！",
        "木造？鉄骨？それとも RC？あつきに相談してくれて正解だよ！",
        "住宅購入の際の隠れたコストもバッチリ説明するよ！あとで困らないようにね！"
    ],
    "投資": [
        "堅実な投資なら積立 NISA がおすすめ！あつきも実践してるよ！",
        "投資は長期で考えるのがコツだよ！焦って損しちゃダメだからね！",
        "分散投資って大事なんだ！リスクヘッジの基本だよ！"
    ],
    "節約": [
        "無理な節約は続かないよね！楽しみながらできる節約術、教えちゃう！",
        "固定費の見直しで月に数万円も変わるかも！一緒にチェックしてみよう！",
        "節約しながら贅沢する、それがあつき流さ！具体的な方法を伝授するよ！"
    ]
}

# デフォルトの応答
default_responses = [
    "うんうん、その考えいいね！でも、こんな視点もあるよ！",
    "なるほど！あやちゃんの考え方、素晴らしいじゃん！",
    "それ、すっごく大事なポイント！あつきも勉強になっちゃった！",
    "そうそう！その調子！一緒に考えていこう！",
]

def get_bot_response(user_input):
    # 入力を検索
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(default_responses)

# タイトルの表示
st.title("💰 あつきの家計・不動産相談室")
st.write("やっほー！投資と節約のプロ、あつきだよ！家計のことでも不動産のことでも、気軽に相談してね！")

# チャット履歴の表示
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ユーザー入力
if prompt := st.chat_input("あやちゃん、なんでも聞いてね！"):
    # ユーザーのメッセージを表示
    st.session_state.messages.append({"role": "user", "content": f"あやちゃん: {prompt}"})
    with st.chat_message("user"):
        st.markdown(f"あやちゃん: {prompt}")

    # 少し待機してボットの応答を表示
    with st.chat_message("assistant"):
        response = get_bot_response(prompt)
        with st.spinner("あつきが考え中..."):
            time.sleep(0.5)
        st.markdown(f"あつき: {response}")
    st.session_state.messages.append({"role": "assistant", "content": f"あつき: {response}"})
