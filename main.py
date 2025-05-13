import streamlit as st
import plotly.graph_objects as go
from xhtml2pdf import pisa
import tempfile
import os

# 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천기", page_icon="🎯", layout="centered")

# MBTI 직업 데이터 (16유형)
mbti_jobs = {
    "INTJ": [{"title": "전략기획가 📊", "desc": "조직의 미래 전략을 수립하는 전문가", "link": "https://www.career.go.kr"}],
    "INTP": [{"title": "연구원 🔬", "desc": "논리적 탐구와 분석을 주로 수행", "link": "https://www.work.go.kr"}],
    "ENTJ": [{"title": "CEO 🧑‍💼", "desc": "조직을 이끄는 리더", "link": "https://www.career.go.kr"}],
    "ENTP": [{"title": "벤처 사업가 🚀", "desc": "창의적 아이디어로 새로운 사업 추진", "link": "https://www.work.go.kr"}],
    "INFJ": [{"title": "상담가 🧘", "desc": "사람들의 내면을 이해하고 돕는 전문가", "link": "https://www.career.go.kr"}],
    "INFP": [{"title": "일러스트레이터 🖌️", "desc": "감성적인 창작물을 그려내는 예술가", "link": "https://www.work.go.kr"}],
    "ENFJ": [{"title": "교육자 👩‍🏫", "desc": "지식과 가치를 전달하는 역할", "link": "https://www.career.go.kr"}],
    "ENFP": [{"title": "콘텐츠 크리에이터 📱", "desc": "창의적 콘텐츠로 사람들과 소통", "link": "https://www.work.go.kr"}],
    "ISTJ": [{"title": "회계사 🧾", "desc": "정확한 수치와 자료로 재정관리", "link": "https://www.career.go.kr"}],
    "ISFJ": [{"title": "간호사 💉", "desc": "환자를 돌보는 헌신적인 직업", "link": "https://www.work.go.kr"}],
    "ESTJ": [{"title": "경영 관리자 📋", "desc": "조직의 효율을 극대화하는 리더", "link": "https://www.career.go.kr"}],
    "ESFJ": [{"title": "이벤트 플래너 🎉", "desc": "사람 중심의 행사 기획자", "link": "https://www.work.go.kr"}],
    "ISTP": [{"title": "파일럿 ✈️", "desc": "기계 조작에 능한 실용적 전문가", "link": "https://www.career.go.kr"}],
    "ISFP": [{"title": "플로리스트 🌷", "desc": "자연과 예술을 조화시키는 직업", "link": "https://www.work.go.kr"}],
    "ESTP": [{"title": "스턴트맨 🤸", "desc": "도전을 즐기는 활동적 전문가", "link": "https://www.career.go.kr"}],
    "ESFP": [{"title": "가수 🎤", "desc": "무대에서 자신을 표현하는 예능인", "link": "https://www.work.go.kr"}]
}

def get_mbti_traits(mbti):
    return {
        "사교성": 80 if mbti[0] == "E" else 20,
        "직관력": 80 if mbti[1] == "N" else 20,
        "감성적 판단": 80 if mbti[2] == "F" else 20,
        "계획성": 80 if mbti[3] == "J" else 20
    }

def convert_html_to_pdf(source_html):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmpfile:
        pisa_status = pisa.CreatePDF(source_html, dest=tmpfile)
        tmpfile.flush()
        if pisa_status.err:
            return None
        else:
            return tmpfile.name

# UI
st.title("🌟 MBTI 진로 추천기 💼✨")
method = st.radio("MBTI를 어떻게 확인할까요?", ["직접 선택하기", "간단 테스트로 확인하기"])

user_mbti = ""
if method == "직접 선택하기":
    user_mbti = st.selectbox("당신의 MBTI를 선택하세요!", list(mbti_jobs.keys()))
else:
    q1 = st.radio("1️⃣ 사람들과 함께 있을 때 에너지가 솟는다", ["예", "아니오"])
    q2 = st.radio("2️⃣ 현실적인 정보보다 직관적인 아이디어를 선호한다", ["예", "아니오"])
    q3 = st.radio("3️⃣ 결정할 때 논리보다는 감정을 더 고려한다", ["예", "아니오"])
    q4 = st.radio("4️⃣ 계획적으로 행동하는 걸 좋아한다", ["예", "아니오"])
    if st.button("📌 MBTI 추정하기"):
        user_mbti = "".join([
            "E" if q1 == "예" else "I",
            "N" if q2 == "예" else "S",
            "F" if q3 == "예" else "T",
            "J" if q4 == "예" else "P"
        ])
        st.success(f"당신의 추정 MBTI는 **{user_mbti}**입니다!")

if user_mbti:
    st.subheader(f"🧭 {user_mbti} 추천 직업")
    jobs = mbti_jobs.get(user_mbti, [])
    
    html_content = f"""
    <html><head>
    <meta charset="UTF-8">
    <style>
    @font-face {{
        font-family: "NanumGothic";
        src: url("https://cdn.jsdelivr.net/gh/webfontworld/NanumGothic/NanumGothic-Regular.ttf");
    }}
    body {{ font-family: "NanumGothic"; }}
    </style></head><body>
    <h2>{user_mbti} 추천 직업</h2><ul>
    """

    for job in jobs:
        st.markdown(f"**🔹 {job['title']}**\n\n- {job['desc']}\n\n[자세히 보기]({job['link']})")
        html_content += f"<li><b>{job['title']}</b>: {job['desc']} (<a href='{job['link']}'>링크</a>)</li>"

    html_content += "</ul><h3>MBTI 성향</h3><ul>"
    traits = get_mbti_traits(user_mbti)
    for k, v in traits.items():
        html_content += f"<li>{k}: {v}</li>"
    html_content += "</ul></body></html>"

    # Radar Chart
    st.markdown("### 📊 성향 시각화")
    fig = go.Figure(data=go.Scatterpolar(
        r=list(traits.values()) + [list(traits.values())[0]],
        theta=list(traits.keys()) + [list(traits.keys())[0]],
        fill='toself'
    ))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=False)
    st.plotly_chart(fig)

    # PDF 변환
    pdf_path = convert_html_to_pdf(html_content)
    if pdf_path:
        with open(pdf_path, "rb") as f:
            st.download_button("📄 결과 PDF 다운로드", f.read(), file_name=f"{user_mbti}_진로추천.pdf", mime="application/pdf")
        os.remove(pdf_path)
    else:
        st.error("PDF 생성에 실패했습니다.")

# 푸터
st.markdown("---")
st.markdown("<h5 style='text-align: center;'>Made with ❤️ by YourName</h5>", unsafe_allow_html=True)
