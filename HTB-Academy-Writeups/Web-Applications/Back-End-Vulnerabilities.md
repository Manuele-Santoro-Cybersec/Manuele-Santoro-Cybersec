# HTB Academy: Web Applications - Back-End & Vulnerabilities

## 🎯 Overview
After mastering Front-End security, this section focuses on the server-side (Back-End) logic and how attackers exploit the way databases, APIs, and servers process data.

---

## 🛠️ Back-End Components & Logic
The back-end is the "engine" of a web application. My study focused on how data travels from the user's browser to the server and eventually to the database.

* **Server-Side Languages:** Analysis of how PHP, Python, and Node.js handle user input.
* **Databases (DBMS):** Understanding the interaction between the application and databases like MySQL or MongoDB (relevant to my work on the *MangoBleed* Sherlock).
* **APIs (REST/SOAP):** How applications communicate with each other and the risks of insecure API endpoints.

---

## ⚠️ Core Vulnerabilities Analyzed
I explored the most critical server-side risks identified in the **OWASP Top 10**:

### 1. Broken Access Control
* **The Risk:** When an application does not properly enforce restrictions on what authenticated users can do.
* **Scenario:** Changing a URL from `/user/profile?id=105` to `/user/profile?id=106` to view another user's data (IDOR - Insecure Direct Object Reference).

### 2. Injection Flaws (SQLi & Command Injection)
* **Concept:** Occurs when untrusted data is sent to an interpreter as part of a command or query.
* **Defense:** Using parameterized queries (Prepared Statements) to separate data from the command.

### 3. Insecure Deserialization
* **Concept:** Exploiting the process of converting data from a format (like JSON or XML) back into an object in memory. This can lead to Remote Code Execution (RCE).

### 4. Broken Authentication
* **Focus:** Weak session management, lack of multi-factor authentication, and the dangers of unencrypted session cookies.

---

## 🛡️ Defensive Best Practices
To secure the back-end, I studied the implementation of:
* **Input Validation:** Never trusting user-supplied data.
* **Least Privilege:** Ensuring the database user only has the permissions strictly necessary.
* **Secure Logging:** (Directly related to my *Brutus* and *MangoBleed* analysis) Ensuring all critical events are logged for forensic investigation.

---

## 🏁 Conclusion
Understanding back-end vulnerabilities is the bridge between being a "script kiddie" and a professional security analyst. It allows me to look at a web request and predict where the server logic might fail.

*Status: Back-End Security Module Completed.*
