#!/usr/bin/env python3
"""Check a built site for broken local links, migration errors, and missing content."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json, re, sys, struct
root=Path(sys.argv[1] if len(sys.argv)>1 else '_site').resolve()
production='--production' in sys.argv
errors=[]
class Page(HTMLParser):
 def __init__(self, text):
  super().__init__();self.ids=[];self.links=[];self.images=[];self.h1=0;self.canonical=[];self.refresh=[];self.scripts=[];self.citations=[];self.feed(text)
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if 'id' in d:self.ids.append(d['id'])
  if tag=='h1':self.h1+=1
  if d.get('class')=='publication-citation':self.citations.append((d.get('data-project'),d.get('data-status')))
  if tag=='img':self.images.append(d)
  if tag=='script':self.scripts.append(d)
  for key in ['href','src']:
   if key in d:self.links.append(d[key])
  if tag=='link' and d.get('rel')=='canonical':self.canonical.append(d.get('href',''))
  if tag=='meta' and d.get('http-equiv','').lower()=='refresh':self.refresh.append(d.get('content',''))
def check(ok,message):
 if not ok:errors.append(message)
html={p:Page(p.read_text()) for p in root.rglob('*.html')}
check(bool(html),'No built HTML found')
checked_links=0
for file,page in html.items():
 text=file.read_text();rel=file.relative_to(root)
 check(len(page.ids)==len(set(page.ids)),f'{rel}: duplicate IDs')
 check(page.h1==1,f'{rel}: expected exactly one h1')
 if not page.refresh:
  check('name="description"' in text,f'{rel}: missing description')
  check(len(page.canonical)==1,f'{rel}: missing canonical URL')
  if production:check(page.canonical[0].startswith('https://asadullahbhuiyan.github.io/'),f'{rel}: wrong production canonical')
 for script in page.scripts:check(script.get('type')=='application/ld+json' or (page.refresh and not script.get('src')),f'{rel}: unexpected executable script')
 for image in page.images:check(bool(image.get('alt')),f'{rel}: missing image alternative text')
 for link in page.links:
  url=urlsplit(link)
  if url.scheme in ['mailto','tel'] or url.netloc not in ['', 'asadullahbhuiyan.github.io','127.0.0.1:4000','localhost:4000']:continue
  target=(root/unquote(url.path).lstrip('/')) if url.path.startswith('/') else (file.parent/unquote(url.path)) if url.path else file
  if target.is_dir():target=target/'index.html'
  if not target.exists() and not target.suffix:target=target/'index.html'
  check(target.exists(),f'{rel}: missing target {link}')
  if url.fragment and target in html:check(unquote(url.fragment) in html[target].ids,f'{rel}: missing anchor {link}')
  checked_links+=1
 for stale in ['SITE UNDER CONSTRUCTION','GitHub University','Paper Title Number','hk684@cornell.edu','QioxoEgAAAAJ','CV_HyejinKim','naca-overview']:
  check(stale not in text,f'{rel}: stale content {stale}')
for img in root.rglob('*.png'):
 with img.open('rb') as f:header=f.read(24)
 check(header[:8]==b'\x89PNG\r\n\x1a\n',f'{img}: corrupt PNG')
for path in ['index.html','research/index.html','publications/index.html','talks/index.html','about/index.html','cv/index.html','404.html','sitemap.xml','assets/files/Asadullah_Bhuiyan_CV.pdf','images/Headshot.jpg']:
 check((root/path).exists(),f'Missing required route or asset {path}')
research=(root/'research/index.html').read_text();talks=(root/'talks/index.html').read_text();home=(root/'index.html').read_text()
pub=research
expected_projects=['learning','quantum','ongoing','singular-potentials','periodically-driven','landau-levels','microtubules']
citations=html[root/'research/index.html'].citations
check([project for project,status in citations]==expected_projects,'Expected each publication exactly once, in project order')
check(sum(status=='journal-articles' for project,status in citations)==5,'Expected five journal articles')
check(sum(status=='preprints' for project,status in citations)==1,'Expected one preprint')
check(sum(status=='in-preparation' for project,status in citations)==1,'Expected one manuscript in preparation')
check('Selected research' not in home and '<figure' not in home,'Homepage must not repeat research projects')
check(home.count('class="hero-note hero-intro"')==3,'Expected three homepage bio paragraphs')
check('class="eyebrow"' not in home,'Homepage should not repeat affiliation eyebrow')
check('aria-current="page">About</a>' in home,'About must be active on homepage')
check('class="section-nav"' not in research and 'class="lead-copy"' not in research,'Research must not repeat bio or section navigation')
for text in [home,research,talks]:
 nav=text.split('id="site-nav"',1)[1].split('</nav>',1)[0]
 labels=re.findall(r'<li><a[^>]*>([^<]+)',nav)
 check(labels==['Research','Talks','CV','About'],'Wrong primary navigation')
for anchor in ['learning','quantum','ongoing','bosonic','earlier']:
 check(anchor in html[root/'research/index.html'].ids,f'Missing research anchor {anchor}')
# Source data are authoritative for publication details; no duplicate citation copies.
from html import unescape
groups=json.loads((Path(__file__).resolve().parent.parent/'_data/publications.json').read_text())
clean=lambda value:' '.join(unescape(re.sub('<[^>]+>','',value)).split())
research_text=clean(research)
for group in groups:
 for paper in group['papers']:
  for field in ['title','authors','venue']:
   check(clean(paper[field]) in research_text,f'Missing citation {field}: {paper["project"]}')
  for link in ([paper['url']] if paper.get('url') else [])+[link['url'] for link in paper.get('links',[])]:
   check(link in html[root/'research/index.html'].links,f'Missing paper/code link {link}')
for phrase in ['Learning from almost nothing','Free-Fermion Dynamics','pseudoharmonic oscillator','Schrödinger Cat States','Landau Levels','Microtubule Ensembles','Chiral critical state ensembles']:
 check(phrase in pub,f'Missing publication: {phrase}')
check(research.count('<figure')==4,'Expected four flagship figures')
check(research.count('<h3>My contributions</h3>')==2,'Expected contributions for both flagship projects')
for date in ['2025-11-11','2025-03-19','2023-03-06']:check(date in talks,f'Missing talk {date}')
for alias,target in {'year-archive':'/research/','talkmap.html':'/talks/','teaching':'/cv/','about':'/','publications':'/research/','resume':'/cv/','cv-json':'/cv/'}.items():
 p=root/alias
 if p.is_dir():p=p/'index.html'
 check(p in html and bool(html[p].refresh),f'Missing redirect {alias}')
 if p in html:check(any(urlsplit(x.split('url=',1)[-1]).path==target for x in html[p].refresh),f'Wrong redirect {alias}')
check(len(list(root.rglob('*.pdf')))==1,'Unexpected PDF beyond approved CV')
for private in ['docs','scripts','Documents','tmp','.git','README.md','Gemfile','Gemfile.lock','LICENSE']:
 check(not (root/private).exists(),f'Internal file exposed in build: {private}')
print(json.dumps({'html_pages':len(html),'local_links_checked':checked_links,'publication_entries':7,'research_figures':4,'errors':errors},indent=2))
sys.exit(bool(errors))
