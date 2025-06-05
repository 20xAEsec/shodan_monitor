import os
import requests

from get_public_ips import scan_network_range

from dotenv import load_dotenv # Load environment variables from .env file
load_dotenv()

# Import the required functions from shodan_monitor.py
from shodan_monitor import (
    create_ip_group,
    find_group_by_name,
    add_ips_to_shodan_group,
    add_alerts_to_group,
)

def get_gateway_ip():
    """
    Retrieves your network's public IP using the api.ipify.org REST API.
    Returns the IP address as a string, or None if the request fails.
    """
    try:
        response = requests.get("https://api.ipify.org?format=json")
        if response.status_code == 200:
            print(f"Public IP obtained: {response.json().get('ip')}")
            return str(response.json().get("ip"))
    except Exception as e:
        print("Failed to obtain public IP:", e)
    return None



def onboard_home_network_to_shodan(group_name="home_network", all_public_devices=False):
    """
    Scans the specified home network range using nmap, identifies live hosts,
    and onboards these IP addresses into a Shodan Monitor group. If the group 
    doesn't exist, it is created. Additionally, built-in alerts are configured.
    
    Parameters:
        group_name (str): Desired name for the Shodan Monitor group.
        all_public_devices (bool): If True, scans for additional public-facing IPs within a given internal subnet range.
    """

    onboard_ips = []
    gateway_ip = get_gateway_ip()
    if not gateway_ip:
        print("Failed to retrieve public IP address.")
        return
    else:
        onboard_ips.append(gateway_ip)

    if all_public_devices:
        from get_public_ips import scan_network_range # lazy import 
        start_range = input("Enter the starting subnet number (192.168.x.0/24) : ")
        end_range = input("Enter the ending subnet number (192.168.y.0/24) : ")
        print(f"Scanning network range 192.168.{start_range}.0/24 to 192.168.{end_range}.0/24 ...")
        public_hosts = scan_network_range(filter_public=True, range_start=int(start_range), range_end=int(end_range))
        if public_hosts:
            print("\nActive public devices found:")
            for ip in public_hosts:
                print(f" - {ip}")

            if len(public_hosts) > 0:
                for ip in public_hosts:
                    onboard_ips.append(ip)
                

        else:
            print("\nNo active public devices detected in the scanned range.")
        
    # Use the stored API key from your credentials module
    api_key = os.getenv("SHODAN_API_KEY")

    # Try to find an existing group with the given name
    group_id = find_group_by_name(api_key, group_name)
    if group_id is None:
        print(f"Group '{group_name}' not found. Creating a new group.")
        group_id = create_ip_group(api_key, group_name)
        if group_id is None:
            print("Failed to create Shodan Monitor group. Exiting.")
            return
    else:
        print(f"Using existing group '{group_name}' with ID: {group_id}")
    
    # Onboard the live IP addresses to the Shodan Monitor group
    if add_ips_to_shodan_group(api_key, group_id, onboard_ips):
        print("Successfully onboarded IPs to Shodan Monitor.")
    else:
        print("Error: Failed to onboard IPs to Shodan Monitor.")
        return
    
    # Optionally, configure built-in alerts for the group
    if add_alerts_to_group(api_key, group_id):
        print("Alerts successfully configured for the group.")
    else:
        print("Warning: Failed to configure alerts for the group.")

# Example usage:
if __name__ == "__main__":
    onboard_home_network_to_shodan(group_name="Home Network", all_public_devices=True) # set to False to skip network scan and only onboard gateway/router IP address

   


