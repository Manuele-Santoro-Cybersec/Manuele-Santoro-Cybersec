# Hack The Box: Starting Point (Tier 0) Summary

## 🎯 Overview
This document summarizes the foundational labs completed in the HTB Starting Point Tier 0. These labs focus on basic network enumeration and the identification of insecure legacy protocols.

---

## 🐱 Machine: Meow
* **Protocol Focus:** Telnet (Port 23)
* **Key Learning:** Remote access via unencrypted protocols.

### 🔍 Technical Analysis
I used `nmap` to identify Port 23 (Telnet) as open. I was able to gain access using a common default credential (`root`) with no password.

### 🛡️ SOC Analyst Perspective
* **Risk:** Telnet transmits all data, including credentials, in **cleartext**. An attacker on the same network could use a sniffer (like Wireshark) to steal admin passwords.
* **Remediation:** Disable Telnet immediately. Replace with **SSH (Port 22)**, which uses encryption to protect data in transit.

---

## 🦌 Machine: Fawn
* **Protocol Focus:** FTP (Port 21)
* **Key Learning:** Misconfigured file transfer services.

### 🔍 Technical Analysis
Enumeration revealed an FTP service allowing **Anonymous** login. This configuration error permitted me to log in without a specific user account and download sensitive files from the server.

### 🛡️ SOC Analyst Perspective
* **Risk:** Anonymous FTP is a major source of **Information Disclosure**. Attackers often scan for this to exfiltrate internal documentation or configuration files.
* **Remediation:** Disable anonymous access. Require strong authentication for all FTP users or move to **SFTP** for encrypted file transfers.

---

## 📈 Skills Demonstrated
* **Network Enumeration:** Using `nmap` to discover open ports and services.
* **Protocol Analysis:** Understanding the inherent risks of legacy protocols (Telnet, FTP).
* **Risk Communication:** Identifying vulnerabilities and proposing industry-standard remediations.

*Completed as part of the Junior Cybersecurity Analyst path.*
