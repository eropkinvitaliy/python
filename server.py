import socket                                                                   
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                           
s.bind(('', 2222))                                                     
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
        client.send(data)