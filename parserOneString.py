from bs4 import BeautifulSoup

html = open('abc.html', 'r').read()

soup = BeautifulSoup(html, 'html.parser')

for tag in soup.find_all():
    if tag.string:
        tag.string = ''

output = str(soup)
output = ''.join(output.split())

print(output)
