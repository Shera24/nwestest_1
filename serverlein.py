#!/usr/bin/env python3

import socket

HOST = ''                 
PORT = 8080             
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
     
    conn, addr = s.accept()
    
    with conn:
        print('GET / HTTP/1.1\r\nHost: localhost\r\n\r\n', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            outdata = "HTTP/1.1 200 OK\r\n\r\n<html><body><h1>Hi BULME</h1></body></html>"
        
            print (outdata)
            conn.sendall(outdata-encode)
            
            
    conn.close()            
            