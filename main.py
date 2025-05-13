import streamlit as st
import random

# 🎨 페이지 설정
st.set_page_config(
    page_title="MBTI 진로 추천기 💼✨",
    page_icon="🎯",
    layout="centered"
)

# 🌟 타이틀
st.markdown("<h1 style='text-align: center; color: #6a1b9a;'>🌟 MBTI 기반 진로 추천기 💼✨</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>MBTI를 선택하거나 간단한 테스트로 유형을 추정해보세요! 🚀</h4>", unsafe_allow_html=True)
st.markdown("---")

# 🧩 직업 데이터
mbti_jobs = {
    "INTJ": ["전략기획가 📊", "데이터 과학자 📈", "시스템 엔지니어 🖥️"],
    "INTP": ["연구원 🔬", "이론 물리학자 🧲", "AI 개발자 🤖"],
    "ENTJ": ["CEO 🧑‍💼", "프로젝트 매니저 🗂️", "변호사 ⚖️"],
    "ENTP": ["혁신가 🧠", "광고 크리에이터 🎬", "벤처 사업가 🚀"],
    "INFJ": ["상담가 🧘", "심리학자 🧠", "작가 ✍️"],
    "INFP": ["시인 📝", "디자이너 🎨", "일러스트레이터 🖌️"],
    "ENFJ": ["교육자 👩‍🏫", "홍보 전문가 📢", "사회운동가 🌍"],
    "ENFP": ["배우 🎭", "창작자 🎥", "콘텐츠 크리에이터 📱"],
    "ISTJ": ["회계사 🧾", "공무원 🏛️", "보안 전문가 🛡️"],
    "ISFJ": ["간호사 💉", "사회복지사 🤝", "도서관 사서 📚"],
    "ESTJ": ["경영 관리자 📋", "군인 🎖️", "프로덕트 매니저 ⚙️"],
    "ESFJ": ["이벤트 플래너 🎉", "초등교사 🍎", "의료 코디네이터 🏥"],
    "ISTP": ["기계공 🧰", "파일럿 ✈️", "응급 구조사 🚑"],
    "ISFP": ["음악가 🎵", "사진작가 📸", "플로리스트 🌷"],
    "ESTP": ["스턴트맨 🤸", "세일즈맨 💼", "요리사 🍳"],
    "ESFP": ["가수 🎤", "방송인 📺", "무대 연출가 🎬"]
}

# 🎯 방법 선택
method = st.radio("MBTI를 어떻게 확인할까요?", ["직접 선택하기", "간단 테스트로 확인하기"])

# 직접 선택
user_mbti = ""
if method == "직접 선택하기":
    mbti_list = sorted(mbti_jobs.keys())
    selected_mbti = st.selectbox("당신의 MBTI를 선택하세요! 👇", mbti_list)
    user_mbti = selected_mbti

# 간단 테스트
else:
    st.markdown("#### 아래 질문에 답해보세요!")

    q1 = st.radio("1️⃣ 사람들과 함께 있을 때 에너지가 솟는다", ["예", "아니오"])
    q2 = st.radio("2️⃣ 현실적인 정보보다 직관적인 아이디어를 선호한다", ["예", "아니오"])
    q3 = st.radio("3️⃣ 결정할 때 논리보다는 감정을 더 고려한다", ["예", "아니오"])
    q4 = st.radio("4️⃣ 계획적으로 행동하는 걸 좋아한다", ["예", "아니오"])

    if st.button("📌 MBTI 추정하기"):
        mbti = ""
        mbti += "E" if q1 == "예" else "I"
        mbti += "N" if q2 == "예" else "S"
        mbti += "F" if q3 == "예" else "T"
        mbti += "J" if q4 == "예" else "P"
        user_mbti = mbti
        st.success(f"당신의 추정 MBTI는 **{mbti}**입니다!")

# 결과 출력
if user_mbti:
    st.markdown("---")
    st.markdown(f"### 🧭 {user_mbti} 유형에 추천되는 직업은?")
    jobs = mbti_jobs.get(user_mbti, ["추천 직업이 없습니다. 😢"])
    for job in jobs:
        st.markdown(f"- {job}")
    st.markdown("💡 *추천은 참고용입니다. 진로는 여러분의 열정과 선택이 가장 중요해요!*")

# 푸터
st.markdown("---")
st.markdown("<h5 style='text-align: center;'>Made with ❤️ by YourName</h5>", unsafe_allow_html=True)
