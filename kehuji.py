#客户端
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
filename = 'C:/1.txt'
def sendfile(conn):
	str1 = conn.recv(1024)

	if os.path.exists(filename):
		print('I have %s, begin to upload!' % filename)
		conn.recv(1024)
		size = 1024
		with open(filename,'rb') as f:
			while True:
				data = f.read(size)
				conn.send(data)
				if len(data) < size:
					break
		print('%s is uploaded successfully!' % filename)
	else:
		print('Sorry, I have no %s' % filename)
		conn.send(b'no')
	conn.close()




s.listen(1)
(conn,addr)=s.accept()
print('I want to uploaded the file %s!' % filename)
s.send(filename.encode('utf-8'))
sendfile(conn)
