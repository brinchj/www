import re, os, glob
from datetime import datetime

def find_pages(dirs):
    if not dirs: return []
    pages = []
    for d in dirs:
        pages += filter(lambda x: '/_' not in x, glob.glob('%s/*.html' % d))
        pages += find_pages([ '%s/%s' % (d, p) for p in os.listdir(d) if os.path.isdir(d+'/'+p)])
    return pages

pages = ['footer.html'] + find_pages(['./sections'])


URL = 'http://diku.dk/hjemmesider/studerende/zerrez/'
RE_LINK = re.compile(r'<a\s+href="((http://[^z"]+/zerrez/[^"]+)|(http://zerrez.s3.amazonaws.com/[^"]+))"')

print 'updating sitemap.html ..'


def to_file(link):
    return 'sections/%s.html' % link[1:]

def modified(link):
    lastmod = None
    if 'zerrez/sections' in link:
        lastmod = datetime.fromtimestamp(os.stat(link[link.index('zerrez/sections/')+7:]).st_mtime).isoformat()
    return lastmod and 'lastmod=%s' % lastmod or ''


links = set()
for p in pages:
    html  = file(p).read()
    for link,_,_ in RE_LINK.findall(html):
        print 'adding:', link
        links.add((link, modified(link)))

file('sitemap.txt','w').write('\n'.join(
    [ '%s %s' % link for link in links]))

print 'links:', len(links)
