from lxml import html

def HTMLToString(filepath):
    with open(filepath, 'r') as file:
        html_content = file.read()

    parser = html.HTMLParser(remove_blank_text=True)

    if '<html' in html_content and '<head' in html_content:
        tree = html.fromstring(html_content, parser=parser)
        output = html.tostring(tree, method='xml').decode().replace('\n', '')
    else:
        tree = html.fragments_fromstring(html_content, parser=parser)
        output = ''.join(html.tostring(e, method='xml').decode().replace('\n', '') for e in tree)

    return output
