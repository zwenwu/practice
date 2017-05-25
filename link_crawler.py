import re
import download
import urllib.parse
import urllib.robotparser
def link_crawler(seed_url,link_regex,user_agent='wswp'):#不支持页面深度
	crawl_queue = [seed_url]
	seen = set(crawl_queue)
	rp = urllib.robotparser.RobotFileParser()
	rp.set_url(seed_url.format('/robots.txt'))
	rp.read()
	while crawl_queue:
		url = crawl_queue.pop()
		if rp.can_fetch(user_agent,url):
			html = download.download(url)
			for link in get_links(html):
				if re.match(link_regex,link):
					link = urllib.parse.urljoin(seed_url,link)
					if link not in seen:
						seen.add(link)
						crawl_queue.append(link)
		else:
			print('Blocked by robots.txt: ',url)

def get_links(html):
	webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
	return webpage_regex.findall(html)
