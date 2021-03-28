import cv2
import io
import socket
import struct
import time
import pickle
import zlib
import numpy as np


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('0.tcp.ngrok.io', 19194))
# client_socket.connect(('10.18.15.41', 8485))
connection = client_socket.makefile('wb')

cam = cv2.VideoCapture(0)

# cam.set(3, 128)
# cam.set(4, 128)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280.0)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720.0)

img_counter = 0

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
print(encode_param)

while True:
    ret, frame = cam.read()
    result, frame = cv2.imencode('.jpg', frame, encode_param)
#    data = zlib.compress(pickle.dumps(frame, 0))
    # frame=frame[:,::-1,:]
    data = pickle.dumps(frame, 0)
    size = len(data)


    # print("{}: {}".format(img_counter, size))
    if img_counter%10==0:
        client_socket.sendall(struct.pack(">L", size) + data)
        # response = client_socket.recv(1024).decode()
        # print(response)
        # cv2.imshow('ImageWindow',response)
        # cv2.waitKey(1)
        # print(response)
    img_counter += 1
    # print(img_counter)
    

cam.release()