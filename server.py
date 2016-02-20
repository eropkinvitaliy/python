import socket                                                                   
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                           
s.bind(('127.0.0.1', 2222))                                                     
s.listen(5)                                                                     
while True:                                                                     
    client, addr = s.accept()
    print(addr)	  
    data = client.recv(1024)  
    if bytes('close'.encode('utf-8')) in data:  
        print('connect close')
        client.close()                                                          
        s.close()                                                               
        break                                                                  
    if data:              
        client.sendall(bytes("""HTTP/1.1 200 OK \r\n Content-Type: text/html; charset=utf-8 \r\n\n <!DOCTYPE html>
	<html lang="en">
	<head>
    	<meta charset="UTF-8">
	<title>Document</title>
	</head>
	<body>
	<h1>Hello</h1>
	</body>
	</html>""".encode('utf-8')))