import urllib.request


def public_ip():
	lista = "0123456789."
	ip=""
	dato=urllib.request.urlopen("http://checkip.dyndns.org").read()
	for x in str(dato):
		if x in lista:
			ip += x
	return ip
	


def main():
	print(public_ip())

if __name__ == "__main__":
	main()	

