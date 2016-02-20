import socket                                                                   
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                           
s.bind(('', 2222))                                                     
s.listen(5)   
client, addr = s.accept()                                                                  
while True:                                                                     
    data = client.recv(1024)  
    client.settimeout(60)
    if bytes('close'.encode('utf-8')) in data:  
        client.close()                                                          
        s.close()                                                               
        break                                                                  
    if data:              
        client.send(data)
        client.close()

