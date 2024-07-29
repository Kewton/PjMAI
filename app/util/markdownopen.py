import os


def escape(_instr):
    return _instr.replace('"', '\\"').replace('`', '\\`')


def get_markdown_files(directory):
    """
    指定したディレクトリ内の.mdファイルの一覧を取得する
    :param directory: str
    :return: list
    """
    markdown_files = [file for file in os.listdir(directory) if file.endswith('.md')]
    return markdown_files


def fetch_markdownfiles_and_contents(_file_list: list) -> str:
    # ファイルを開き、内容を読み込む
    all_files = []
    outstr = ""
    print(_file_list)
    for file_path in _file_list:
        try:
            # 拡張子を取得
            print(file_path)
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    all_files.append(f"// ---------------------")
                    all_files.append(f"// start")
                    all_files.append(f"// filename:{file_path} ")
                    all_files.append(f"// ---------------------")
                    all_files.append(content)
                    all_files.append(f"// ---------------------")
                    all_files.append(f"// end")
                    all_files.append(f"// ---------------------")
                    all_files.append("")
        except (UnicodeDecodeError, IOError):
            print(f"Error reading {file_path}. It may not be a text file or might have encoding issues.")
    
    if len(all_files) > 0:
        outstr = '\n'.join(str(elem) for elem in all_files)
    else:
        outstr = "指定のファイルは存在しません。"
    return outstr
