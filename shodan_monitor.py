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