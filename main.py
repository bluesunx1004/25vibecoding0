import streamlit as st
import plotly.graph_objects as go
from xhtml2pdf import pisa
import tempfile
import os

# 🎨 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천기 💼✨", page_icon="🎯", layout="centered")

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
    # 다른 유형도 필요 시 추가
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

# 사용자 입력
st.markdown("<h1 style='text-align: center; color: #6a1b9a;'>🌟 MBTI 기반 진로 추천기 💼✨</h1>", unsafe_allow_html=True)
method = st.radio("MBTI를 어떻게 확인할까요?", ["직접 선택하기", "간단 테스트로 확인하기"])

user_mbti = ""
if method == "
