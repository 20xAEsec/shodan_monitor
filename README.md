# shodan_monitor
Python wrapper library for the Shodan Monitor REST API


## Description
This product enables monitoring and alerting capabilities on public-facing endpoints via Shodan Monitor. The goal of this library is to enable real-time updates on potential vulnerabilities and misconfigurations affecting your publicly-facing networking products.

By instantly getting actionable alerts about security misconfigurations, vulnerable services, open databases, and more to network owners/admins, you will reduce the TTR on vulnerabilities affecting the devices on your network perimeter.


### Installation

To install the gitleaks pre-commit hook and prevent your secret from being pushed,  
install the pre-commit hook by running these commands at the repo root.  
This will run GitLeaks against every commit, and block your commit if your changes contain hard-coded credentials.

```bash
pip install pre-commit
pre-commit install
```

To install all the required dependencies, clone the repository, install the dependencies, and execute ```home_network_monitor.py```

```bash
git clone https://github.com/20xAEsec/shodan_monitor.git
cd shodan_monitor
pip install -r requirements.txt
```
To onboard your home network using the script, execute the following command:
```bash
python3 home_network_monitor.py
```

### shodan-monitor.py
wrapper library for simple interaction with the Shodan API to create and update monitoring groups in Shodan Monitor.
Cloud resources and public-facing internal network devices (firewalls etc) can be identified and grouped via SIEM queries, and then loaded into Shodan Monitor to enable alerting on a number of misconfigurations malware, vulnerable services and more as described in the documentation.

#### Real-time monitoring
Shodan Monitor offers users real-time monitoring capabilities with customizable alerts. 
#### Granular search
Shodan Monitor's search algorithm allows users to specify a wide range of device parameters, including IP addresses, domains, and service ports, to customize their search for connected devices.
#### Customizable criteria
Users can create their customized criteria to enable the Shodan Monitor to focus on specific devices, services, or regions.
#### Historical analysis
Monitor provides a history of device activity, with data kept up to 14 months based on the selected subscription. The historical data allows for verification of new anomalies in broader contexts, making it possible to track long-term developments.
#### API Integrations
Monitor provides APls for integrating with other security management tools to feed systems with intelligence using real-time monitoring and event triggers.

# Home Network Onboarding to Shodan Monitor

This Python script automates the process of onboarding your home network's public IP address into a Shodan Monitor group. It retrieves your network's public IP, creates or locates an existing Shodan Monitor group, adds your IP to that group, and configures built-in alert triggers—all while leveraging environment variables for secure API key management.

## Overview

The script performs the following tasks:

1. **Load Environment Variables:**  
   Uses the `python-dotenv` package to load environment variables from a `.env` file. Make sure your `.env` file contains your Shodan API key (e.g., `SHODAN_API_KEY=your_api_key`).

2. **Retrieve Public IP:**  
   Calls an external service (ipify) to obtain the public IP address of your network. This IP represents the outward-facing gateway of your internal network.
      - Additionally, if `all_public_devices=True`, an ```nmap``` scan is performed to search for devices with public IP addresses on your network to be onboarded.

4. **Manage Shodan Monitor Group:**  
   - **Find Group:** Attempts to find an existing Shodan Monitor group by name.
   - **Create Group:** If no matching group is found, a new group is created.
   - **Onboard IP:** The retrieved public IP is then onboarded into the group.
   - **Configure Alerts:** Built-in alert triggers are configured for the group to monitor for specific events.

5. **Example Usage:**  
   When executed as the main script, it will run the onboarding process with the group name "Home Network".

### Alerts
| Alert Name              | Description                                                                                                                                                      |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| end_of_life            | Triggered when Shodan Monitor detects devices or software that are no longer supported by the vendor, posing a significant security risk as the device may no longer receive critical patches or firmware updates. |
| industrial_control_system | Triggered when Shodan Monitor detects devices or software that control and monitor industrial processes, such as manufacturing lines, which attackers can potentially exploit to gain unauthorized access or disrupt physical processes. |
| internet_scanner       | Triggered when Shodan Monitor detects network reconnaissance activities, such as scanning for open ports, that are often precursors to more targeted attacks.      |
| iot                   | Triggered when Shodan Monitor detects the presence of Internet of Things (IoT) devices, such as smart home devices, which attackers can potentially exploit to gain access to or disrupt your network. |
| malware               | Triggered when Shodan Monitor detects malware activity on a device, domain or service.                                                                           |
| new_service           | Triggered when Shodan Monitor detects a new service being offered, such as a new webserver, database, or email, that was not previously available to the internet. |
| open_database         | Triggered when Shodan Monitor detects an open database that is not protected by a password or firewall.                                                          |
| ssl_expired           | Triggered when Shodan Monitor detects SSL or TLS certificates that have expired or are soon to expire, which can lead to security vulnerabilities in your web-based applications and services. |
| uncommon              | Triggered when Shodan Monitor detects a device or system with an unusual configuration or usage pattern.                                                         |
| uncommon_plus         | Similar to the uncommon alert, however, uncommon_plus is triggered when Shodan Monitor detects a device or system with an even more unusual configuration.        |
| vulnerable            | Triggered when Shodan Monitor detects a device, system, or service with known vulnerabilities that can be exploited by attackers to gain unauthorized access or cause disruption to the network or system. |


## Requirements

This project relies on the following Python packages, each pinned to a specific version to ensure compatibility and stability. Make sure to install these dependencies exactly as specified:

- **certifi (2025.1.31):**  
  Provides Mozilla's CA Bundle, ensuring that SSL certificates used in HTTPS connections are validated properly for secure communication.

- **charset-normalizer (3.4.1):**  
  A tool for detecting and normalizing character encodings. It ensures that text data is correctly interpreted across various formats.

- **idna (3.10):**  
  Implements support for Internationalized Domain Names (IDN), enabling the correct handling of non-ASCII domain names.

- **python-dotenv (1.0.1):**  
  Loads environment variables from a `.env` file into your application's environment. This helps manage configuration and sensitive information (e.g., API keys) securely.

- **python-nmap (0.7.1):**  
  A Python wrapper for the Nmap tool, allowing you to perform network scans and discover devices on your network programmatically.

- **requests (2.32.3):**  
  A user-friendly HTTP library for Python, used to make API calls and interact with web services easily.

- **urllib3 (2.3.0):**  
  A powerful, low-level HTTP client library that underpins the Requests library. It handles the core aspects of HTTP communication and connection pooling.
