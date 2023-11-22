from bs4 import BeautifulSoup

def HTMLToString(file_path):
    html = open(file_path, 'r').read()

    soup = BeautifulSoup(html, 'html.parser')

    output = str(soup).replace('\n', '')

    return output