from bs4 import BeautifulSoup

html = open('abc.html', 'r').read()

soup = BeautifulSoup(html, 'html.parser')
output = str(soup)
output = ''.join(output.split())

print(output)
