import socket
import sys

import numpy as np
import cv2
import struct


def send_msg(sock, msg):
    # Prefix each message with a 4-byte length (network byte order)
    msg = struct.pack('>I', len(msg)) + msg
    sock.sendall(msg)


def recv_msg(sock):
    # Read message length and unpack it into an integer
    raw_msglen = recvall(sock, 4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    # Read the message data
    print(msglen)
    return recvall(sock, msglen)


def recvall(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = b''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data


def map_with_remote_frames(mapping):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
            client_ip = input("Client ip: ")
            s2.connect((client_ip, 4000))
            server_ip = input("Server ip: ")
            s.bind((server_ip, 5000))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = recv_msg(conn)
                    nparr = np.fromstring(data, np.uint8)
                    img = cv2.imdecode(nparr, 1)

                    # ---- Do stuff with img
                    # imagem = cv2.bitwise_not(img)
                    imagem = mapping.detect(img)
                    # ----

                    img_str = cv2.imencode('.jpg', imagem)[1].tostring()
                    send_msg(s2, img_str)
