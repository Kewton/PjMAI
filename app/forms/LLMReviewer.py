"""
下記プロンプトを使用して自動生成

~~~~
PythonのStreamlitを使用して簡単アプリを開発しています。
下記ユーザーストーリーを実現するコードを生成して下さい。

# 概要
 - プロンプトテンプレートとLLMモデルとmarkdownファイルを指定してLLMを実行する
 - プロンプトテンプレートはjsonにて（name:str、description:str、value:dict）形式で管理おり、valueにプロンプトテンプレートを登録している
 - プロンプトテンプレートを取得する関数は用意されている
    →getNameList() -> pd.DataFrame:
    →getTemplateByName(_name) -> dict:
 - LLMモデルを取得する関数は用意されている
    →getValueByFormnameAndKeyNameAndValueKey(_formname, _keyname, _valueKey) -> dict:
    下記のように実行することでLLMモデルの一覧を取得することができる
    getValueByFormnameAndKeyNameAndValueKey("common", "system", "llmmodellist")
 - リストに指定したmarkdownファイルのリストを元にmarkdownの中身を取得する関数は用意されている
    →fetch_markdownfiles_and_contents(_file_list: list) -> str:
 - markdownファイルが格納されているディレクトリはシステムで管理する
 - UIは「プロンプトテンプレートの選択」「LLMモデルの選択」「markdownファイルの選択」「プロンプトテンプレートの表示」「LLMの実行結果」で構成されている
 - LLMを実行する関数は用意されている
    →execLlmApi(_selected_model, _messages)
# ユーザーストーリー
 - プロンプトテンプレートとLLMモデルとmarkdownファイルを指定し「実行」ボタンを押下するとLLMを実行してその結果を出力する
~~~~
"""
import streamlit as st
from app.myjsondb.myTemplate import getNameList, getTemplateByName
from app.myjsondb.myStreamlit import getValueByFormnameAndKeyNameAndValueKey
from app.util.markdownopen import fetch_markdownfiles_and_contents, get_markdown_files
from app.util.execLlmApi import execLlmApi


def LLMReviewer():

    # プロンプトテンプレートの選択と表示
    st.header("Select Prompt Template", divider=True)
    templates_df = getNameList()
    template_options = templates_df["name"].tolist()
    selected_template = st.selectbox("Template", template_options)
    template_data = getTemplateByName(selected_template)
    st.write(f"Description: {template_data['description']}")
    st.write(f"system content: {template_data['systemcontent']}")
    st.write(f"user content: {template_data['usercontent']}")

    # LLMモデルの選択
    st.header("Select LLM Model", divider=True)
    llm_models = getValueByFormnameAndKeyNameAndValueKey("common", "system", "llmmodellist")
    selected_model = st.selectbox("Model", llm_models)

    # markdownファイルの選択
    st.header("Select Markdown Files", divider=True)
    markdown_files = get_markdown_files(getValueByFormnameAndKeyNameAndValueKey("common", "system", "workdir"))
    selected_files = st.multiselect("Markdown Files", markdown_files)

    # LLMの実行
    if st.button("Execute"):
        if selected_template and selected_model and selected_files:
            markdown_content = fetch_markdownfiles_and_contents(selected_files)
            _messages = []
            _systemrole_content = template_data["systemcontent"]
            _content = template_data['usercontent'].replace("[$_1]", markdown_content)
            _messages.append({"role": "system", "content": _systemrole_content})
            _messages.append({"role": "user", "content": _content})
            content, role = execLlmApi(selected_model, _messages, "")
            st.success("Execution completed successfully.")
            st.header("LLM Execution Result:", divider=True)
            st.write(content)
        else:
            st.error("Please select all required fields (Template, Model, and Markdown Files).")
