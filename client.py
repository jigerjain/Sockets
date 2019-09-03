import socket

HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))

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
            print("Full Message is:\n")
            print(full_msg)

            
            
