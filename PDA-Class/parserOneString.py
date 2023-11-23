from lxml import html

def HTMLToString(filepath):
    with open(filepath, 'r') as file:
        html_content = file.read()

    parser = html.HTMLParser(remove_blank_text=True)
    tree = html.fragments_fromstring(html_content, parser=parser)

    output = ''.join(html.tostring(e, method='html').decode().replace('\n', '') for e in tree)

    return output
