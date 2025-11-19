import streamlit as st
import google.generativeai as genai

# 1. 페이지 설정
st.set_page_config(page_title="쪼아쌤의 AI 도우미", page_icon="🤖")

# 2. 제목
st.title("🤖 쪼아쌤의 AI 교실")
st.write("궁금한 것을 물어보세요! 제가 친절하게 알려줄게요.")

# 3. 비밀번호(API 키) 설정 (나중에 입력할 거야)
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
else:
    api_key = st.text_input("Google API Key를 입력하세요", type="password")

# 4. AI와 대화하기
if api_key:
    # AI 설정
    genai.configure(api_key=api_key)
    
    # 쪼아쌤이 AI Studio에서 쓴 프롬프트나 설정을 여기에 넣는 거야.
    # 지금은 기본 모델로 설정할게.
    model = genai.GenerativeModel('gemini-1.5-flash')

    # 사용자가 입력하는 곳
    user_input = st.text_input("질문을 입력하세요:")

    if user_input:
        with st.spinner('AI가 생각 중입니다...'):
            try:
                response = model.generate_content(user_input)
                st.success("답변이 도착했습니다!")
                st.write(response.text)
            except Exception as e:
                st.error(f"에러가 났어요: {e}")
