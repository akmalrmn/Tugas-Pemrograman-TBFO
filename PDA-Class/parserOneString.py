from lxml import html

def HTMLToString1(filepath):
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

def HTMLToString2(file_path):
    result = ""
    inTag = False

    with open(file_path, 'r') as file:
        content = file.read()

        for char in content:
            if char == '<':
                result += char
                inTag = True
            elif char == '>':
                result += char
                inTag = False
            elif not inTag and char in [' ', '\t', '\n']:
                continue
            else:
                result += char

    return result
