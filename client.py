import socket
import time
TCP_IP = '192.168.20.170'
TCP_PORT = 9001
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
# ext = s.recv(10)
st = time.time()
with open('received_file.mp4', 'wb') as f:
    print('file opened')
    while True:
        #print('receiving data...')
        data = s.recv(BUFFER_SIZE)
        # print('data=%s', (data))
        if not data:
            f.close()
            print('file close()')
            break
        # write data to a file
        f.write(data)

print("time elapsed: ", time.time() - st)

print('Successfully get the file')
s.close()
print('connection closed')
