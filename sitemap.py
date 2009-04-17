import re

URL = 'http://diku.dk/hjemmesider/studerende/zerrez/'
RE_LINK = re.compile(r'<a\s+href="(\?[^"]+)"')

print 'updating sitemap.html ..'

links = []
html  = file('index.html').read()
for link in RE_LINK.findall(html):
    print 'adding:', link
    links.append(URL + link)

file('sitemap.lst','w').write('\n'.join(links))
print 'links:', len(links)
