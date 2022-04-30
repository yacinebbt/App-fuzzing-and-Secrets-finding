import requests as r
# get robots directories
def robots(url):
	data = r.get(url).text
	x = [i for i in data.split("\n") if "/" in i]
	new_paths = [ i.split(":")[1].strip() for i in data.split("\n") if i.startswith("Disallow") or i.startswith("Allow")]
	if len(x) >0:
		for i in x:
			if i not in new_paths:
				new_paths.append(i)
	print("New path founds on Robots.txt file: ")
	return new_paths

def find_secrets(url_list):
	try:
		with open("false_positives.txt","r") as file:
			false_positives = list(set(file.read().split("\n")))
		with open("db.txt","r",encoding="latin-1") as db:
			data =  list(set(db.read().split("\n")))
			for url in url_list:
				for keyword in data:
					for line in r.get(url).text.split("\n"):
						print(url)
						line = line.strip()
						if keyword in line:
							c = 0
							for fp in false_positives:
								if fp  not in line:
									c +=1
									# print(Fore.RED+"False positive detected")
							if c == len(false_positives):
								print("[+] Found: "+line  +" \t[*] Link: "+ url )
	except Exception as e:
		print("An error occured: ", e)
		exit(-2)

# print(robots("http://10.0.2.6/robots.txt"))
l = ["http://10.0.2.6/passwords/passwords.html"]
# find_secrets(l)
print(r.get(l[0]).text.split("\n"))
print(r.get("http://10.0.2.6/robots.txt").status_code)