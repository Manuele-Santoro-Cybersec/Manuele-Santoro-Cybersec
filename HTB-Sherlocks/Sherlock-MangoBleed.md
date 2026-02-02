# HTB Sherlock: MangoBleed - Incident Response Report
**Case:** High-Priority Server Compromise Analysis
**Host:** mongodbsync (Secondary MongoDB Server)
**Methodology:** Rapid Triage Analysis (UAC Artifacts)

## 🛡️ Incident Overview
Early this morning, an investigation was launched into `mongodbsync` following reports of a potential compromise via the **"MongoBleed"** vulnerability. Using root-level triage data, I performed a forensic reconstruction of the attacker's activities.

## 🔍 Step-by-Step Investigation

### 1. Vulnerability Research (CVE Identification)
Based on the "MongoBleed" reference, I identified the associated **CVE ID**. This vulnerability allows for unauthorized memory disclosure or information leakage from the MongoDB process, often leading to credential theft.

### 2. Service & Version Verification
By analyzing the triage logs, I confirmed the running version of MongoDB. This verified the server's susceptibility to the MongoBleed exploit, confirming the initial attack vector.

### 3. Log Analysis & Brute-Force Detection
* **Initial Access:** I parsed the MongoDB logs to identify the first connection timestamp of a brute-force cycle.
* **Attacker Identification:** Isolated the **Attacker's IP Address** by correlating failed authentication spikes with successful session establishment.
* **Connection Metrics:** Counted the total "Accepted" vs. "Ended" connections to determine the duration and intensity of the breach.

### 4. Post-Exploitation & Lateral Movement
* **Memory Analysis:** Verified the command prompt used during the memory hack to understand the attacker's interactive capabilities.
* **Data Staging:** Discovered a **Python Web Server** initiated by the attacker. 
* **Exfiltration Target:** Identified the specific directory targeted for data exfiltration, confirming that the attacker was attempting to move sensitive database files off-site.

## 📊 Incident Assessment
The system was successfully compromised via the MongoBleed vulnerability, followed by a brute-force attack for persistence. The attacker attempted to stage and exfiltrate data using a temporary Python-based web server.

## 🛡️ Countermeasures & Remediation
1. **Patching:** Immediately upgrade MongoDB to a version patched against MongoBleed (CVE-XXXX).
2. **Network Segmentation:** Place the MongoDB server behind a firewall, allowing access only from trusted IPs (Whitelist).
3. **Log Monitoring:** Implement SIEM alerts for "Python http.server" execution on production servers.
4. **Credential Rotation:** Rotate all database and system passwords, as they may have been leaked via memory disclosure.
