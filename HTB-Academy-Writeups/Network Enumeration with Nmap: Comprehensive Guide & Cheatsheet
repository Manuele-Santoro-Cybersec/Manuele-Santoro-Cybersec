🔍 Network Enumeration with Nmap: Comprehensive Guide & Cheatsheet
Module Status: Completed ✅ | Platform: HTB Academy | Role Focus: SOC Analyst / Penetration Tester

📌 Executive Summary
This document compiles the methodologies, advanced commands, and techniques learned in the "Network Enumeration with Nmap" module. The objective is to document the process of mapping a target's attack surface, from identifying active hosts to discovering specific vulnerabilities using the Nmap Scripting Engine (NSE).

For a SOC Analyst, a deep understanding of Nmap is crucial not only for conducting internal vulnerability assessments but, more importantly, for analyzing network traffic, recognizing attacker scanning patterns, and properly configuring IDS/IPS (Intrusion Detection/Prevention Systems).

🛠️ 1. Host Discovery
Before scanning ports, it is necessary to identify which hosts are alive on the network to avoid generating unnecessary traffic.

Ping Sweep (ICMP Echo Request): Ideal for internal networks where firewalls do not block ICMP. The -sn parameter disables port scanning.

Bash
sudo nmap -sn <SUBNET>
(Example <SUBNET>: 10.129.2.0/24)

Disable Ping (Evasion): If the target blocks ICMP requests (e.g., modern Windows machines or perimeter firewalls), we force Nmap to scan the ports by treating the host as "always alive."

Bash
sudo nmap -Pn <IP_ADDRESS>
🚪 2. Port Scanning Techniques
Once the host is identified, the goal is to determine the state of its ports (Open, Closed, Filtered).

TCP SYN Scan (Stealth Scan - Default with root privileges): Sends only the SYN packet and does not complete the TCP Three-Way Handshake. It is faster and less noisy in application logs.

Bash
sudo nmap -sS -p- <IP_ADDRESS>
TCP Connect Scan (Default without root privileges): Fully completes the TCP handshake. This leaves highly visible traces in the target's logs.

Bash
nmap -sT -p 22,80,443 <IP_ADDRESS>
UDP Scan: Essential for discovering crucial services like DNS (53), SNMP (161), or TFTP (69), although it is slower and less reliable due to the "stateless" nature of UDP.

Bash
sudo nmap -sU -p 53,161 --max-retries 1 <IP_ADDRESS>
🧬 3. Service & OS Enumeration
Knowing open ports is not enough; an analyst must know exactly what is running behind those ports.

Service Version Detection: Fundamental for identifying outdated software versions. Nmap sends specific probes and compares the responses against its database.

Bash
sudo nmap -sV -p 80,443 <IP_ADDRESS>
OS Detection: Nmap analyzes details like TTL (Time to Live) and TCP window sizes to guess the target operating system.

Bash
sudo nmap -O <IP_ADDRESS>
Aggressive Scan (-A): Combines OS detection, Service Version, default NSE scripts, and traceroute. Note: Very noisy, use with caution in monitored environments.

Bash
sudo nmap -A -p- <IP_ADDRESS>
🤖 4. Nmap Scripting Engine (NSE)
The NSE transforms Nmap from a simple port scanner into a powerful vulnerability assessment tool. The scripts are written in Lua.

Default Scripts Execution: Runs a suite of safe and common scripts.

Bash
sudo nmap -sC -p 80 <IP_ADDRESS>
Vulnerability Search & Exploitation (Vuln Category): Checks if exposed services are affected by known vulnerabilities (CVEs).

Bash
sudo nmap --script vuln -p 445 <IP_ADDRESS>
Specific Enumeration (e.g., SMB): Gathers detailed information on a specific protocol (exposed shares, users, password policies).

Bash
sudo nmap -p 445 --script smb-os-discovery,smb-enum-users <IP_ADDRESS>
⚡ 5. Performance, Output & Evasion
Techniques to speed up the scan, save results for forensic analysis, and bypass basic defenses.

Timing Templates (-T): Controls the scan's aggressiveness (from 0 paranoid to 5 insane). -T4 is the ideal compromise for assessments on reliable networks.

Bash
sudo nmap -p- -T4 <IP_ADDRESS>
Save Output in All Formats (-oA): Produces .nmap (human-readable), .xml (for importing into tools like Metasploit), and .gnmap (grepable, for bash parsing) files.

Bash
sudo nmap -p- -sV -oA target_scan <IP_ADDRESS>
Decoy Scan (Evasion): Hides your real IP address among a flood of fake "decoy" IP addresses.

Bash
sudo nmap -D <FAKE_IP_1>,<FAKE_IP_2>,ME -p 80 <IP_ADDRESS>
💡 SOC Analyst Takeaways (Defensive Perspective)
From a defense and monitoring perspective, recognizing these activities is vital:

TCP Log Analysis: A high volume of SYN packets from the same IP to various ports, without ever completing the handshake (missing the final ACK packet), is a clear indicator of an ongoing SYN Scan. This should trigger alerts on the IDS/SIEM.

Detecting Aggressive Scans: The use of the -sV flag (Version Detection) often causes errors or anomalous strings (Nmap probes) to be logged in web server application logs (e.g., Apache/Nginx access.log).

Mitigation: Implement rate-limiting rules and Portscan Detection on perimeter firewalls or via EDR solutions to dynamically block IPs executing multiple connections to unexpected ports within a short timeframe.
