import re
import download
def crawl_sitemap(url):
	sitemap = download.download(url)
	links = re.findall('<loc>(.*?)</loc>',sitemap)
	for link in links:
		html = download.download(link)
