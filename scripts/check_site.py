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
home=(root/'index.html').read_text()
page=html[root/'index.html']
check(home.count('class="hero-note hero-intro"')==3,'Expected three homepage bio paragraphs')
check('class="eyebrow"' not in home,'Homepage should not repeat affiliation eyebrow')
for file,parsed in html.items():
 if parsed.refresh:continue
 text=file.read_text()
 nav=text.split('id="site-nav"',1)[1].split('</nav>',1)[0]
 labels=re.findall(r'<li><a[^>]*>([^<]+)',nav)
 check(labels==['Publications','Talks','Research','CV'],'Wrong primary navigation')
 for target in ['/#publications','/#talks','/#research']:
  check(target in nav,f'Missing navigation target {target}')
check('aria-current="page"' not in home,'Section navigation must not mark an entire page active')
for anchor in ['publications','talks','research','learning','quantum']:
 check(anchor in page.ids,f'Missing homepage anchor {anchor}')
check(home.index('id="publications"')<home.index('id="talks"')<home.index('id="research"'),'Wrong homepage section order')
for stale in ['My contributions','publication-citation','id="ongoing"','id="bosonic"','id="earlier"','id="hubbard-holstein"','under review','accepted, 2026','Accepted article']:
 check(stale not in home,f'Retired or obsolete homepage content: {stale}')
check(home.count('<figure')==2,'Expected two highlight figures')
check(home.count('class="research-highlight"')==2,'Expected two research highlights')
for heading in ['Analytic theory of neural-network learning under input corruption','Topology and entropy in monitored quantum dynamics']:
 check(heading in home,f'Missing highlight heading: {heading}')
check('high-noise, infinite-width limit' in home,'Missing scope of learning result')
for figure in ['learning-robustness-published.png','quantum-classification.png']:
 check(any(i.get('src','').endswith(figure) for i in page.images),f'Missing highlight figure {figure}')
for figure in ['learning-theory.png','quantum-protocol.png']:
 check(not any(i.get('src','').endswith(figure) for i in page.images),f'Unexpected extra figure {figure}')
# The bibliography is the only full citation record; highlights share its links.
from html import unescape
groups=json.loads((Path(__file__).resolve().parent.parent/'_data/publications.json').read_text())
clean=lambda value:' '.join(unescape(re.sub('<[^>]+>','',value)).split())
home_text=clean(home)
expected_bibliography=[p['project'] for group in groups for p in group['papers']]
home_projects=re.findall(r'class="bibliography-entry" data-project="([^"]+)"',home)
check(home_projects==expected_bibliography,'Homepage bibliography must contain each shared citation once in data order')
check(len(home_projects)==6,'Expected six publication entries')
check(re.findall(r'<ol class="bibliography-list" start="(\d+)"',home)==['1'],'Journal bibliography must begin at 1')
for group in groups:
 for paper in group['papers']:
  for field in ['title','authors','venue']:
   check(clean(paper[field]) in home_text,f'Missing citation {field}: {paper["project"]}')
  check(home_text.count(clean(paper['title']))==1,f'Duplicate full citation: {paper["project"]}')
  if paper.get('note'):check(clean(paper['note']) in home_text,f'Missing publication status: {paper["project"]}')
  if paper.get('url'):check(paper['url'] in page.links,f'Missing paper link: {paper["project"]}')
  if paper['project'] in ['learning','quantum']:
   section=home.split('id="'+paper['project']+'"',1)[1].split('</section>',1)[0]
   check(paper['url'] in section and 'Read the paper' in section,f'Missing highlight paper link: {paper["project"]}')
   for link in paper.get('links',[]):
    if link['label']=='Research code':check(link['url'] in section,f'Missing highlight code link: {paper["project"]}')
check('Physical Review Research 8, 043088 (2026).' in home,'Missing published learning citation')
check('https://doi.org/10.1103/qkrg-wbbj' in page.links,'Missing published learning DOI')
talks=json.loads((Path(__file__).resolve().parent.parent/'_data/talks.json').read_text())
check(len(talks)==3 and home.count('<time datetime=')==3,'Expected three talks')
for talk in talks:
 for field in ['venue','title','display_date']:
  check(clean(talk[field]) in home_text,f'Missing talk {field}: {talk["date"]}')
 if talk.get('url'):check(talk['url'] in page.links,f'Missing talk program {talk["date"]}')
for alias,target in {'research':'/#research','year-archive':'/#research','talkmap.html':'/#talks','talks':'/#talks','teaching':'/cv/','about':'/','publications':'/#publications','resume':'/cv/','cv-json':'/cv/'}.items():
 p=root/alias
 if p.is_dir():p=p/'index.html'
 check(p in html and bool(html[p].refresh),f'Missing redirect {alias}')
 if p in html:check(any((lambda u: u.path+('#'+u.fragment if u.fragment else ''))(urlsplit(x.split('url=',1)[-1]))==target for x in html[p].refresh),f'Wrong redirect {alias}')
research=(root/'research/index.html').read_text()
check("['#learning', '#quantum']" in research and 'window.location.replace' in research,'Missing legacy research fragment forwarding')
check('research-highlight' not in research,'Legacy Research must not render old content')
for profile in ['scholar.google.com','github.com/AsadullahBhuiyan','linkedin.com/in/asadullah-bhuiyan','mailto:ab2398@cornell.edu']:
 check(any(profile in link for link in page.links),f'Missing professional profile {profile}')
check(len(list(root.rglob('*.pdf')))==1,'Unexpected PDF beyond approved CV')
for private in ['docs','scripts','Documents','tmp','.git','README.md','Gemfile','Gemfile.lock','LICENSE']:
 check(not (root/private).exists(),f'Internal file exposed in build: {private}')
print(json.dumps({'html_pages':len(html),'local_links_checked':checked_links,'publication_entries':len(expected_bibliography),'research_figures':home.count('<figure'),'errors':errors},indent=2))
sys.exit(bool(errors))
