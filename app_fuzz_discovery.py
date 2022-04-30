"""
* Name  : Fast Fuzzing script
* PL	: Python
* Author: Yacine BOULBOT
"""

import aiohttp
import asyncio
import time
import argparse
import requests as r
from validator_collection import checkers
from os import path
# from tqdm import tqdm
# from alive_progress import alive_bar
from colorama import Fore, Back, Style
from datetime import datetime
from art import tprint
from itertools import cycle
import ipaddress


BOLD='\033[1m'
END = '\033[0m'

# http = ['85.25.72.91:5566', '144.217.240.185:9300', '121.156.109.108:8080', '65.21.3.120:80', '51.75.206.209:80', '103.47.66.150:8080', '46.0.203.186:8080', '103.148.178.228:80', '47.117.136.150:22', '50.206.25.110:80', '132.145.195.93:3128', '103.117.192.14:80', '160.226.208.239:8080', '178.134.157.215:8080', '85.25.119.113:5566', '103.209.64.19:6666', '61.9.34.98:1337', '190.152.182.150:55443', '88.119.195.35:8080', '134.209.42.113:8888', '5.9.201.68:3128', '180.250.204.91:8088', '186.67.26.178:999', '120.220.220.95:8085', '93.86.63.73:8080', '61.91.61.110:80', '154.0.12.57:8080', '165.16.71.1:1981', '114.5.199.208:8080', '118.193.47.193:8118', '156.200.116.78:1976', '154.66.109.209:8080', '156.200.113.178:1976', '186.67.26.181:999', '168.235.64.246:8118', '168.205.100.36:8080', '168.83.78.195:80', '115.233.221.139:3128', '85.25.91.156:5566', '41.65.246.3:3129', '202.146.1.119:8080', '202.152.12.202:8080', '186.67.26.180:999', '197.246.212.70:3030', '170.233.235.249:3128', '203.123.57.154:63123', '103.156.218.232:8080', '175.144.112.239:80', '50.206.25.109:80', '41.65.67.166:1976', '223.96.90.216:8085', '36.91.107.61:8080', '66.211.155.34:8080', '67.73.184.178:8081', '103.140.188.61:8085', '80.106.247.145:53410', '152.231.25.58:8080', '217.73.139.204:8080', '46.99.205.2:8080', '95.216.12.141:22209', '85.25.100.47:5566', '188.138.101.167:5566', '95.161.188.246:38302', '68.185.57.66:80', '181.129.2.90:8081', '50.206.25.106:80', '177.87.168.105:53281', '84.252.139.198:3128', '103.216.82.20:6666', '177.19.131.82:3130', '177.93.33.246:999', '88.255.101.231:8080', '81.24.117.250:18080', '122.155.165.191:3128', '20.47.108.204:8888', '190.113.40.94:999', '77.73.241.154:80', '194.233.69.41:443', '85.25.198.22:5566', '197.246.212.12:3030', '41.77.7.234:3129', '85.26.146.169:80', '45.175.160.25:999', '194.233.73.108:443', '188.138.89.29:5566', '20.81.62.32:3128', '188.246.186.142:41890', '185.255.47.59:8080', '47.92.113.71:80', '159.65.171.69:80', '203.84.153.250:8080', '173.82.149.243:8080', '121.168.11.196:80', '192.99.239.215:8080', '197.157.219.169:48625', '124.158.167.18:8080', '152.67.85.151:8118', '114.6.88.238:60811', '173.249.57.9:443', '45.189.113.63:999', '103.80.237.211:3888', '47.113.90.161:83', '185.94.218.57:43403', '139.5.150.146:3888', '27.72.105.233:19132', '103.53.19.204:60080', '149.56.96.252:5566', '85.25.91.161:5566', '179.106.86.3:8080', '85.25.201.22:5566', '181.188.156.171:3128', '175.144.112.238:80', '82.147.118.164:8080', '195.175.89.198:8080', '103.138.41.132:8080', '37.204.157.91:41890', '217.60.194.53:8080', '103.78.254.78:80', '46.219.80.142:57401', '175.106.10.226:51630', '47.74.226.8:5001', '86.123.166.13:8080', '182.253.199.102:8080', '47.100.255.35:80', '41.65.236.58:1976', '36.94.161.219:8080', '54.39.102.233:3128', '154.236.168.169:1981', '202.63.243.226:8080', '106.15.2.195:8118', '187.19.158.13:80', '202.169.51.46:8080', '202.180.21.107:8080', '190.109.0.226:999', '139.255.10.234:8080', '41.65.67.166:1981', '94.23.91.209:80', '84.205.17.234:8080', '103.36.35.135:8080', '193.164.131.202:7890', '175.144.112.236:80', '186.159.20.210:8080', '103.241.182.97:80', '77.236.237.241:1256', '31.163.192.161:3129', '177.55.245.198:8080', '188.138.106.158:5566', '103.159.46.34:83', '160.19.232.85:3128', '50.206.25.104:80', '213.6.28.87:8080', '51.68.199.120:3128', '45.172.111.20:999', '51.81.80.44:80', '103.14.199.225:83', '201.186.131.56:999', '159.192.138.170:8080', '181.78.16.235:8080', '158.140.169.101:10000', '85.25.226.242:5566', '190.103.28.250:999', '1.20.217.52:8080', '183.88.210.77:8080', '50.206.25.111:80', '181.198.86.74:999', '187.216.90.46:53281', '177.39.136.163:8080', '110.232.67.42:55443', '107.151.182.247:80', '185.136.151.138:41890', '103.159.90.22:82', '45.175.160.29:999', '179.51.136.3:8080', '103.81.214.235:84', '213.230.121.114:3128', '159.192.131.178:8080', '185.213.167.164:8081', '62.75.236.132:5566', '202.164.152.229:8080', '191.97.19.158:999', '152.228.163.151:80', '85.25.150.32:5566', '115.75.2.213:38351', '36.94.27.124:8080', '112.6.117.135:8085', '106.54.128.253:999', '35.230.154.184:3128', '186.208.81.214:3129', '170.155.5.235:8080', '200.106.184.12:999', '23.238.33.186:80', '41.65.236.37:1976', '79.124.78.144:80', '5.16.0.97:1256', '12.69.91.226:80', '45.229.34.101:999', '80.244.226.92:8080', '131.72.69.98:45005', '203.243.63.16:80', '36.92.22.70:8080', '69.160.192.139:8080', '176.236.85.246:9090', '185.175.119.113:47174', '68.188.59.198:80', '103.218.102.162:8080', '14.160.24.212:8080', '113.176.81.31:55443', '200.13.154.49:8080', '103.14.198.21:83', '221.159.192.122:12345', '108.166.183.204:80', '158.181.21.247:8081', '37.61.220.237:1080', '103.163.134.4:8181', '179.43.101.150:999', '103.124.136.90:63123', '103.73.75.69:8080', '202.169.252.190:8181', '197.157.193.219:8080', '103.83.178.166:8181', '170.80.202.238:999', '31.179.228.64:8081', '45.181.207.129:999', '197.255.55.122:41890', '177.155.215.36:8080', '43.243.174.26:84', '103.14.198.145:83', '45.182.22.54:999', '200.112.215.21:999', '103.106.219.77:8080', '177.234.212.71:999', '49.0.82.190:8080', '45.230.169.9:999', '94.231.178.249:9797', '181.224.162.199:999', '89.204.214.142:8080', '201.150.117.97:999', '175.101.14.115:84']
# proxy_cycle = cycle(http)

# print messages with colors
def pretty(data, message ,color):
	for i in data:
		if not i.endswith("/"):
			print(f"{color}" + message + "\t"+ i + f"{Style.RESET_ALL}")


async def get_urls(session, url, http_response_codes, output):
    async with session.head(url) as server_response:
        # proxy = next(proxy_cycle)
        # print(r.get(url='https://ident.me/', proxy=http))
        try:
        	url_code = {}
        	http_response_codes.append(301)
        	http_response_codes = set(http_response_codes)
        	if server_response.status in http_response_codes:
        		url_code[server_response.status] = url
        	if bool(url_code): # check if dic is not empty
	        	if output != "Pen":
	        		data = str(server_response.status) + " --> " + url + "\n"
	        		with open(output,'a') as file:
	        			file.write(data)
	        	return url_code
        except:
            print("ERROR retrieving following url ==> ", url)

async def main(url, filename, matches, output):
	async with aiohttp.ClientSession() as session:
		with open(filename,"r", encoding='latin-1') as f:
			urls = f.readlines()
			tasks = []
			for page in urls:
				current_target = url + page[:-1]
				tasks.append(asyncio.ensure_future(get_urls(session, current_target, matches, output)))
			original_url = await asyncio.gather(*tasks)
			resp_200 = []
			resp_403 = []
			new_dirs = []
			other_resp = []
			for url in original_url:
				if url is not None:
					if list(url.keys())[0] == 200:
						resp_200.append(list(url.values())[0])
					elif list(url.keys())[0] == 301:
						new_dir = list(url.values())[0]+"/"
						new_dirs.append(new_dir)
					elif list(url.keys())[0] == 403:
						resp_403.append(list(url.values())[0])
					else:
						if list(url.keys())[0] != 404:
							other_resp.append(url)
			return resp_200, resp_403, other_resp, new_dirs



def check_ip(ip):
  if ip.startswith("http://") or ip.startswith("https://"):
    tmp = ip.split("//")[1]
    if "/" in tmp:
      return tmp.split("/")[0]
    else:
      return tmp
  else:
    return False



def is_ip(ip):
	ip = check_ip(ip)

	if not ip:
		return False
	else:
		try:
			if ":" in ip:
				if int(ip.split(":")[1]) < 65535 and int(ip.split(":")[1]) > 0:
					if ipaddress.ip_address(ip.split(":")[0]):
						return True
				else:
					return False
				if ipaddress.ip_address(ip.split(":")[0]):
					return True
		except:
			return False


def menu(url, dictionnary, matches, output, urls_200):
	try:
		if url is not None:
			if(checkers.is_url(url) or True):
				if not url.endswith("/"):
					url = url + "/"
				print(url, " is a valid url")
				print(BOLD+Back.WHITE+Fore.LIGHTRED_EX + "Currently fuzzing => ",url+END)
				if dictionnary is not None:
					check_file = path.exists(dictionnary)
					if check_file:
						if matches is not None:
							try:
								if isinstance(matches, list):
									matches = ','.join(str(i) for i in matches)
								response = (matches).split(",")
								response = [ int(i) for i in response ]
								if output is not None and output != "Pen":
									res = asyncio.run(main(url, dictionnary, response, output))
									urls_200.append(res[0])
									pretty(res[0],"\t[+] Code: 200 => Interesting File found: ", Fore.LIGHTGREEN_EX)
									pretty(res[1],"\t[*] Code: 403 => Might be Interesting: ", Fore.LIGHTYELLOW_EX)
									pretty(res[2],"\t[-] Other files: " ,Fore.LIGHTRED_EX)
									print()
									if res[3]:
										pretty(res[3], "\t\t[=>]  A new directory found", Fore.YELLOW)
										print()
										for new_dir in res[3]:
											menu(new_dir, dictionnary, response, output,urls_200)
								else:
									res = asyncio.run(main(url, dictionnary, response,  "Pen")) #, urls_200))
									urls_200.append(res[0])
									pretty(res[0],"\t[+] Code: 200 => Interesting File found: ", Fore.LIGHTGREEN_EX)
									pretty(res[1],"\t[*] Code: 403 => Might be Interesting: ", Fore.LIGHTYELLOW_EX)
									pretty(res[2],"\t[-] Other files: " ,Fore.LIGHTRED_EX)
									print()
									if res[3]:
										pretty(res[3], "\t\t[=>]  A new directory found", Fore.YELLOW)
										print()
										for new_dir in res[3]:
											menu(new_dir, dictionnary, response,  "Pen",urls_200)
							except Exception as e:
								print(BOLD+Fore.RED +"Invalid HTTP Response status: "+ matches+END)
								print("Error: ", e)
								print("Please provide valid http response code (check: https://developer.mozilla.org/fr/docs/Web/HTTP/Status)")
								end_message()
								exit(-1)
						else:
							print(Fore.LIGHTYELLOW_EX + "using default status: 200,403"+END)
							response = [200,403]
							res = asyncio.run(main(url, dictionnary, response,  "Pen"))#,urls_200))
							urls_200.append(res[0])
							pretty(res[0],"\t[+] Code: 200 => Interesting File found: ", Fore.LIGHTGREEN_EX)
							pretty(res[1],"\t[*] Code: 403 => Might be Interesting: ", Fore.LIGHTYELLOW_EX)
							pretty(res[2],"\t[-] Other files: " ,Fore.LIGHTRED_EX)
							print()
							if res[3]:
								pretty(res[3], "\t\t[=>]  A new directory found", Fore.YELLOW)
								print()
								for new_dir in res[3]:
									menu(new_dir, dictionnary, response,  "Pen", urls_200)
							print('')
					else:
						print(BOLD+Fore.RED +"Please provide a valid path to your dictionnary.\n[-] Unable to open file: "+ dictionnary+"\nQuitting..."+END)
						end_message()
						exit(-1)
				else:
					# print("je suis la")
					# response = [200,403]
					# dictionnary = "w.txt"
					dictionnary = "/usr/share/wordlists/dirb/common.txt"
					check_file = path.exists(dictionnary)
					if check_file:
						if matches is not None:
							try:
								print(Fore.LIGHTYELLOW_EX + "using status: "+matches+END)
								print(Fore.LIGHTYELLOW_EX + "using default dictionnary: "+dictionnary+END)
								if isinstance(matches, list):
									matches = ','.join(str(i) for i in matches)
								response = (matches).split(",")
								response = [ int(i) for i in response ]
								if output is not None and output != "Pen":
									res = asyncio.run(main(url, dictionnary, response, output))
									urls_200.append(res[0])
									pretty(res[0],"\t[+] Code: 200 => Interesting File found: ", Fore.LIGHTGREEN_EX)
									pretty(res[1],"\t[*] Code: 403 => Might be Interesting: ", Fore.LIGHTYELLOW_EX)
									pretty(res[2],"\t[-] Other files: " ,Fore.LIGHTRED_EX)
									print()
									if res[3]:
										pretty(res[3], "\t\t[=>]  A new directory found", Fore.YELLOW)
										print()
										for new_dir in res[3]:
											menu(new_dir, dictionnary, response, output,urls_200)
								else:
									res = asyncio.run(main(url, dictionnary, response,  "Pen")) #, urls_200))
									urls_200.append(res[0])
									pretty(res[0],"\t[+] Code: 200 => Interesting File found: ", Fore.LIGHTGREEN_EX)
									pretty(res[1],"\t[*] Code: 403 => Might be Interesting: ", Fore.LIGHTYELLOW_EX)
									pretty(res[2],"\t[-] Other files: " ,Fore.LIGHTRED_EX)
									print()
									if res[3]:
										pretty(res[3], "\t\t[=>]  A new directory found", Fore.YELLOW)
										print()
										for new_dir in res[3]:
											menu(new_dir, dictionnary, response,  "Pen",urls_200)
							except Exception as e:
								print(BOLD+Fore.RED +"Invalid HTTP Response status: "+ matches+END)
								print("Error: ", e)
								print("Please provide valid http response code (check: https://developer.mozilla.org/fr/docs/Web/HTTP/Status)")
								end_message()
								exit(-1)
						else:
							print(Fore.LIGHTYELLOW_EX + "using default status: 200,403"+END)
							response = [200,403]
							res = asyncio.run(main(url, dictionnary, response,  "Pen"))#,urls_200))
							urls_200.append(res[0])
							pretty(res[0],"\t[+] Code: 200 => Interesting File found: ", Fore.LIGHTGREEN_EX)
							pretty(res[1],"\t[*] Code: 403 => Might be Interesting: ", Fore.LIGHTYELLOW_EX)
							pretty(res[2],"\t[-] Other files: " ,Fore.LIGHTRED_EX)
							print()
							if res[3]:
								pretty(res[3], "\t\t[=>]  A new directory found", Fore.YELLOW)
								print()
								for new_dir in res[3]:
									menu(new_dir, dictionnary, response,  "Pen", urls_200)
							print('')
					else:
						print(BOLD+Fore.RED +"Please provide a valid path to your dictionnary.\n[-] Unable to open file: "+ dictionnary+"\nQuitting..."+END)
						end_message()
						exit(-1)
					# 	print("Using default dictionnary: ", dictionnary)
					# 	res = asyncio.run(main(url, dictionnary, response,  "Pen"))#,urls_200))
					# 	urls_200.append(res[0])
					# 	pretty(res[0],"\t[+] Code: 200 => Interesting File found: ", Fore.LIGHTGREEN_EX)
					# 	pretty(res[1],"\t[*] Code: 403 => Might be Interesting: ", Fore.LIGHTYELLOW_EX)
					# 	pretty(res[2],"\t[-] Other files: " ,Fore.LIGHTRED_EX)
					# 	print()
					# 	if res[3]:
					# 		pretty(res[3], "\t\t[=>]  A new directory found", Fore.YELLOW)
					# 		print()
					# 		for new_dir in res[3]:
					# 			menu(new_dir, dictionnary, response,  "Pen", urls_200)
					# else:
					# 	print(BOLD+Fore.RED + "Unable to open ", dictionnary, ". Please Make sure file exists and you have read access on it\nQuitting..." +END)
					# 	end_message()
					# exit(-1)
			else:
				print(BOLD+Fore.RED+"Please provide a valid url"+END)
				end_message()
				exit(-1)
	except Exception as e:
		print("Raised exception => ", e)
	return urls_200


def end_message():
	print("\n\n\n"+BOLD+Back.WHITE+Fore.BLACK+"Written by: Yacine Boulbot"+END)

def find_secrets(url_list):
	try:
		with open("false_positives.txt","r") as file:
			false_positives = list(set(file.read().split("\n")))
		with open("db.txt","r",encoding="latin-1") as db:
			data =  list(set(db.read().split("\n")))
			for url in url_list:
				for keyword in data:
					for line in r.get(url).text.split("\n"):
						line = line.strip()
						if keyword in line:
							c = 0
							for fp in false_positives:
								if fp  not in line:
									c +=1
									# print(Fore.RED+"False positive detected")
							if c == len(false_positives):
								print(Fore.LIGHTGREEN_EX+"[+] Found: "+ END+line  + Fore.YELLOW + " \t[*] Link: "+ url + END)
	except Exception as e:
		print("An error occured: ", e)
		exit(-2)

# get robots directories
def robots(url):
	data = r.get(url).text
	if r.get(url).status_code == 200:
		x = [i for i in data.split("\n") if "/" in i]
		new_paths = [ i.split(":")[1].strip() for i in data.split("\n") if i.startswith("Disallow") or i.startswith("Allow")]
		if len(x) >0:
			for i in x:
				if i not in new_paths:
					new_paths.append(i)
		print("New path founds on Robots.txt file: ")
		return new_paths

# print(robots("https://www.azfrance.fr/robots.txt"))




if __name__ == '__main__':
	
	parser = argparse.ArgumentParser(description=f"{Fore.YELLOW}*** Super Fast web fuzzing tool ***{Style.RESET_ALL}", epilog=f"{Fore.BLACK}Written by: Yacine Boulbot{Style.RESET_ALL}")
	parser.add_argument("-u", "--url",  type=str, help=f"{Fore.YELLOW}Specify a web url (ex: http://localhost/, https://vuln.com/, http://1.2.3.4/ {Style.RESET_ALL}",required=True)
	parser.add_argument("-d", "--dictionnary", type=str, help=f"{Fore.YELLOW}Dictionnary wordlist{Style.RESET_ALL}", required=False)
	parser.add_argument("-m", "--match", type=str, help=f"{Fore.YELLOW}Match http response code (usage exemple: --match 200,403,500..){Style.RESET_ALL}", required=False)
	parser.add_argument("-o", "--output", type=str, help=f"{Fore.YELLOW}Save result to a file{Style.RESET_ALL}", required=False)
	args = parser.parse_args()
	tprint("""Super Fast
		Fuzzing Tool""", font="random")
	start_time = time.time()
	urls_200 = []
	print(BOLD+Back.WHITE+Fore.MAGENTA+ "Started at: ", datetime.now().strftime("%d/%m/%Y %H:%M:%S"), END)
	try:
		urls_200 = menu(args.url, args.dictionnary, args.match, args.output, urls_200)
		urls_200 = [item for sublist in urls_200 for item in sublist]
		urls_200 = [ i for i in urls_200 if not i.endswith("/")]
		try:
			print("fuzzing robots.txt")
			r_dirs = robots(args.url+"/robots.txt")
			for i in r_dirs:
				if i.endswith("/"):
					menu(args.url+i, args.dictionnary, args.match, args.output, urls_200)
				else:
					print("New Path found in robots.txt: ", i)

		except:
			print("Error 404 robots.txt file not found")
		print("Fuzzing phase ended\nScanning accessible files for juicy informations")
		# print("****  ", urls_200)
		find_secrets(urls_200)
	except:
		pass
	if args.output is not None:
		print(BOLD+Back.LIGHTCYAN_EX + Fore.WHITE +"data saved into: ", args.output + END)
	print(BOLD+Back.WHITE+Fore.MAGENTA+  "Ended at: ", datetime.now().strftime("%d/%m/%Y %H:%M:%S"), END)
	print(BOLD+f"{Fore.CYAN}Time Elapsed ---< %s seconds >---" % (time.time() - start_time), F"{Style.RESET_ALL}")
	# 304 secondes --> 14521


"""
TODO:
* Add regular expressions to detect AWS keys, SSH Keys, Credentials...
"""