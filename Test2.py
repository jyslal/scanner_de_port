import socket
import ipaddress
import argparse

def main():
    parser = argparse.ArgumentParser(description="ceci est un test")
    parser.add_argument("-c", "--cible", type=str, default="127.0.0.1")
    parser.add_argument("-p", "--port", type=int, nargs="+")
    args = parser.parse_args()
    port = args.port
    ip_add = args.cible
    if not port:
        while True: 
            try:
                ipaddress.ip_address(ip_add) 
                break
            except ValueError:
                ip_add = input("veuillez entrer un cible valide")

        for i in range(1,1000):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#créer un socket
                s.settimeout(0.2)#temp avant déconnexion
                if s.connect_ex((ip_add, i)) == 0: #essayer de ce connecter une ip avoir tel port
                    print(f"{i}/tcp - {socket.getservbyport(i, 'tcp')}")# getservbyport = tu obtient un service précis en fonction du port
                s.close()#ferme le socket
            except OSError:
                continue
    else:
        for n in port:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#créer un socket
                s.settimeout(0.2)#temp avant déconnexion
                if s.connect_ex((ip_add, n)) == 0: #essayer de ce connecter une ip avoir tel port
                    print(f"{n}/tcp - {socket.getservbyport(n, 'tcp')}")# getservbyport = tu obtient un service précis en fonction du port
                s.close()#ferme le socket
            except OSError:
                continue

#hostname = socket.gethostname()
#ip = socket.gethostbyname(hostname)
#print(f'Hostname: {hostname}')
#print(f'IP: {ip}')
#https://www.w3schools.com/python/ref_module_socket.asp