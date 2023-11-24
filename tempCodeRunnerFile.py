soup = BeautifulSoup(html, 'html.parser')

for tag in soup.find_all():
    for attr, value in list(tag.attrs.items()):
        if attr == '' and len(value) == 1 and value[0] == '':
            tag.attrs.pop(attr)

output = re.sub(r'(\s+"")=\s+', r'\1 ', html)
output = ''.join(output.splitlines())  # Join lines into a single string

print(output)