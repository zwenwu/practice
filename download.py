import urllib.request
import urllib.error
import urllib.parse
def download(url,user_agent='wswp',proxy=None,num_retries=2):
	print('Download: ',url)
	headers = {'User_agent' : user_agent}
	request = urllib.request.Request(url,headers=headers)
	opener = urllib.request.build_opener()
	if proxy:
		proxy_params = {urllib.parse.urlparse(url).scheme: proxy}
		opener.add_handler(urllib.request.ProxyHandler(proxy_params))
	try:
		html = urllib.request.urlopen(request).read().decode('utf-8')
	except urllib.error.URLError as e:
		print('Download error: ',e.reason)
		html = None
		if num_retries > 0:
			if hasattr(e,'code') and 500 <= e.code < 600:
				download(url,user_agent,proxy,num_retries-1)
	return html