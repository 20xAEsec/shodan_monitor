# shodan_monitor
Python wrapper library for the Shodan Monitor REST API


## Description
This product enables monitoring and alerting capabilities on public-facing endpoints via Shodan Monitor. The goal of this library is to enable real-time updates on potential vulnerabilities and misconfigurations affecting your publicly-facing networking products.

By instantly getting actionable alerts about security misconfigurations, vulnerable services, open databases, and more to network owners/admins, you will reduce the TTR on vulnerabilities affecting the devices on your network perimeter.


### Installation

#### GitLeaks pre-commit hook
To install the gitleaks pre-commit hook and prevent your secret from being pushed,  
install the pre-commit hook by running these commands at the repo root.  
This will run GitLeaks against every commit, and block your commit if your changes contain hard-coded credentials.

```bash
pip install pre-commit
pre-commit install
```

If you try to commit a hard-coded secret, you will be blocked with the following message.  

```bash
[WARNING] Gitleaks detected hardcoded secrets. Commit aborted.
```  
Be sure to use proper secrets management to commit to this project.

#### Shodan Monitor Installation

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

This project relies on the following Python packages, each pinned to a specifi c version to ensure compatibility and stability. Make sure to install these dependencies exactly as specified:

- **boto3 (1.38.30)**: AWS SDK for Python to interact with AWS services.
- **botocore (1.38.30)**: Core functionality used by boto3 for making AWS API calls.
- **certifi (2025.1.31)**: Provides SSL certificates for secure HTTP requests.
- **cfgv (3.4.0)**: Validates configuration and settings files.
- **charset-normalizer (3.4.1)**: Detects and normalizes text encoding for HTTP responses.
- **distlib (0.3.9)**: Supports packaging and distribution of Python software.
- **filelock (3.18.0)**: Offers file locking to prevent concurrent access issues.
- **identify (2.6.12)**: Detects file types and properties, commonly used by git hooks.
- **idna (3.10)**: Handles internationalized domain names in URLs.
- **jmespath (1.0.1)**: Queries JSON data structures efficiently.
- **nodeenv (1.9.1)**: Manages isolated Node.js environments.
- **platformdirs (4.3.8)**: Provides standardized paths for application data.
- **pre_commit (4.2.0)**: Framework to manage and execute git pre-commit hooks.
- **python-dateutil (2.9.0.post0)**: Utilities for parsing and manipulating dates and times.
- **python-dotenv (1.0.1)**: Loads environment variables from `.env` files.
- **python-nmap (0.7.1)**: Enables network scanning and host discovery with nmap.
- **PyYAML (6.0.2)**: Parses and serializes YAML files.
- **requests (2.32.3)**: Simplifies HTTP requests to APIs and web services.
- **s3transfer (0.13.0)**: Provides managed transfers of files to and from AWS S3.
- **six (1.17.0)**: Ensures compatibility between Python 2 and Python 3.
- **urllib3 (2.3.0)**: Performs robust HTTP client operations and connection pooling.
- **virtualenv (20.31.2)**: Creates isolated Python environments.
