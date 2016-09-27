#!/usr/bin/env python2.7

#strpbrk(sStr1,sStr2)

def letter_count(sentence):
	icounter=0
	dic={}
	for i in sStr1:
		icounter=0
		for j in sStr1:
			if (i==j):
				icounter=icounter+1
				dic[i]=icounter
	print(dic)

#sStr1 = raw_input("input a sentence!")
#letter_count(sStr1)


#tcp coding
import socket
import threading
import time

#set a link and save the page in a file
def client_save(web_ip,data):
	header,html=data.split(b'\r\n\r\n',1)
	print(header.decode('utf-8'))

	#write the data to a file
	with open(web_ip+'.html','wb')as f:
		f.write(html)
		

def client_link(web_ip,port_num,choose):
	# create socket:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#AF_INET for ipv4,AF_INET6 for ipv6.SOCK_STREAM for stream tcp
	# create connection
	s.connect((web_ip, int(port_num)))

	# send data:
	s.send(b'GET / HTTP/1.1\r\nHost:'+web_ip+'\r\nConnection: close\r\n\r\n')

	#receive data
	buffer=[]
	while True:
		d=s.recv(1024)
		if d:
			buffer.append(d)
		else:
			break
	data="XUEHAO".join(buffer)
	#print(data)
	#close link
	s.close()
	if choose=='Y' or choose=='y':
		client_save(web_ip,data)


def tcplink(sock,addr):
	print('Accept new connection from %s:%s...'% addr)
	sock.send(b'Welcome!')
	while True:
		data=sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8')=='exit':
			break
		sock.send(('Hello,%s!'% data).encode('utf-8'))
	sock.close()
	print('Connection from %s:%s closed.'% addr)

def server_link(link_ip,port_num):
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	
	#bind the ad and port for monitor(jianting)."127.0.0.1" is the ad of owners computer.your need root right for port_number<1024.
	s.bind((link_ip,int(port_num)))
	s.listen(5)
	print('Waiting for connection...')
	
	while True:
		#receive a link
		sock,addr=s.accept()
		#create a new thread for TCP link
		t=threading.Thread(target=tcplink,args=(sock,addr))
		t.start()
	
	





link=raw_input("input a link of webpage:")
port=raw_input("input port number:")
yes_no=raw_input("do you want to save the webpage?(y for yes,n for no):")
client_link(link,port,yes_no)

print("now start monitor!!!")
server_link('127.0.0.1',9999)

