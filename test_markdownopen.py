from app.util.markdownopen import fetch_markdownfiles_and_contents


if __name__ == '__main__':
    out = fetch_markdownfiles_and_contents(["./README.md", "./README_2.md"])
    print(out)