import streamlit as st
import matplotlib.pyplot as plt
# 간단한 bar_chart 대체 예시
import pandas as pd

if stats:
    st.markdown("#### 📊 직업 관련 통계")
    df = pd.DataFrame({
        '항목': ['인기도 (%)', '평균 연봉 (만원)'],
        '값': [stats["인기도"], stats["평균연봉"]]
    })
    df.set_index('항목', inplace=True)
    st.bar_chart(df)

# 페이지 설정
st.set_page_config(
    page_title="MBTI 진로 추천기 💼✨",
    page_icon="🎯",
    layout="centered"
)

# 사용자 정의 스타일
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

st.markdown("<h1 style='text-align: center; color: #6a1b9a;'>🌟 MBTI 기반 진로 추천기 💼✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>당신의 MBTI를 선택하고, 어울리는 직업을 확인해보세요! 🚀</h3>", unsafe_allow_html=True)

mbti_list = [
    "INTJ 🧠", "INTP 🧪", "ENTJ 🦾", "ENTP 🔬",
    "INFJ 🧙‍♂️", "INFP 🎨", "ENFJ 📣", "ENFP 🌈",
    "ISTJ 📚", "ISFJ 🛡️", "ESTJ 🧱", "ESFJ 💐",
    "ISTP 🛠️", "ISFP 🎸", "ESTP 🏍️", "ESFP 🎤"
]

# MBTI 선택
mbti = st.selectbox("당신의 MBTI를 선택하세요! 👇", mbti_list)

# MBTI 추천 직업 + 설명
mbti_jobs = {
    "INTJ 🧠": [
        ("전략기획가 📊", "기업이나 조직의 장기적인 방향을 설정하고 전략을 수립하는 역할."),
        ("데이터 과학자 📈", "데이터를 분석하여 인사이트를 도출하고 모델을 개발하는 직업."),
        ("시스템 엔지니어 🖥️", "IT 시스템의 설계, 구축, 운영을 담당하는 기술 전문가.")
    ],
    "ENFP 🌈": [
        ("배우 🎭", "다양한 캐릭터를 연기하며 사람들에게 감정을 전달하는 예술가."),
        ("창작자 🎥", "콘텐츠를 기획하고 만들어내는 자유로운 사고의 예술가."),
        ("콘텐츠 크리에이터 📱", "SNS나 유튜브 등을 통해 창의적인 콘텐츠를 제작하고 공유하는 사람.")
    ],
    # 나머지 MBTI도 동일하게 추가 가능
}

# 직업 통계 (인기 순위 및 연봉)
job_stats = {
    "전략기획가 📊": {"인기도": 85, "평균연봉": 7000},
    "데이터 과학자 📈": {"인기도": 95, "평균연봉": 8500},
    "시스템 엔지니어 🖥️": {"인기도": 75, "평균연봉": 6500},
    "배우 🎭": {"인기도": 90, "평균연봉": 4000},
    "창작자 🎥": {"인기도": 80, "평균연봉": 3500},
    "콘텐츠 크리에이터 📱": {"인기도": 92, "평균연봉": 4500}
}

# 직업 추천 & 설명
if mbti:
    selected_key = mbti
    jobs = mbti_jobs.get(selected_key, [])

    st.markdown("### 🔍 추천 직업 리스트 (클릭해서 설명 보기):")
    for job_name, job_desc in jobs:
        if st.button(f"🔎 {job_name}"):
            st.markdown(f"#### 📘 {job_name} 설명")
            st.markdown(f"{job_desc}")

            # 통계 그래프 시각화
            stats = job_stats.get(job_name)
            if stats:
                st.markdown("#### 📊 직업 관련 통계")
                fig, ax = plt.subplots()
                ax.bar(["인기도 (%)", "평균 연봉 (만원)"], [stats["인기도"], stats["평균연봉"]])
                ax.set_ylim(0, max(stats["평균연봉"] + 1000, 100))
                st.pyplot(fig)

st.markdown("---")
st.markdown("💡 *추천은 참고용이에요. 진짜 진로는 당신의 선택에서 시작됩니다!* 💪")
st.markdown("<h5 style='text-align: center;'>Made with ❤️ by YourName</h5>", unsafe_allow_html=True)
