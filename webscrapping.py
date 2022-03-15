import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://en.wikipedia.org/wiki/Python_(programming_language)').read()

soup = bs.BeautifulSoup(source,'lxml')

# title of the page
print(soup.title)

# get attributes:
print(soup.title.name)

# get values:
print(soup.title.string)

# beginning navigation:
print(soup.title.parent.name)

print(soup.find_all('p'))

for paragraph in soup.find_all('p'):
    print(paragraph.string)
    print(str(paragraph.text))

for url in soup.find_all('a'):
    print(url.get('href'))

body = soup.body
for paragraph in body.find_all('p'):
    print(paragraph.text)

#scrapping specifically with a table example
table = soup.table

#find the table rows within the table
table_rows = table.find_all('tr')

# iterate through the rows,find the td tags, and then print out each of the table data tags:
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)

for item in soup.find_all('img'):
    print(item['src'])
