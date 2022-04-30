import requests as r
# from lxml import html
from bs4 import BeautifulSoup

# def read_proy_list(list_of_proxies_files):
# 	http_proxy = {}
# 	https_proxy = {}
# 	ftp_proxy = {}
# 	files  = list_of_proxies_files.split(",")

# 	# with open(list_of_proxies_files) as f :
# 	# 	data = f.read().split("\n")
# 	# 	for 

# # http_proxy  = "http://10.10.1.10:3128"
# # https_proxy = "https://10.10.1.11:1080"
# # ftp_proxy   = "ftp://10.10.1.10:3128"



# def send_through_proxies(url, proxy_list):
# 	res = r.get(url, proxies=proxy_list)
# 	print(res.head())


# https://www.scrapingbee.com/blog/python-requests-proxy/
def grab_proxies():
	# session = requests.Session()

	proxies = {}
	http = r.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all").text.split("\r\n")
	https = r.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=https&timeout=10000&country=all&ssl=all&anonymity=all").text.split("\r\n")
	socks4 = r.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all").text.split("\r\n")
	socks5 = r.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all").text.split("\r\n")

	http = ",".join([i for i in http if i != ""])
	https = ",".join([i for i in https if i != ""])
	socks4 = ",".join([i for i in socks4 if i != ""])
	socks5 = ",".join([i for i in socks5 if i != ""])
	
	proxies['http']=http.split(",")
	proxies['https']=https.split(",")
	proxies['socks4']=socks4.split(",")
	proxies['socks5']=socks5.split(",")
	# session.proxies = proxies

	return http, https, socks4, socks5







# free proxy lists online
# https://spys.one/en/
# https://free-proxy-list.net/
# https://proxyscrape.com/free-proxy-list
# https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=yes&anonymity=all
print(grab_proxies())