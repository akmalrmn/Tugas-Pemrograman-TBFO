from bs4 import BeautifulSoup

html = open('abc.html', 'r').read()

soup = BeautifulSoup(html, 'html.parser')

for tag in soup.find_all():
    if tag.contents:
        for content in tag.contents:
            if isinstance(content, str):
                content.replace_with('')

output = str(soup)

print(output)
