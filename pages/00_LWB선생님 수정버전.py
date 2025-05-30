import streamlit as st

# MBTI 정보
mbti_info = {
    "INTJ": {
        "title": "🧠 INTJ - 전략가형",
        "description": "논리적이고 분석적인 사고를 가진 전략가입니다. 혼자 있는 것을 즐기며 독립적인 성향이 강합니다.",
        "tips": [
            "🧩 계획적이고 명확한 상담 구조를 제공해 주세요.",
            "🗂️ 사전 정보를 충분히 주고 스스로 생각할 시간을 주세요.",
            "📊 논리적 근거와 자료를 활용한 피드백을 선호합니다."
        ],
        "example": [
            "**상담교사:** 최근 진로에 대해 어떤 생각을 하고 있어요?",
            "**INTJ 학생:** 구체적인 계획은 아직 없지만, 혼자서 관련 자료들을 조사해 보고 있어요.",
            "**상담교사:** 좋아요. 그 자료들을 바탕으로 내가 도와줄 수 있는 부분이 있다면 말해줘요. 필요한 정보나 구조적인 가이드를 함께 만들어보자구요. 📘"
        ],
        "career": ["🔬 과학자", "📈 데이터 분석가", "🧠 연구개발 전문가"],
        "keywords": ["자료 조사", "계획", "논리적", "스스로 해결", "효율성"]
    },
    "ENFP": {
        "title": "🌈 ENFP - 활동가형",
        "description": "열정적이고 창의적이며 다른 사람들과의 교류를 즐깁니다. 감정이입 능력이 뛰어납니다.",
        "tips": [
            "🎨 감성적 공감과 따뜻한 피드백이 중요해요.",
            "📢 자유롭게 자신의 이야기를 펼칠 수 있도록 도와주세요.",
            "🧶 너무 틀에 얽매인 방식보다 유연한 접근이 좋아요."
        ],
        "example": [
            "**상담교사:** 요즘 학교생활은 어때요?",
            "**ENFP 학생:** 요즘은 뭔가 재밌는 걸 하고 싶은데 어디에 에너지를 써야 할지 모르겠어요.",
            "**상담교사:** 그런 마음이 드는 건 정말 멋진 감정이에요! 😄 혹시 최근에 관심이 생긴 분야가 있다면 이야기해 줄래요? 자유롭게 편하게 말해도 돼요."
        ],
        "career": ["🎭 예술가", "📚 교육자", "🌍 사회활동가", "📢 마케팅 전문가"],
        "keywords": ["열정", "자유", "창의력", "공감", "에너지"]
    },
    "ISFJ": {
        "title": "💖 ISFJ - 수호자형",
        "description": "배려심이 많고 책임감 있는 성격으로, 조용하지만 헌신적인 태도를 보입니다.",
        "tips": [
            "🛡️ 부드럽고 안정감 있는 상담 환경을 만들어 주세요.",
            "📘 관심과 칭찬을 표현하면 더 마음을 열 수 있어요.",
            "🎗️ 실용적인 조언과 구체적인 안내를 좋아합니다."
        ],
        "example": [
            "**상담교사:** 요즘 힘든 일은 없어요?",
            "**ISFJ 학생:** 그냥 별일은 없는데, 뭔가 계속 실수하는 것 같아서 자존감이 낮아져요.",
            "**상담교사:** 그럴 때도 있죠. 😊 하지만 당신은 항상 성실하고 책임감 있게 행동하고 있어요. 작은 실수보다 당신의 태도가 훨씬 더 소중하답니다. 함께 차근차근 정리해볼까요?"
        ],
        "career": ["👩‍⚕️ 간호사", "📚 교사", "🛠️ 행정 전문가"],
        "keywords": ["책임감", "도움", "신뢰", "배려", "안정감"]
    }
}

# 앱 설정
st.set_page_config(page_title="학생 MBTI 상담 도우미 💬", layout="centered", page_icon="🎓")
st.title("💬 학생 MBTI 상담 도우미")
st.markdown("학생의 MBTI를 선택하면, 해당 성격의 특징과 효과적인 상담 팁, 추천 진로, 대화 예시까지 한눈에 볼 수 있어요! 😊")

# MBTI 선택
mbti = st.selectbox("🔍 학생의 MBTI를 선택해주세요:", list(mbti_info.keys()))

# 정보 표시
if mbti:
    info = mbti_info[mbti]
    st.markdown("---")
    st.subheader(info["title"])
    st.markdown(f"**📌 성격 특징:**\n\n{info['description']}")
    
    st.markdown("**🛠️ 상담 팁:**")
    for tip in info["tips"]:
        st.markdown(f"- {tip}")

    st.markdown("**🎯 추천 진로/직업:**")
    for career in info["career"]:
        st.markdown(f"- {career}")

    st.markdown("**🗣️ 공감 키워드/상담 키워드:**")
    st.markdown("이런 키워드로 공감하면 좋아요:")
    st.markdown(", ".join(f"`{kw}`" for kw in info["keywords"]))

    st.markdown("**💬 상담 대화 예시:**")
    with st.expander("📖 예시 대화 보기"):
        for line in info["example"]:
            st.markdown(line)

    # 다운로드 버튼 - 문자열을 직접 전달
    output_text = f"{info['title']}\n\n📌 성격 특징:\n{info['description']}\n\n"
    output_text += "🛠️ 상담 팁:\n" + "\n".join(info['tips']) + "\n\n"
    output_text += "🎯 추천 진로/직업:\n" + "\n".join(info['career']) + "\n\n"
    output_text += "🗣️ 공감 키워드:\n" + ", ".join(info['keywords']) + "\n\n"
    output_text += "💬 상담 예시:\n" + "\n".join(info['example'])

    st.download_button(
        label="📥 MBTI 상담 정보 다운로드",
        data=output_text,  # <-- 수정된 부분: StringIO 제거
        file_name=f"{mbti}_상담정보.txt",
        mime="text/plain"
    )

    st.markdown("---")
    st.success("📚 학생의 성향을 이해하고 공감하는 상담이 최고의 교육입니다!")

# 피드백 섹션
st.markdown("## 🙋 사용자 의견")
feedback = st.text_area("이 앱을 사용해본 소감이나 추가되면 좋을 기능이 있다면 적어주세요!")
if st.button("📨 의견 보내기"):
    st.success("소중한 의견 감사합니다! 😊")

# 하단 문구
st.markdown("""
<div style='text-align: center; font-size: 16px; margin-top: 30px;'>
    🙌 상담은 학생과의 믿음을 쌓는 과정입니다. <br>
    <b>진심 어린 관심</b>과 <b>MBTI 이해</b>로 보다 깊은 대화를 시작해 보세요!
</div>
""", unsafe_allow_html=True)
