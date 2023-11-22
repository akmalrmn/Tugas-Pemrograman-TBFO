import re
from lxml import html

def HTMLToString(filepath):
    with open(filepath, 'r') as file:
        html_content = file.read()

    tree = html.fromstring(html_content)

    output = html.tostring(tree, method='html').decode().replace('\n', '')

    output = re.sub(r'>\s+<', '><', output)

    print(output)

HTMLToString('a.html')