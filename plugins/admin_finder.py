"""
admin_finder.py- web admin finder
author: levi0x0
Copyright (c) 2013-201x sb0x project

See the file LICENSE
"""
import urllib2
import sys

def admin_finder(target, lst):

	try:
		toGo = "%s/%s" % (target, lst)
		urllib2.urlopen(toGo)
	
	except urllib2.HTTPError, e:
		if e.code != 404:
			print "[+] %s | %s" % (toGo, e.code)
			sys.exit()
		elif e.code == 404:
			print "[-] %s [404]" % (toGo)
	except urllib2.URLError, e:
		print "[+] %s | %s" % (toGo, e.code)
		raw_input("->Found...")
	else:
		print "[+] %s" % (toGo)
		raw_input("->Found...")

try:
	print "--Web admin Finder v.0.2--"
	print "- include http://\n"
	target = raw_input("* Target:")
	if not "://" in target:
		print "http:// requierd.."
		sys.exit()
	else:
		pass
	print "\n* Type:"
	print "(1) PHP"
	print "(2) ASP"
	print "(3) ASPX"
	ask = int(raw_input(">"))
	if ask == 1:
		lst = raw_input("* WordList: (Default)") or "wordlist/af_php.lst"
	elif ask == 2:
		lst = raw_input("* WordList: (Default)") or "wordlist/af_asp.lst"
	elif ask == 3:
		lst = raw_input("* WordList: (Default)") or "wordlist/af_aspx.lst"
	else:
		print "* Please choice type"
		sys.exit(1)
	lst = open(lst, 'rU').readlines()

	for lst in lst:
		admin_finder(target, lst.replace('\n', ''))
except KeyboardInterrupt:
	print "\n[*] bye."
	sys.exit()
except AttributeError:
	print "[-]connection faild.. OR URL Unvaild."
	sys.exit()
except:
	print "[-] got error!"
	print "[*] Please report: https://www.github.com/Levi0x0/sb0x-project"
	sys.exit()
