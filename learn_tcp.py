

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Connecting 163.com...')
s.connect(('www.liaoxuefeng.com', 80))

print('Send GET request...')
s.send(b'GET / HTTP/1.1\r\nHost: www.liaoxuefeng.com\r\nConnection: close\r\n\r\n')

buffer = []

print('Receiving data...')
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = b''.join(buffer)

s.close()

print('Printing...')
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))

with open('python.html', 'wb') as f:
    f.write(html)

