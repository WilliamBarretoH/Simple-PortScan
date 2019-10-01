import socket

#scanning from port 1 to 1025
for port in range(1, 1025):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex(("192.168.0.1", port))
    if 0 == result:
        print("Port: {} Open".format(port))
    sock.close()
