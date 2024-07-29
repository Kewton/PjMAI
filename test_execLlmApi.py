from app.util.execLlmApi import execLlmApi


if __name__ == '__main__':
    selected_model = "gpt-4o-mini"
    _messages = []
    _systemrole_content = """
あなたはスーパレビュワーです
    """
    _content = """
「うんこ」をかっこよく表現して下さい。
    """
    _messages.append({"role": "system", "content": _systemrole_content})
    _messages.append({"role": "user", "content": _content})
    encoded_file = None
    content, role = execLlmApi(selected_model, _messages, encoded_file)
    print(content)
    print("-------")
    print(role)