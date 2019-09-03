import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)

msg = "How are you doing you my friend"
msg_w_header=f"{len(msg):<{HEADERSIZE}}"+msg

while True:
    client_conn, addr = s.accept()
    print("Connection from {} accepted!".format(addr))
    client_conn.send(bytes(msg_w_header,"utf-8"))