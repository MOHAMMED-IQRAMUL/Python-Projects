from bs4 import BeautifulSoup

html_doc = ''

with open('readed.html', 'r', encoding="utf-8") as f:
    html_doc = f.read()
    
    
soup = BeautifulSoup(html_doc, 'html.parser')

with open('beautifull.html', 'w', encoding="utf-8") as f:
    f.write(soup.prettify())
    
information = {}
information['title'] = soup.title
information['title.name'] = soup.title.name
information['title.string'] = soup.title.string

print(information)
