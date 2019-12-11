"""
import socket 
import select 
import sys 
HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1",1234))

while True:
    new_msg = True
    full_msg = ""
    while True:
        msg = s.recv(16)
        msg = msg.decode("utf-8")
        if new_msg:
            msg_len = int(msg[:HEADERSIZE])
            msg = msg[HEADERSIZE:]
            new_msg = False
        full_msg += msg
        if len(full_msg) == msg_len:
            print("Full Message is:")
            print(full_msg)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
if len(sys.argv) != 3: 
    print("Correct usage: script, IP address, port number")
    exit() 
IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2]) 
server.connect((IP_address, Port)) 
  
while True: 
    # maintains a list of possible input streams 
    # sockets_list = [sys.stdin, server] 
    message = server.recv(2048) 
    print(message)
    ""There are two possible input situations. Either the 
    user wants to give  manual input to send to other people, 
    or the server is sending a message  to be printed on the 
    screen. Select returns from sockets_list, the stream that 
    is reader for input. So for example, if the server wants 
    to send a message, then the if condition will hold true 
    below.If the user wants to send a message, the else 
    condition will evaluate as true""
#    read_sockets, write_socket, error_socket = select.select(sockets_list,[],[]) 
  
#    for socks in read_sockets: 
#        if socks == server: 
#            message = socks.recv(2048) 
#            print(message)
#        else: 
#            message = sys.stdin.readline() 
#           server.send(message) 
#           sys.stdout.write("<You>") 
#           sys.stdout.write(message) 
#           sys.stdout.flush() 
#server.close()
# 
# 
"""        
import socket 
import select 
import sys 
  
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
if len(sys.argv) != 4: 
    print "Correct usage: script, IP address, port number, Your name"
    exit() 
IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2]) 
server.connect((IP_address, Port)) 
  
while True: 
  
    # maintains a list of possible input streams 
    sockets_list = [sys.stdin, server] 
  
    """ There are two possible input situations. Either the 
    user wants to give  manual input to send to other people, 
    or the server is sending a message  to be printed on the 
    screen. Select returns from sockets_list, the stream that 
    is reader for input. So for example, if the server wants 
    to send a message, then the if condition will hold true 
    below.If the user wants to send a message, the else 
    condition will evaluate as true"""
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 
  
    for socks in read_sockets:  
        if socks == server: 
            message = socks.recv(2048) 
            print message 
        else: 
            message = sys.stdin.readline() 
            server.send(message) 
            sys.stdout.write(sys.argv[3]) 
            sys.stdout.write(": > ") 
            sys.stdout.write(message)
            sys.stdout.flush() 
        print("\nType your message here:")
            
server.close() 