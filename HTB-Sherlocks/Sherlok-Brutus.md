# HTB Sherlock: Brutus - Write-up
**Role:** SOC Analyst / Digital Forensics  
**Focus:** Log Analysis (auth.log / wtmp) & Persistence Detection

## 🛡️ Incident Overview
An investigation into a Linux server compromise. The goal was to identify a brute-force attack, track the successful login, and uncover the persistence mechanism used by the attacker.

## 🔍 Investigation Steps

### 1. Initial Analysis (Log Triage)
I started by manually inspecting the `auth.log` file. I identified a high volume of failed login attempts for the `root` user, followed by a successful authentication.
* **Findings:** The attacker successfully logged in on **Session 37** after multiple failed attempts.

### 2. Identifying Persistence (MITRE ATT&CK T1136.001)
After gaining access, the attacker executed commands to create a new user and assign them to privileged groups.
* **Tactic:** Persistence
* **Technique:** [Create Account: Local Account (T1136.001)](https://attack.mitre.org/techniques/T1136/001/)
* **Action:** The attacker created a "backdoor" user to maintain access and exfiltrate data.

### 3. Timeline Correlation
To verify the exact duration and session details, I analyzed the `wtmp` file using the command:
`who /path/to/wtmp`

I then correlated this with the session data in `auth.log` using:
`sudo grep "session 37" auth.log`

## 📊 Summary of Evidence
| Evidence | Detail |
| :--- | :--- |
| **Attack Vector** | SSH Brute Force |
| **Successful Session** | Session 37 |
| **Persistence Method** | New User Creation (Local Account) |
| **Tooling Used** | Grep, Who, Linux Text Editor |

## 🛡️ Remediation Recommendations
1. **Disable Root Login:** Configure SSH to deny root login (`PermitRootLogin no`).
2. **Implement Fail2Ban:** Automatically block IPs after X failed attempts.
3. **MFA:** Enforce Multi-Factor Authentication for all SSH sessions.
