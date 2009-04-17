import re, os
from datetime import datetime

URL = 'http://diku.dk/hjemmesider/studerende/zerrez/'
RE_LINK = re.compile(r'<a\s+href="(\?[^"]+)"')

print 'updating sitemap.html ..'


def to_file(link):
    return 'sections/%s.html' % link[1:]

def modified(link):
    return datetime.fromtimestamp(os.stat(to_file(link)).st_mtime).isoformat()


links = []
html  = file('index.html').read()
for link in RE_LINK.findall(html):
    print 'adding:', link
    links.append((URL + link, modified(link)))

file('sitemap.txt','w').write('\n'.join(
    [ '%s\tlastmod=%s' % link for link in links]))

print 'links:', len(links)
