import streamlit as st
import plotly.graph_objects as go
import pdfkit
import base64
import tempfile
import os
from xhtml2pdf import pisa

def convert_html_to_pdf(source_html, output_filename):
    with open(output_filename, "w+b") as result_file:
        pisa_status = pisa.CreatePDF(source_html, dest=result_file)
    return pisa_status.err
# 🎨 페이지 설정
st.set_page_config(
    page_title="MBTI 진로 추천기 💼✨",
    page_icon="🎯",
    layout="centered"
)

# 📋 직업 데이터 (설명 & 링크 포함)
mbti_jobs = {
    "INTJ": [
        {"title": "전략기획가 📊", "desc": "조직의 미래 전략을 수립하는 전문가입니다.", "link": "https://www.career.go.kr"},
        {"title": "데이터 과학자 📈", "desc": "데이터 분석으로 인사이트를 도출합니다.", "link": "https://www.work.go.kr"},
        {"title": "시스템 엔지니어 🖥️", "desc": "IT 인프라를 설계하고 운영합니다.", "link": "https://www.career.go.kr"}
    ],
    "ENFP": [
        {"title": "배우 🎭", "desc": "감정을 표현하고 캐릭터를 연기합니다.", "link": "https://www.career.go.kr"},
        {"title": "콘텐츠 크리에이터 📱", "desc": "영상 및 콘텐츠를 제작하고 전달합니다.", "link": "https://www.work.go.kr"},
        {"title": "창작자 🎥", "desc": "창의적 아이디어를 기반으로 다양한 작품을 만듭니다.", "link": "https://www.career.go.kr"}
    ],
    # 필요에 따라 다른 MBTI도 추가
}

# MBTI 성향 시각화용
def get_mbti_traits(mbti):
    return {
        "사교성": 80 if mbti[0] == "E" else 20,
        "직관력": 80 if mbti[1] == "N" else 20,
        "감성적 판단": 80 if mbti[2] == "F" else 20,
        "계획성": 80 if mbti[3] == "J" else 20
    }

# 사용자 입력
st.markdown("<h1 style='text-align: center; color: #6a1b9a;'>🌟 MBTI 기반 진로 추천기 💼✨</h1>", unsafe_allow_html=True)
method = st.radio("MBTI를 어떻게 확인할까요?", ["직접 선택하기", "간단 테스트로 확인하기"])

user_mbti = ""
if method == "직접 선택하기":
    mbti_list = sorted(mbti_jobs.keys())
    selected_mbti = st.selectbox("당신의 MBTI를 선택하세요! 👇", mbti_list)
    user_mbti = selected_mbti
else:
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
    jobs = mbti_jobs.get(user_mbti, [])

    html_content = f"<h2>{user_mbti} 추천 직업</h2><ul>"
    for job in jobs:
        st.markdown(f"#### 🔹 {job['title']}")
        st.markdown(f"💬 {job['desc']}")
        st.markdown(f"[자세히 보기]({job['link']})")
        html_content += f"<li><strong>{job['title']}</strong>: {job['desc']} (<a href='{job['link']}'>링크</a>)</li>"
    html_content += "</ul>"

    st.markdown("💡 *추천은 참고용입니다. 진로는 여러분의 열정과 선택이 가장 중요해요!*")

    # Radar Chart
    st.markdown("### 📊 MBTI 성향 레이더 차트")
    traits = get_mbti_traits(user_mbti)
    labels = list(traits.keys())
    values = list(traits.values())
    fig = go.Figure(data=go.Scatterpolar(
        r=values + [values[0]],
        theta=labels + [labels[0]],
        fill='toself',
        name='MBTI 성향'
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100])
        ),
        showlegend=False
    )
    st.plotly_chart(fig)

    # HTML에 시각화도 추가
    html_content += "<h3>MBTI 성향 점수</h3><ul>"
    for k, v in traits.items():
        html_content += f"<li>{k}: {v}</li>"
    html_content += "</ul>"

    # PDF 저장
    if st.button("📄 결과를 PDF로 다운로드"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmpfile:
            pdfkit.from_string(html_content, tmpfile.name)
            with open(tmpfile.name, "rb") as f:
                pdf = f.read()
            b64 = base64.b64encode(pdf).decode()
            href = f'<a href="data:application/octet-stream;base64,{b64}" download="{user_mbti}_진로추천.pdf">📥 PDF 다운로드</a>'
            st.markdown(href, unsafe_allow_html=True)
            os.unlink(tmpfile.name)

# 푸터
st.markdown("---")
st.markdown("<h5 style='text-align: center;'>Made with ❤️ by YourName</h5>", unsafe_allow_html=True)
