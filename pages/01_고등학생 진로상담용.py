import streamlit as st
import pandas as pd
from xhtml2pdf import pisa
from io import BytesIO
import base64

# Streamlit 설정
st.set_page_config(page_title="MBTI 진로 상담 도우미", layout="centered")

st.title("🧭 MBTI 기반 고등학생 진로 상담 도우미")
st.write("MBTI 유형에 따라 추천 직업과 전공, 활동을 안내해드립니다.")

# 16개 MBTI 유형 데이터
data = {
    'MBTI': [
        'ISTJ', 'ISFJ', 'INFJ', 'INTJ',
        'ISTP', 'ISFP', 'INFP', 'INTP',
        'ESTP', 'ESFP', 'ENFP', 'ENTP',
        'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ'
    ],
    '성격특성': [
        '신중하고 책임감 있음', '성실하고 따뜻함', '이상주의적, 공감능력 높음', '독립적이고 전략적',
        '논리적이며 실용적', '조용하고 친절함', '감성적이고 창의적', '분석적이며 호기심 많음',
        '적응력 뛰어나고 활동적', '사교적이고 유쾌함', '열정적이며 창의적', '재치 있고 논쟁적',
        '조직적이고 지도력 있음', '협조적이며 책임감 있음', '타인에 대한 관심 많음', '목표 지향적이고 주도적'
    ],
    '추천직업': [
        '회계사, 공무원', '간호사, 사회복지사', '상담사, 심리학자', '연구원, 전략기획자',
        '기술자, 파일럿', '디자이너, 플로리스트', '작가, 예술가', '개발자, 과학자',
        '소방관, 스포츠 트레이너', '연예인, 이벤트 플래너', '기자, 콘텐츠 기획자', '벤처 창업가, 마케터',
        '경영자, 군인', '교사, 간호사', '사회복지사, 홍보 담당자', 'CEO, 변호사'
    ],
    '관련전공': [
        '경영학, 행정학', '간호학, 사회복지학', '심리학, 교육학', '공학, 경제학',
        '기계공학, 항공학', '시각디자인, 예술학', '문예창작, 시각예술', '컴퓨터공학, 수학',
        '체육학, 응급구조학', '공연예술학, 관광학', '신문방송학, 광고홍보학', '경영학, 창업학',
        '경영학, 법학', '교육학, 사회복지학', '언론정보학, 커뮤니케이션', '법학, 정치외교학'
    ],
    '추천활동': [
        '모의고사 분석, 행정체험', '병원 자원봉사, 독서토론', '멘토링, 심리상담 체험', '과학탐구, 수학경시대회',
        '로봇 제작, 드론 대회', '일러스트 그리기, 꽃꽂이', '시쓰기, 영화 감상', '코딩, 수학 문제 풀이',
        '체육대회, 구조 훈련', '공연 참가, 축제 기획', 'UCC 공모전, 스토리텔링', '창업 캠프, 아이디어톤',
        '리더십 캠프, 군사체험', '교육봉사, 협업 활동', '토론, 사회 참여 프로그램', '모의 법정, 토론대회'
    ]
}

# 데이터프레임 생성
df = pd.DataFrame(data)

# 사용자 MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", df['MBTI'])

if selected_mbti:
    result = df[df['MBTI'] == selected_mbti].iloc[0]
    
    st.subheader("📌 MBTI 진로 정보")
    st.markdown(f"**성격 특성:** {result['성격특성']}")
    st.markdown(f"**추천 직업:** {result['추천직업']}")
    st.markdown(f"**관련 전공:** {result['관련전공']}")
    st.markdown(f"**추천 활동:** {result['추천활동']}")

    # HTML 텍스트 생성
    html = f"""
    <html>
    <head><meta charset="utf-8"></head>
    <body>
        <h2>MBTI 진로 상담 결과</h2>
        <p><strong>MBTI 유형:</strong> {selected_mbti}</p>
        <p><strong>성격 특성:</strong> {result['성격특성']}</p>
        <p><strong>추천 직업:</strong> {result['추천직업']}</p>
        <p><strong>관련 전공:</strong> {result['관련전공']}</p>
        <p><strong>추천 활동:</strong> {result['추천활동']}</p>
    </body>
    </html>
    """

    # PDF 생성 함수
    def convert_html_to_pdf(source_html):
        pdf_buffer = BytesIO()
        pisa_status = pisa.CreatePDF(source_html, dest=pdf_buffer, encoding='utf-8')
        if not pisa_status.err:
            return pdf_buffer.getvalue()
        return None

    pdf = convert_html_to_pdf(html)

    if pdf:
        b64 = base64.b64encode(pdf).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="mbti_result.pdf">📄 결과 PDF 다운로드</a>'
        st.markdown(href, unsafe_allow_html=True)

