import socket

def scan_ports(target, ports=range(1, 1025)):
    print(f"[INFO] Scanning {target} for open ports...")
    for port in ports:
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((target, port))
            print(f"[OPEN] Port {port} is open.")
            s.close()
        except:
            continue
