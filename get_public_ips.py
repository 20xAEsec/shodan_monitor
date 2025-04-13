import nmap
import ipaddress

def scan_network_range(filter_public=True, range_start=0, range_end=10):
    """
    - Scans each /24 subnet from 192.168.0.0/24 to 192.168.10.0/24 (default) and returns a list of IP addresses
    that are up. Optionally, it filters the results to include only publicly routable IP addresses.
    
    - Range values can be adjusted to scan a different range of subnets.
    
    Parameters:
        filter_public (bool): If True, only include hosts whose IP is not in a private range.
                              (Note: 192.168.x.x addresses are private, so this will usually return an empty list.)
        range_start (int): Starting subnet number for scanning (192.168.x.0/24)
        range_end (int): Ending subnet number (0-10) for scanning. (192.168.x.0/24)
    
    Returns:
        list: A list of active IP addresses (as strings) from the specified range.
    """
    active_hosts = []
    scanner = nmap.PortScanner()
    
    # Loop through subnets 192.168.0.0/24 to 192.168.10.0/24
    for subnet in range(range_start, range_end):
        network_range = f"192.168.{subnet}.0/24"
        print(f"Scanning network {network_range} ...")
        scanner.scan(hosts=network_range, arguments="-sn -T5")
        
        for host in scanner.all_hosts():
            if scanner[host].state() == "up":
                # If filtering for public IPs, only include if the IP is not private.
                # Note: In a 192.168.x.x network, all addresses are private.
                if filter_public:
                    try:
                        if not ipaddress.ip_address(host).is_private:
                            active_hosts.append(host)
                    except ValueError as e:
                        print(f"Skipping invalid IP {host}: {e}")
                else:
                    active_hosts.append(host)
    
    return active_hosts

if __name__ == "__main__":
    # Set filter_public=False if you want all active devices even if they have private addresses.
    public_only = True
    results = scan_network_range(filter_public=public_only)
    
    if results:
        print("\nActive (and publicly routable, if filtered) devices found:")
        for ip in results:
            print(f" - {ip}")
    else:
        if public_only:
            print("\nNo publicly routable devices detected in the scanned range (expected for private 192.168.x.x addresses).")
        else:
            print("\nNo active devices detected in the scanned range.")
