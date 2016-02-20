import socket                                                                   
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                           
s.bind(('', 2222))                                                     
s.listen(10)   
while True:   
    conn, addr = s.accept()	                                                                  
    data = conn.recv(1024)  
    if bytes('close'.encode('utf-8')) in data:  
        conn.close()                                                          
        s.close()                                                               
        break                                                                  
    if data:              
        conn.send(data)
        conn.close()


