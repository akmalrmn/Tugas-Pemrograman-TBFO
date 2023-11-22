from bs4 import BeautifulSoup

html = open('a.html', 'r').read()

soup = BeautifulSoup(html, 'html.parser')

output = str(soup).replace('\n', '')

print(output)