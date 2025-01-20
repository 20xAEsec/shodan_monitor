import boto3
import json 
import requests 
import time 
import urllib.parse

import credentials # API Key stored here (if storing locally)

# Creates new Network Monitoring group in Shodan Monitor 
# with initial IP address of 8.8.8.8 (Google DNS) - 1 IP required for group creation
# Input: 
    # api_key - Shodan API Key
    # group_name - Desired name of monitoring group to create in Shodan Monitor
# Return Value:
    # Group ID for created group
def create_ip_group(api_key, group_name) :
    url = f'https://api.shodan.io/shodan/alert?key={api_key}'
    payload = {
        "name": group_name,
        "filters": {
        "ip": "8.8.8.8" # placeholder for required value
        }
    }
    time.sleep(1)
    response = requests.post(url, json=payload)

    if __debug__:
        print("create_ip_group status code - " + str(response.status_code) )
    
    # If successful, get and return the Group ID, otherwise return None
    if response.status_code == 200:
        print ("IP group created - " + response.text)
        return response. json()['id']
    else:
        return None

# Delete Shodan Monitor network alert group
# Input: 
    # api_key - Shodan API Key
    # group_id - Group ID to delete
# Return Value:
    # True if deletion is successful
    # False otherwise
def delete_ip_group(api_key, group_id):
    url = f'https://api.shodan.io/shodan/alert/{group_id}?key={api_key}'
    time.sleep(1)
    response = requests.post(url)
    print("group deletion status code" + str(response.status_code) )
    
    # If successful, get and return the Group ID, otherwise return None
    if response.status_code == 200:
        print("IP group deleted - " + response.text)
        return True
    else:
        return False
    
# Resolves for Group ID from given Group Name
# Input:
    # api_key - Shodan API Key 
    # group_name - Group Name to return Group ID for
# Return Value:
    # Group ID of requested Shodan Monitor network alert group
def find_group_by_name(api_key, group_name):
    url = f'https://api.shodan.io/shodan/alert/info?key={api_key}'
    time.sleep(1)
    response = requests.get(url)
    print ("find_group_by_name status code - " + str(response.status_code) )
    if response.status_code == 200:     # if the API request was successful
        try:
            network_alerts = response.json() # Parse the JSON response

            for alert in network_alerts:  # Iterate through the list of network alerts
                if alert['name'] == group_name: # if match is found
                    print(alert['id'])  # Return the 'id' value of the matching network alert
                    return alert['id']
        except Exception as e:
            print(e)
            print(response.text)
            print(response.status_code)
            return None
    else:
        print(f"Error: API request failed with status code {response.status_code}")
        return None



# Adds IP addresses to a Shodan Monitor group
# Input: 
    # api_key - Shodan API Key
    # group_id - Group ID to add IPs to
    # ip_list - List of IP's to add to Shodan Monitor group
# Return Value:
    # True if addition is successful
    # False if not
def add_ips_to_shodan_group(api_key, group_id, ip_list):
    url = f'https://api.shodan. io/shodan/alert/{group_id}?key={api_key}'
    payload = {'ips': ip_list}
    time.sleep(1)
    response = requests.post(url, data=payload)
    # Return True if successful; otherwise False
    if response.status_code == 200:
        print("ips added to shodan group")
        return True
    else:
        print("error adding ips to shodan group")
        return False


# Takes a list of IPs to update a specified Shodan Monitor network alert group with
# Input:
    # api_key - Shodan API Key
    # Shodan Monitor group ID to update
    # List of IP's to update Shodan Monitor group with
# Return Value:  
    # True if IPs added successfully
    # False otherwise
def update_shodan_group_ips(api_key, group_id, update_list):
    group_url = f'https://api.shodan.io/shodan/alert/{group_id}/info?key={api_key}'
    time.sleep (1)
    response = requests.get(group_url)
    #print (group_url)
    # Check if the API request was successful
    if response.status_code == 200:
        ip_list = response. json()["'filters"]["ip"]  # Parse the JSON response; gets IP's in Group

        update_set = set(update_list) # convert to sets for efficient comparisons
        shodan_ip_set = set(ip_list)

        # If there are no new IP's to be added to Shodan; no point moving forward
        if update_set == shodan_ip_set:
            print ("No new IP's to add; Shodan Group up-to-date")
            return True
        
        new_ips = update_set - shodan_ip_set   # determine the new IPs to add
        stale_ips = shodan_ip_set - update_set # and the stale ones to remove
        final_set = shodan_ip_set - stale_ips  # out with the old
        final_set = final_set | new_ips        # and in with the new

        final_list_payload = list(final_set)

        update_url = f'https://api.shodan.io/shodan/alert/{group_id}?key={api_key}' # endpoint to POST new IP list to Shodan Monitor
        payload = {
            "filters": {
            "ip": list (final_set)
            }
        }
        time.sleep(1)
        response = requests.post(update_url, json=payload)

        if response.status_code == 200:
            print ("SUCCESS - Shodan Monitor alert group updated" ) 
            return True
        else:
            print(str(response.status_code) + " - ERROR updating Shodan Monitor alert group")
            print(payload)
            return False


# Updates all groups with the configured notifier to send alerts to
# Input:
    # api_key - Shodan API Key
    # notifier_id - Notifier ID to remove/add to alert (str) - 'custom' or 'email'
    # option - "update" or "delete"
# Return Value:
    # None
    # Result - All groups updated with specified notifier id
def update_all_group_notifiers(api_key, notifier_id, option):
    
    if notifier_id == "custom":
        notifier_id = "<custom-id>"
    if notifier_id == "email":
        notifier_id = "default"

    url = f'https://api.shodan.io/shodan/alert/info?key={api_key}'
    time.sleep(1)
    response = requests.get(url) # get your list of configured alerts

    if response.status_code == 200:
        network_alerts = response.json()
        for alert in network_alerts: # and for each ot your configured alertd
            group_id = alert ['id']
            url = f'https://api.shodan.io/shodan/alert/{group_id}/notifier/{notifier_id}?key={api_key}'
            time.sleep(1)
            if option == "update": 
                response = requests.put(url) # either add the new notifier
                print (response.status_code)
            if option == "delete":
                response = requests.delete (url) # or delete the configured notifier
    else:
        print(f"Error: API request failed with status code {response.status_code}")


# Updates groups with configured notifier to send alerts to
# Input:
    # api_key - Shodan API Key
    # group_id - Group ID to add notifier to
    # notifier_id - Notifier ID to remove/add to alert (str) - 'custom' or 'email'
    # option - "update" or "delete"
# Output:
    # True if added successfully
    # False otherwise
def update_group_notifier(api_key, group_id, notifier_id, option):
    
    if notifier_id == "custom":
        notifier_id = "<custom-id>"
    if notifier_id == "email":
        notifier_id = "default"
    
    url = f'https://api.shodan.io/shodan/alert/{group_id}/notifier/{notifier_id}?key={api_key}'
    time.sleep(1)
    if option == "update":
        response = requests.put(url)
    elif option == "delete":
        response = requests.delete(url)
    
    if response.status_code != 200:
        print(f"Error: API request failed with status code {response.status_code}")
        return False
    else:
        return True

# Returns a Py Dictionary mapping groupName → groupID
# Input: 
    # api_key - Shodan API Key
# Return Value:
    # Python Dict mapping groupName → groupID
def get_group_listing(api_key):
    url = f'https://api.shodan.io/shodan/alert/info?key={api_key}'
    time.sleep(1)
    response = requests.get(url) # get list of configured network alert groups
    result_dict = {}
    if response. status_code == 200:
        network_alerts = response.json ()
        for alert in network_alerts:  # Iterate through the list of network alerts
            group_name = alert['name']
            group_id = alert['id']
            result_dict[group_name] = group_id # and create groupName → group ID mapping

    return result_dict

# Configures built-in Shodan Monitor alerts for a specified group
# Input:
    # group_id - Group ID to add alerts to
# Output:
    # True if alerts added successfully
    # False otherwise
def add_alerts_to_group(api_key, group_id):
    trigger = "new_service,malware,uncommon,open_database,ssl_expired,vulnerable"
    url=f'https://api.shodan.io/shodan/alert/{group_id}/trigger/{trigger}?key={api_key}'
    time.sleep(1)
    response = requests.put(url, headers={'Content-Type': 'application/json'})
    print(response.status_code)
    print(response.json())
    if response.json()["success"] == True:
        print("added alerts to " + str(group_id))
        return True
    else:
        return False
    
group_id = create_ip_group(credentials.API_KEY, "test_group")
add_alerts_to_group(credentials.API_KEY, group_id)