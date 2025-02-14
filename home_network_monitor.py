import os
import requests
from dotenv import load_dotenv # Load environment variables from .env file
load_dotenv()

# Import the required functions from shodan_monitor.py
from shodan_monitor import (
    create_ip_group,
    find_group_by_name,
    add_ip_to_shodan_group,
    add_alerts_to_group,
)

def get_public_ip():
    """
    Retrieves the public IP address of the current network by querying an external service.
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



def onboard_home_network_to_shodan(group_name="home_network"):
    """
    Scans the specified home network range using nmap, identifies live hosts,
    and onboards these IP addresses into a Shodan Monitor group. If the group 
    doesn't exist, it is created. Additionally, built-in alerts are configured.
    
    Parameters:
        group_name (str): Desired name for the Shodan Monitor group.
        network_range (str): CIDR notation for the network range to scan.
    """
    gateway_ip = get_public_ip()
    if not gateway_ip:
        print("Failed to retrieve public IP address.")
        return

    
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
    if add_ip_to_shodan_group(api_key, group_id, gateway_ip):
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
    onboard_home_network_to_shodan(group_name="Home Network")
