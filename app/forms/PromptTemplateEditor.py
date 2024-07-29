"""
下記プロンプトを使用して自動生成

~~~~
PythonのStreamlitを使用して簡単アプリを開発しています。
下記ユーザーストーリーを実現するコードを生成して下さい。

# 概要
 - LLMへのプロンプトテンプレートを管理する
 - テンプレートはjsonにて（name:str、description:str、value:dict）形式で管理している。valueにプロンプトテンプレートを登録
 - 登録/更新・削除・取得する関数は用意されている
    - 登録/更新
　　→upsertValueBynameAnddescription(_name, _description, _value) -> bool:
    - 削除
　　→deletePjByName(_name) -> bool
　 - 取得
　　→getTemplateByName(_name) -> dict:
　　→getNameList() -> pd.DataFrame:
 - UIは「st.columns」を使用して2列に分けており、左側（１列目）にはテンプレート名と説明の一覧を表示し、右側（２列目）で登録済みのテンプレートを編集したり新規登録したりできる

# ユーザーストーリー
 - 右側のテンプレート編集エリアにて、テンプレート名・説明・テンプレートを入力し、「更新」ボタンをクリックすることでDBに新規登録することができる。
 - 登録済みのテンプレートが存在しない場合、左側には何も表示しない
 - 登録済みのテンプレートが存在する場合、左側にテンプレートと説明の一覧が表示されており、選択することで右側の編集エリアに初期表示することができる。なお、テンプレートの編集は可能であり「更新」ボタンをクリックすることでDBに登録することができる。また、「削除」ボタンをクリックすることでDBから削除することができる。
 - 「更新」「削除」ボタン押下後、左側の説明一覧が自動で最新化される
~~~~
"""
import streamlit as st
from app.myjsondb.myTemplate import upsertValueBynameAnddescription, deletePjByName, getTemplateByName, getNameList


def PromptTemplateEditor():
    # 2列に分ける
    col1, col2 = st.columns(2)

    with col1:
        st.header("Templates List")
        templates_df = getNameList()
        
        if not templates_df.empty:
            selected_template = st.selectbox("Select a template to edit", templates_df["name"])
        else:
            selected_template = None
            st.write("No templates available.")

    with col2:
        st.header("Template Editor")
        
        if selected_template:
            template_data = getTemplateByName(selected_template)
            name = st.text_input("Template Name", value=template_data["name"])
            description = st.text_input("Description", value=template_data["description"])
            systemcontent = st.text_area("Template Value(system role)", value=str(template_data["systemcontent"]))
            usercontent = st.text_area("Template Value(user content) * Write [$_1] in the markdown file insertion point", value=str(template_data["usercontent"]))
        else:
            name = st.text_input("Template Name")
            description = st.text_input("Description")
            systemcontent = st.text_area("Template Value(system content)")
            usercontent = st.text_area("Template Value(user content)")

        if st.button("Update"):
            if upsertValueBynameAnddescription(name, description, systemcontent, usercontent):
                st.success("Template updated successfully.")
            else:
                st.error("Failed to update the template.")
            
            # 左側のテンプレートリストを最新化
            templates_df = getNameList()

        if selected_template and st.button("Delete"):
            if deletePjByName(name):
                st.success("Template deleted successfully.")
                selected_template = None
            else:
                st.error("Failed to delete the template.")
            
            # 左側のテンプレートリストを最新化
            templates_df = getNameList()

    # 左側に最新のテンプレートリストを表示
    with col1:
        if not templates_df.empty:
            st.write(templates_df)
        else:
            st.write("No templates available.")
