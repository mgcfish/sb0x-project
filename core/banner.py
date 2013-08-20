"""
menu.py user menu interface

Copyright (c) 2013-201x sb0x project

See the file LICENSE
"""

#version
version = '1.0.5-beta'

logo = '''
	+-+-+-+-+ +-+-+-+-+-+-+-+
	|s|b|0|x| |p|r|o|j|e|c|t|
	+-+-+-+-+ +-+-+-+-+-+-+-+
'''

def banner():
	print "**************************************"
	print logo
	print "\tsb0x project %s" % (version)
	print "\t  Copyright (c) 2013\n" 
	print "**************************************\n"
	
def options():
	print "--" 
	print "(1) web - Web brute force ,scanners, etc.."
	print "(2) dos - DOS exploits"
	print "(3) ftp - FTP server brute force attack"
	print "(4) shell - php_reverse_shell, perl_shell"

def web_op():
	print "Web options"
	print "(1) - Wordpress wp-login.php Brute force"
	print "(2) - Web Login Page brute force"
	print "(3) - Web admin finder"

def web_wp():
	from plugins import wordpress
	wordpress.main()
	
def web_bf():
	from plugins import test_site
	test_site.main()
def web_af():
	from plugins import admin_finder

def dos_op():
	print "DOS options:\n"
	print "(1) - MS12-020 Windows RDP DOS exploit."

def ms12_20():
	from plugins import ms12_20
	
def shell_op():
	print "Shell Options:"
	print "(1)- php_reverse_shell"
	print "(2)- perl_bind_shell"
def php_re_sh():
	from plugins import php_reverse_shell
	
def perl_shell():
	from plugins import perl_shell
