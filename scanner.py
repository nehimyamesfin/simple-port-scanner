import socket

target = "example.com"  # here i used a random website as a target, but u can use any other website as an input or ip addresses
total_open_port = 0

for port in range(1, 65535):  # this will scan all ports from 1 to 65535
    s = socket.socket()
    s.settimeout(0.5)   # u can set the time as u want for increased scanning speed
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
        total_open_port = total_open_port + 1
    s.close()

print(f"Scan completed! {total_open_port} port are open.")
