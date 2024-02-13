import argparse
import socket
import threading
import time
import re

# Dictionary mapping common port numbers to their respective service names
COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    5432: "PostgreSQL",
    8080: "HTTP Proxy",
    # Add more port numbers and service names as needed
}

def scan_port(host, port, timeout, verbose=False):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))
            if result == 0:
                service_name = COMMON_PORTS.get(port, "Unknown")
                if verbose:
                    print(f"Port {port} ({service_name}) is open")
                return port
            else:
                if verbose:
                    print(f"Port {port} is closed")
    except Exception as e:
        if verbose:
            print(f"Error scanning port {port}: {e}")
    return None

def scan_ports(host, ports, timeout, num_threads, verbose=False):
    open_ports = []
    lock = threading.Lock()

    if len(ports) < 2:
        raise ValueError("Port list must contain at least two elements.")

    def scan_range(start, end):
        nonlocal open_ports
        for port in range(start, end):
            result = scan_port(host, port, timeout, verbose)
            if result:
                with lock:
                    open_ports.append(result)

    # Split ports into ranges for multi-threaded scanning
    port_ranges = [(ports[i], ports[i + 1]) for i in range(0, len(ports), 2)]

    # Create and start threads
    threads = []
    for start, end in port_ranges:
        thread = threading.Thread(target=scan_range, args=(start, end))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    return open_ports

def main():
    print("Welcome to the Simple Port Scanner!")
    print("This tool allows you to perform port scanning on a target host.")

    parser = argparse.ArgumentParser(description="Advanced Port Scanner")
    parser.add_argument("-H", "--host", help="Target IP address or hostname")
    parser.add_argument("-p", "--ports", default="1-1024", help="Port range to scan (default: 1-1024)")
    parser.add_argument("-t", "--targets", help="File containing target IP addresses")
    parser.add_argument("-T", "--timeout", type=float, default=1, help="Timeout for port connection (default: 1 second)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    host = args.host
    timeout = args.timeout
    verbose = args.verbose

    # Parse port range
    try:
        ports = parse_ports(args.ports)
    except ValueError as e:
        print(f"Error parsing port range: {e}")
        return

    # Perform port scanning
    start_time = time.time()
    
    if args.targets:
        try:
            with open(args.targets) as file:
                for line in file:
                    target_host = line.strip()
                    open_ports = scan_ports(target_host, ports, timeout, num_threads, verbose)
                    display_results(target_host, open_ports)
        except FileNotFoundError:
            print("File not found.")
            return
    else:
        if not host:
            print("Please specify a target host using the -H option or a file containing target IP addresses using the -t option.")
            return
        open_ports = scan_ports(host, ports, timeout, num_threads, verbose)
        display_results(host, open_ports)

    end_time = time.time()
    print(f"\nScan completed in {end_time - start_time:.2f} seconds")

def parse_ports(port_str):
    port_ranges = []

    # Regular expression to match port range formats
    pattern = re.compile(r'(\d+)(?:-(\d+))?')

    # Split port_str by comma and iterate over each part
    for part in port_str.split(','):
        match = pattern.match(part)
        if match:
            start = int(match.group(1))
            end = int(match.group(2)) if match.group(2) else start
            port_ranges.append((start, end))
        else:
            raise ValueError(f"Invalid port range format: {part}")

    # Convert port_ranges to a flat list of ports
    ports = []
    for start, end in port_ranges:
        ports.extend(range(start, end + 1))

    return ports

def display_results(host, open_ports):
    if open_ports:
        print(f"\nOpen ports on {host}:")
        for port in open_ports:
            service_name = COMMON_PORTS.get(port, "Unknown")
            print(f"    Port {port} ({service_name}) is open")
    else:
        print(f"\nNo open ports found on {host}")

if __name__ == "__main__":
    main()
