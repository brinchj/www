import re, os
from datetime import datetime

URL = 'http://diku.dk/hjemmesider/studerende/zerrez/'
RE_LINK = re.compile(r'<a\s+href="http://[^z]+/zerrez/([^"]+)"')

print 'updating sitemap.html ..'


def to_file(link):
    return 'sections/%s.html' % link[1:]

def modified(link):
    return datetime.fromtimestamp(os.stat(link).st_mtime).isoformat()


links = []
html  = file('footer.html').read()
for link in RE_LINK.findall(html):
    print 'adding:', link
    links.append((URL + link, modified(link)))

file('sitemap.txt','w').write('\n'.join(
    [ '%s\tlastmod=%s' % link for link in links]))

print 'links:', len(links)
