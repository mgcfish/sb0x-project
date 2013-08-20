"""
test.py lib for http POST method brute force
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

	def __init__(self, target, tags, user, passwords, proxy, proxy_server, proxy_port, user_agent,verbose,log_err):

		self.target = target #target
		self.tags = tags #HTML tags
		self.user = user #UserName
		self.passwords = passwords #Passwords wordlist
		self.proxy = proxy #proxy true or false
		self.proxy_server = proxy_server #proxy server
		self.proxy_port = proxy_port #proxy port
		self.log_err = log_err #login error 
		self.user_agent = user_agent #user_agetn lists
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

		self.request = urllib2.Request( self.target, self.data, self.headers )
		self.response = urllib2.urlopen( self.request ).read()
		#start analyze response
		if not self.log_err in self.response:
			print "[*] Login ERROR NOT FOUND"
			print "[*] USER: %s" % (self.user)
			print "[*] PASS: %s" % (self.passwords)
			sys.exit(0)

		else:
			if self.verbose:
				print "[-]USER: %s PASS:%s" % ( self.user, self.passwords)
			else:
				pass

			
