import streamlit as st

# 🎨 페이지 설정
st.set_page_config(
    page_title="MBTI 진로 추천기 💼✨",
    page_icon="🎯",
    layout="centered"
)

# 🌈 사용자 정의 스타일
st.markdown("""
    <style>
    body {
        background-color: #fce4ec;
        color: #4a148c;
    }
    .stSelectbox, .stButton {
        font-size: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 🌟 타이틀
st.markdown("<h1 style='text-align: center; color: #6a1b9a;'>🌟 MBTI 기반 진로 추천기 💼✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>당신의 MBTI를 선택하고, 어울리는 직업을 확인해보세요! 🚀</h3>", unsafe_allow_html=True)

# 🧩 MBTI 리스트
mbti_list = [
    "INTJ 🧠", "INTP 🧪", "ENTJ 🦾", "ENTP 🔬",
    "INFJ 🧙‍♂️", "INFP 🎨", "ENFJ 📣", "ENFP 🌈",
    "ISTJ 📚", "ISFJ 🛡️", "ESTJ 🧱", "ESFJ 💐",
    "ISTP 🛠️", "ISFP 🎸", "ESTP 🏍️", "ESFP 🎤"
]

mbti = st.selectbox("당신의 MBTI를 선택하세요! 👇", mbti_list)

# 🧭 추천 데이터
mbti_jobs = {
    "INTJ 🧠": ["전략기획가 📊", "데이터 과학자 📈", "시스템 엔지니어 🖥️"],
    "INTP 🧪": ["연구원 🔬", "이론 물리학자 🧲", "AI 개발자 🤖"],
    "ENTJ 🦾": ["CEO 🧑‍💼", "프로젝트 매니저 🗂️", "변호사 ⚖️"],
    "ENTP 🔬": ["혁신가 🧠", "광고 크리에이터 🎬", "벤처 사업가 🚀"],
    "INFJ 🧙‍♂️": ["상담가 🧘", "심리학자 🧠", "작가 ✍️"],
    "INFP 🎨": ["시인 📝", "디자이너 🎨", "일러스트레이터 🖌️"],
    "ENFJ 📣": ["교육자 👩‍🏫", "홍보 전문가 📢", "사회운동가 🌍"],
    "ENFP 🌈": ["배우 🎭", "창작자 🎥", "콘텐츠 크리에이터 📱"],
    "ISTJ 📚": ["회계사 🧾", "공무원 🏛️", "보안 전문가 🛡️"],
    "ISFJ 🛡️": ["간호사 💉", "사회복지사 🤝", "도서관 사서 📚"],
    "ESTJ 🧱": ["경영 관리자 📋", "군인 🎖️", "프로덕트 매니저 ⚙️"],
    "ESFJ 💐": ["이벤트 플래너 🎉", "초등교사 🍎", "의료 코디네이터 🏥"],
    "ISTP 🛠️": ["기계공 🧰", "파일럿 ✈️", "응급 구조사 🚑"],
    "ISFP 🎸": ["음악가 🎵", "사진작가 📸", "플로리스트 🌷"],
    "ESTP 🏍️": ["스턴트맨 🤸", "세일즈맨 💼", "요리사 🍳"],
    "ESFP 🎤": ["가수 🎤", "방송인 📺", "무대 연출가 🎬"]
}

# 🎯 결과 출력
if mbti:
    selected_key = mbti.split(" ")[0] + " " + mbti.split(" ")[1]
    jobs = mbti_jobs.get(selected_key, ["추천 직업이 없습니다. 😢"])
    
    st.markdown("### 🔍 추천 직업 리스트:")
    for job in jobs:
        st.markdown(f"- {job}")
    
    st.markdown("---")
    st.markdown("💡 *추천은 재미로 봐주세요. 진짜 진로는 스스로 개척하는 거예요!* 💪")

# 🎁 푸터
st.markdown("---")
st.markdown("<h5 style='text-align: center;'>Made with ❤️ by YUN</h5>", unsafe_allow_html=True)
