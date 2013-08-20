"""
menu.py user menu interface

Copyright (c) 2013-201x sb0x project

See the file LICENSE
"""
from banner import *
import sys
import time
import os

banner()
while True:
	try:
		options()
		print "-->Press Ctrl+C to Quit!"
		ask = int(raw_input(">"))
		if ask == 1:
			web_op()
			ask = int(raw_input("web>"))
			if ask == 1:
				web_wp()
			elif ask == 2:
				web_bf()
			elif ask == 3:
				web_af()
			else:
				print "You need to choice option..."
		elif ask == 2:
			dos_op()
			ask = int(raw_input("dos>"))
			if ask == 1:
				ms12_20()
				sys.exit()
			else:
				print "[-]You need to choice option..."
		elif ask == 3:
			import plugins.test_ftp
			sys.exit()
		elif ask == 4:
			shell_op()
			ask = int(raw_input("shell>"))
			if ask == 1:
				php_re_sh()
				sys.exit()
			elif ask == 2:
				perl_shell()
				sys.exit()
			else:
				print "[-]You need to choice option..."
				time.sleep(1.5)
		else:
			print "[-]You need to choice option..."
			time.sleep(1.5)

	except ValueError:
		print "[-]ValueError you need to choice a number.."
		time.sleep(2)
	except KeyboardInterrupt:
		print "\n[*]bye (:"
		sys.exit()
