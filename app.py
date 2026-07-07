import pathlib

import streamlit as st
import streamlit.components.v1 as components

# ── 기본 설정 ────────────────────────────────────────────────
BASE_DIR = pathlib.Path(__file__).parent
HTML_FILE = BASE_DIR / "trendfit.html"
FAVICON_FILE = BASE_DIR / "favicon.png"

st.set_page_config(
    page_title="트렌드핏 | TrendFit",
    page_icon=str(FAVICON_FILE) if FAVICON_FILE.exists() else "✨",
    layout="centered",
)

# Streamlit 기본 여백/헤더를 최대한 제거해서 뉴스레터 디자인이
# 그대로 보이도록 함
st.markdown(
    """
    <style>
        #MainMenu, header, footer {visibility: hidden;}
        .block-container {padding: 0 !important; max-width: 100% !important;}
        iframe {border: none;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ── trendfit.html 그대로 렌더링 ──────────────────────────────
if not HTML_FILE.exists():
    st.error(f"'{HTML_FILE.name}' 파일을 찾을 수 없습니다. app.py와 같은 폴더에 두었는지 확인해주세요.")
else:
    html_content = HTML_FILE.read_text(encoding="utf-8")
    # 세로 스크롤이 가능하도록 넉넉한 높이로 렌더링
    components.html(html_content, height=2400, scrolling=True)
