import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 7000))

while True:
    data, addr = sock.recvfrom(1024)
    print(f"received message: {data} from {addr}")
