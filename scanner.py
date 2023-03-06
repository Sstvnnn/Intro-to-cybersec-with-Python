import argparse
import socket

def scan_port(host, port):
    try:
        # Create a new socket/ host-port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Internet, Pertukaran Data
        
        # Set a timeout of 1 second
        sock.settimeout(1)
        
        # Connect to the host and port
        connection = sock.connect_ex((host,port))
        # Check if the port is open
        if connection != 0 :
            print(f"Port {port} is open")
        else :
            print(f"Port {port} is closed")
        # Close the socket
        sock.close()
    
    except socket.error:
        print(f"Port {port} is closed")

def scan_host(host, ports):
    # Loop through the list of ports and scan each one
    for port in ports:
        scan_port(host,port)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Port Scanner")
    parser.add_argument("host", help="Host to scan")
    #parser.add_argument("ports", help="Ports to scan (comma-separated)")
    args = parser.parse_args()

    host = args.host
    #ports from file
    #with open 
    file_name = input("Enter File Name : ")
    try :
        with open(f"{file_name}.txt", 'r') as f :
            ports = f.read()
            ports = ports.split("\n")
    except FileNotFoundError :
        print("There's no file")
        with open(f"{file_name}.txt", 'w') as f:
            port_list = input("Input ports : ")
            ports = port_list.split(",")
            test = '\n'.join(str(i)for i in ports)
            f.write(test)
    ports = [int(port) for port in ports] # args.ports = string

    scan_host(host, ports)



