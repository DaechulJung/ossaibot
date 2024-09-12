import openai
import streamlit as st
from streamlit_chat import message

# OpenAI API Key 설정
openai.api_key = "your_openai_api_key"  # 환경 변수로 설정하는 것을 권장

# Streamlit 페이지 설정
st.set_page_config(page_title="Chatbot", page_icon=":robot_face:")

# 챗봇의 초기 상태 저장
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

# OpenAI API 호출 함수
def generate_response(prompt):
    # response = openai.Completion.create(
    #     engine="text-davinci-003",  # 또는 다른 엔진 사용 가능
    #     prompt=prompt,
    #     max_tokens=150,
    #     n=1,
    #     stop=None,
    #     temperature=0.7,
    # )
    # message = response.choices[0].text.strip()
    message = "hello world"
    return message

# 사용자 입력
st.title("Chatbot with Streamlit")
user_input = st.text_input("You: ", "Hello, how are you?", key="input")

if user_input:
    # OpenAI API를 통해 답변 생성
    output = generate_response(user_input)

    # 대화 기록을 저장
    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(output)

# 채팅 UI 표시
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state['generated'][i], key=str(i))