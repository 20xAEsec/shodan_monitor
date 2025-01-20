# shodan_monitor
Python wrapper library for the Shodan Monitor API


## Description
This product enables monitoring and alerting capabilities on public-facing endpoints via Shodan Monitor. The goal of this library is to enable real-time updates on potential vulnerabilities and misconfigurations affecting your publicly-facing networking products.

By instantly getting actionable alerts about security misconfigurations, vulnerable services, open databases, and more to network owners and administrators, we reduce the time to remediation on vulnerabilities affecting the devices which make up our attack surface.

### shodan-monitor.py
wrapper library for simple interaction with the Shodan API to create and update monitoring groups in Shodan Monitor.
Cloud resources and public-facing internal network devices (firewalls etc) can be identified and grouped via Sentinel/Opensearch queries, and then loaded into Shodan Monitor to enable alerting on a number of misconfigurations malware, vulnerable services and more as described in the linked documentation. These alerts can then be sent to the resource owners Scorecard product for remediation.

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
### Alerts
Alert Name	Description
end_of_life	Triggered when Shodan Monitor detects devices or software that are no longer supported by the vendor, posing a significant security risk as the device may no longer receive critical patches or firmware updates.
industrial_control_system	Triggered when Shodan Monitor detects devices or software that control and monitor industrial processes, such as manufacturing lines, which attackers can potentially exploit to gain unauthorized access or disrupt physical processes.
internet_scanner	Triggered when Shodan Monitor detects network reconnaissance activities, such as scanning for open ports, that are often precursors to more targeted attacks.
iot	Triggered when Shodan Monitor detects the presence of Internet of Things (loT) devices, such as smart home devices, which attackers can potentially exploit to gain access to or disrupt your network.
malware	Triggered when Shodan Monitor detects malware activity on a device, domain or service.
new_service	Triggered when Shodan Monitor detects a new service being offered, such as new webserver, database, or email, that was not previously available to the internet.
open_database	Triggered when Shodan Monitor detects an open database that is not protected by a password or firewall.
ssl_expired	Triggered when Shodan Monitor detects SSL or LS certificates that have expired or are soon to expire, which can lead to security vulnerabilities in your web-based applications and services.
uncommon	Triggered when Shodan Monitor detects a device or system with an unusual configuration or usage pattern.
uncommon_plus	Similar to the uncommon alert, however, uncommon_plus is triggered when Shodan Monitor detects a device or system with an even more unusual configuration.
vulnerable	Triggered when Shodan Monitor detects a device, system, or service with known vulnerabilities that can be exploited by attackers to gain unauthorized access or cause disruption to the network or system.
