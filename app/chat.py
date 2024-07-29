import streamlit as st
from app.forms.PromptTemplateEditor import PromptTemplateEditor
from app.forms.LLMReviewer import LLMReviewer

MAIN_TITLE = "Project management efficiency tools"


def chat():
    st.set_page_config(layout="wide")
    st.title(MAIN_TITLE)
    tab1, tab2, tab3 = st.tabs([
        "Prompt Template Editor",
        "LLM Reviewer",
        "Search Project Info"
    ])

    with tab1:
        # テンプレート名
        # 表示優先度
        # テンプレートの説明
        # プロンプト
        PromptTemplateEditor()

    with tab2:
        LLMReviewer()

    with tab3:
        st.header("工事中", divider=True)
