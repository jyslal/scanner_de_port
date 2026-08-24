import socket
import ipaddress
import argparse
import time
import subprocess

def arg_gestion():
    # Section récuperation des arguments
    parser = argparse.ArgumentParser(description="Ceci est le parser de ce script")
    parser.add_argument("-c", "--cible", type= str, default="127.0.0.1")
    parser.add_argument("-p", "--port", nargs= "+", type= int)
    parser.add_argument("-pi", "--ping", action="store_true")
    args = parser.parse_args() #création de l'objet args
    port = args.port
    cible = args.cible
    ping = args.ping

    # retour des valeurs
    return cible, port, ping


def scanner_port(cible, port):
    print("[Début du scan...]\n")
    if type(port) == list:
        for i in port:
                try:
                    socket_prog = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    socket_prog.settimeout(0.1)
                    if socket_prog.connect_ex((cible, i)) == 0:
                        print(f"->{i}/tcp {socket.getservbyport(i, 'tcp')}: OPEN")
                    else:
                        print(f"->{i}/tcp {socket.getservbyport(i, 'tcp')}: CLOSE/FILTRED")    
                    
                    socket_prog.close()
                except OSError:
                     continue                
    else:
        nbre_port_open = 0
        for i in range(1, 1024):
                        try:
                            socket_prog = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            socket_prog.settimeout(0.1)
                            if socket_prog.connect_ex((cible, i)) == 0:
                                print(f"->{i}/tcp {socket.getservbyport(i, 'tcp')}: OPEN")
                                nbre_port_open += 1
                            socket_prog.close()
                        except OSError:
                            continue
        if nbre_port_open == 0:
            print("Aucun port ouvert détecté!")
    

def connectivite(cible):
    reachable = False
    #for c in  cible:
    ping = subprocess.run(["ping", "-c", "4", cible], stdout= subprocess.DEVNULL, stderr= subprocess.DEVNULL)
    if ping.returncode == 0:
        print("L'hôte est joignable par ping\n")
    else:
        print("L'hôte est injoingable par ping veuillez vérifiez")


def main():
    cible, port, ping = arg_gestion()
    if ping:
        connectivite(cible)
    try:
        debut = time.perf_counter()
        ipaddress.ip_address(cible)
        #if connectivite(cible) == True:
        scanner_port(cible, port)
        fin = time.perf_counter()
        print(f"\n[Fin du scan...] \nTime -> {fin - debut:.2f} (s) ")
        #else:
        #print("[Unreachable hote] - Veuillez vérifiez que l'hôte existe bien ou que vous êtes bien connecté au même réseau ou encore qu'il n'a pas de parefeu activé ")
    except ValueError:
          print("Addresse invalide!")

          return
    

if __name__ == '__main__':
    main()
