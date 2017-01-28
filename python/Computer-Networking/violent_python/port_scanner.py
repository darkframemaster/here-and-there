#!/usr/bin/env python

import socket
import os
import sys

def retBanner(ip, port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip, port))
		banner = s.recv(1024)
		return banner
	except:
		return ''

def checkVulns(banner, filename):
	f = open(filename, 'r')
	for line in f.readlines():
		if line.strip('\n') in banner:
			print '[+] Server is vulnerable: ' + banner.strip('\n')
		else:			
			print 'Error: bad banner, ' + line

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		if not os.path.isfile(filename):
			print '[-] ' + filename + ' does not exist.'
			exit(0)
		if not os.access(filename, os.R_OK):
			print '[-] ' + filename + ' access denied.'
			exit(0)
	else:
		print '[-] Usage: ' + str(sys.argv[0]) + ' <vuln filename>'
		exit(0)
	
	print '[+] Start scanning'
	port_list = [21, 22, 25, 80, 110, 443]
	for x in range(147, 150):
		ip = '101.200.56.34'
		for port in port_list:
			banner = retBanner(ip, port)
			if banner:
				print '[+] ' + ip + ':' + str(port) + '\n' + banner
				checkVulns(banner, filename)

if __name__ == '__main__':
	main()
