# Forensic Investigation: Operation Dream Job (Lazarus APT)

## 📌 Incident Overview
This Sherlock involves a Digital Forensics investigation into a targeted spear-phishing attack attributed to the **Lazarus Group (APT)**. The threat actor utilized a "dream job" social engineering lure (posing as Lockheed Martin) to trick a user into mounting a malicious ISO file. The goal of this analysis was to reconstruct the infection chain from the initial mount to the establishment of persistence.

## 🛠️ Methodology & Forensic Tools
I employed a hybrid forensic workflow, utilizing industry-standard Windows tools for artifact extraction and a **Linux environment** for advanced data processing and correlation.

### 1. Windows Artifact Analysis
* **Shortcut (.lnk) Analysis:** Used `LECmd` to decode the malicious shortcut found within the ISO. This revealed the use of **Signed Binary Proxy Execution**, where `rundll32.exe` was used to load a hidden DLL.
* **Registry Forensics:** Investigated System and User Hives (`NTUSER.DAT`) using `Registry Explorer` to identify unauthorized modifications in the boot/logon process.
* **Timeline Reconstruction:** Parsed the Master File Table (MFT) to establish a precise sequence of events surrounding the ISO mount and the subsequent file drops.

### 2. Linux-Based Data Processing
To increase efficiency and handle the extracted forensic data more effectively, I transitioned to a **Linux environment** for the final stages of the investigation:
* **Command-Line Agility:** Utilized `grep`, `awk`, and `sed` to filter through exported CSVs from the MFT and USNJournal. This allowed for near-instant identification of the malicious DLL creation timestamp.
* **Log Correlation:** Processed triage data using Bash scripting to correlate the execution of `rundll32.exe` with the writing of persistence keys in the registry.
* **Streamlined Workflow:** The Linux CLI provided a faster, more flexible environment for searching across multiple forensic artifacts simultaneously, a critical skill in time-sensitive SOC environments.

## 🔍 Key Findings & Technical Learnings

### Infection Vector & Evasion
The investigation confirmed the use of an ISO image to bypass **Mark-of-the-Web (MotW)** protections. The execution relied on a malicious DLL (`o6be68.dll`) triggered via a deceptive `.lnk` file, mapping to **MITRE T1218.011**.

### Persistence Mechanism
By analyzing the Registry Run keys, I identified how the malware ensured its survival across reboots. The attacker created an entry named `UpdateService` to re-execute the malicious payload at every user logon (**MITRE T1547.001**).

### Threat Actor Profiling
Analyzing this case provided deep insights into the TTPs (Tactics, Techniques, and Procedures) of the Lazarus Group, specifically their reliance on job-themed lures and stealthy persistence through native Windows binaries.

## 🛡️ Conclusion
This case study demonstrates my ability to handle complex APT-level investigations. By integrating **Linux-based analysis** into the forensic workflow, I was able to accelerate the detection of the attack's persistence and accurately map the threat actor's activity across the system.

---
**Candidate:** Manuele - Junior SOC Analyst / DFIR Specialist
**Platform:** Hack The Box (Sherlocks)
