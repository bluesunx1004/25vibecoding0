import streamlit as st 

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

# 🧩 직업 및 전공 데이터
mbti_jobs = {
    "INTJ": [{"job": "전략기획가 📊", "majors": ["경영학", "경제학", "정책학"]},
             {"job": "데이터 과학자 📈", "majors": ["통계학", "컴퓨터공학", "산업공학"]},
             {"job": "시스템 엔지니어 🖥️", "majors": ["소프트웨어공학", "전산학", "정보통신공학"]}],
    "INTP": [{"job": "연구원 🔬", "majors": ["물리학", "생명과학", "화학"]},
             {"job": "이론 물리학자 🧲", "majors": ["물리학", "천문학"]},
             {"job": "AI 개발자 🤖", "majors": ["컴퓨터공학", "전산학", "인공지능"]}],
    "ENTJ": [{"job": "CEO 🧑‍💼", "majors": ["경영학", "경제학", "산업공학"]},
             {"job": "프로젝트 매니저 🗂️", "majors": ["경영학", "IT경영", "산업디자인"]},
             {"job": "변호사 ⚖️", "majors": ["법학", "행정학"]}],
    "ENTP": [{"job": "혁신가 🧠", "majors": ["벤처창업학", "디자인공학", "기술경영"]},
             {"job": "광고 크리에이터 🎬", "majors": ["광고홍보학", "커뮤니케이션학"]},
             {"job": "벤처 사업가 🚀", "majors": ["창업학", "경영학"]}],
    "INFJ": [{"job": "상담가 🧘", "majors": ["심리학", "사회복지학"]},
             {"job": "심리학자 🧠", "majors": ["심리학"]},
             {"job": "작가 ✍️", "majors": ["문예창작", "국어국문학"]}],
    "INFP": [{"job": "시인 📝", "majors": ["국어국문학", "문예창작"]},
             {"job": "디자이너 🎨", "majors": ["시각디자인", "제품디자인"]},
             {"job": "일러스트레이터 🖌️", "majors": ["회화", "애니메이션", "디지털아트"]}],
    "ENFJ": [{"job": "교육자 👩‍🏫", "majors": ["교육학", "유아교육", "초등교육"]},
             {"job": "홍보 전문가 📢", "majors": ["광고홍보학", "커뮤니케이션학"]},
             {"job": "사회운동가 🌍", "majors": ["사회학", "정치외교학"]}],
    "ENFP": [{"job": "배우 🎭", "majors": ["연극영화학", "공연예술학"]},
             {"job": "창작자 🎥", "majors": ["영상디자인", "애니메이션"]},
             {"job": "콘텐츠 크리에이터 📱", "majors": ["디지털미디어", "미디어커뮤니케이션"]}],
    "ISTJ": [{"job": "회계사 🧾", "majors": ["회계학", "경영학"]},
             {"job": "공무원 🏛️", "majors": ["행정학", "정치외교학"]},
             {"job": "보안 전문가 🛡️", "majors": ["정보보호학", "컴퓨터공학"]}],
    "ISFJ": [{"job": "간호사 💉", "majors": ["간호학"]},
             {"job": "사회복지사 🤝", "majors": ["사회복지학"]},
             {"job": "도서관 사서 📚", "majors": ["문헌정보학"]}],
    "ESTJ": [{"job": "경영 관리자 📋", "majors": ["경영학", "산업공학"]},
             {"job": "군인 🎖️", "majors": ["국방학", "행정학"]},
             {"job": "프로덕트 매니저 ⚙️", "majors": ["산업디자인", "컴퓨터공학", "IT경영"]}],
    "ESFJ": [{"job": "이벤트 플래너 🎉", "majors": ["호텔관광학", "이벤트경영학"]},
             {"job": "초등교사 🍎", "majors": ["초등교육학"]},
             {"job": "의료 코디네이터 🏥", "majors": ["보건행정학", "의료경영학"]}],
    "ISTP": [{"job": "기계공 🧰", "majors": ["기계공학", "로봇공학"]},
             {"job": "파일럿 ✈️", "majors": ["항공운항학", "항공우주공학"]},
             {"job": "응급 구조사 🚑", "majors": ["응급구조학"]}],
    "ISFP": [{"job": "음악가 🎵", "majors": ["실용음악", "작곡", "음악학"]},
             {"job": "사진작가 📸", "majors": ["사진영상학", "시각디자인"]},
             {"job": "플로리스트 🌷", "majors": ["원예학", "플로리스트학"]}],
    "ESTP": [{"job": "스턴트맨 🤸", "majors": ["스포츠과학", "연극영화"]},
             {"job": "세일즈맨 💼", "majors": ["마케팅학", "경영학"]},
             {"job": "요리사 🍳", "majors": ["조리학", "외식경영학"]}],
    "ESFP": [{"job": "가수 🎤", "majors": ["실용음악", "보컬전공"]},
             {"job": "방송인 📺", "majors": ["방송연예학", "커뮤니케이션학"]},
             {"job": "무대 연출가 🎬", "majors": ["연극학", "공연예술학"]}]
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

        st.markdown(
            """
            🧪 **더 정밀한 MBTI 검사를 원하시나요?**  
            [👉 정식 MBTI 검사 받기 (16Personalities)](https://www.16personalities.com/ko)
            """,
            unsafe_allow_html=True
        )

# 결과 출력
if user_mbti:
    st.markdown("---")
    st.markdown(f"### 🧭 {user_mbti} 유형에 추천되는 진로 정보는?")
    job_list = mbti_jobs.get(user_mbti, [])

    if not job_list:
        st.warning("추천 직업이 없습니다. 😢")
    else:
        for item in job_list:
            st.markdown(f"**직업**: {item['job']}")
            st.markdown(f"🧑‍🎓 **관련 전공**: {', '.join(item['majors'])}")
            st.markdown("")

    st.markdown("💡 *추천은 참고용입니다. 진로는 여러분의 열정과 선택이 가장 중요해요!*")

# 푸터
st.markdown("---")
st.markdown("<h5 style='text-align: center;'>Made with ❤️ by YourName</h5>", unsafe_allow_html=True)
