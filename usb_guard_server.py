import socket

s=socket.socket()

s.bind(('', 1313))
s.listen(20)

uuids = []

while True:
	print('waiting for a connection')
	conn, addr = s.accept()
	try:
		print('address is', addr)
		while True:
			data = conn.recv(2048)
			print('recieved', data)
			if data:
				if data not in uuids:
					uuids.append(data)
				print('sending', uuids, 'to client')
				conn.sendall(uuids)
			else:
				print('no data from client om address:',addr)
				break
	finally:
		conn.close()