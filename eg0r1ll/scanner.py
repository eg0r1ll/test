import socket
import platform
import subprocess 
import time

def get_ips(ips, ports):
    ping_parametr = "-n" if platform.system().lower() == "windows" else "-c"
    
    if len(ips) == 3:
        main_ip = ips[0]

        for i in range(int(ips[1]), int(ips[2]) + 1):
            timer = time.perf_counter()
            temp_ip = main_ip + str(i)
            command = ["ping", ping_parametr, "1", temp_ip]
            print(f"scan ip: {temp_ip}")
            response = subprocess.run(command, stdout=subprocess.PIPE).returncode == 0

            if response:
                print("response: OK")
                open_ports = scan_ports(ports, temp_ip)
                print(temp_ip, open_ports, round(time.perf_counter() - timer, 3))
                print()
            else:
                print("response: NO\n")

    elif len(ips) == 1:
        timer = time.perf_counter()
        command = ["ping", ping_parametr, "1", ips[0]]
        response = subprocess.run(command, stdout=subprocess.PIPE).returncode == 0

        if response:
            print("response: OK")
            ports = scan_ports(ports, ips[0])
            print(ips[0], ports, round(time.perf_counter() - timer, 3))
            print()
        else:
            print("response: NO\n")


def scan_ports(ports, temp_ip):
    result = []
    if len(ports) == 2: 
        for port in range(int(ports[0]), int(ports[1]) + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                try_connect = sock.connect_ex((temp_ip, port))
                if try_connect == 0:
                    print(f"{temp_ip}:{port} OPEN")
                    result.append(port)
                print(f"{temp_ip}:{port} CLOSE")

    elif len(ports) == 1:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            try_connect = sock.connect_ex((temp_ip, ports[0]))

            if try_connect == 0:
                print(f"{temp_ip}:{ports[0]} OPEN")
                result.append(ports[0])
            print(f"{temp_ip}:{ports[0]} CLOSE")
            
    return result

def main():

    diap_ip = input("ip or diaposon(x.x.x. start end): ").split() # 192.168.0.1 / 192.168.0. 0 255
    diap_port = input("port os diaposon(end start): ").split() # 100 / 10 50
    
    if len(diap_port) == 2 or len(diap_port) == 1 and len(diap_ip) == 1 or len(diap_ip) == 3:
        print(diap_ip, diap_port)
        get_ips(diap_ip, diap_port)


if __name__ == "__main__":
    main()
