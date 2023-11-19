from bs4 import BeautifulSoup

def HTMLToString(file_path):
    html = open(file_path, 'r').read()

    soup = BeautifulSoup(html, 'html.parser')

    for tag in soup.find_all():
        if tag.contents:
            for content in tag.contents:
                if isinstance(content, str):
                    content.replace_with('')

    output = str(soup)
    output = ''.join(output.split())

    return output
