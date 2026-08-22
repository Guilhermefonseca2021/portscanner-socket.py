import socket
# import termcolor

def scan(target, ports):
    print("\n" + "Starting Scan for " + str(target))
    for port in range(1, ports):
        scan_ports(targets, port)

def scan_ports(ip_target, port):
    try:
        sock = socket.socket()
        sock.connect((ip_target, port))
        print("[+] Port Opened " + str(port))
        sock.close()
    except:
        pass
        # print("[-] Port closed " + str(port))


targets = input("[*] Enter Target To Scan: ")
ports = int(input("[*] Enter how many ports you want to scan: "))
#
# ==============================
#
if ',' in targets:
    print("[*] Scanning multiple targets")
    for ip_address in targets.split(','):
        scan(ip_address(''), ports)
else:
    scan(targets, ports)
