# Technical Analysis: Web Application Front-End Vulnerabilities

## 🎯 Overview
This section covers the "Client-Side" of web security. Unlike back-end attacks that target the server/database, front-end attacks target the **User** by exploiting how the browser renders HTML, CSS, and JavaScript.

## 🔍 Key Vulnerabilities Analysed

### 1. Cross-Site Scripting (XSS)
I explored the three main types of XSS and how they appear in a SOC environment:
* **Reflected XSS:** Malicious scripts "echoed" back from a URL parameter.
    * *Analyst Note:* In logs, look for `<script>` tags or encoded strings like `%3Cscript%3E` in GET request parameters.
* **Stored (Persistent) XSS:** The script is saved on the server (e.g., in a comment section) and executes for every user who views the page.
* **DOM-based XSS:** The vulnerability exists entirely in the client-side code (JavaScript) without necessarily reaching the server.

### 2. Cross-Site Request Forgery (CSRF)
I analysed how attackers trick authenticated users into performing unwanted actions (like changing a password) by exploiting the browser's automatic cookie-sending behaviour.
* **Defense identified:** Use of `SameSite` cookie attributes and unique **Anti-CSRF Tokens**.

### 3. Clickjacking (UI Redressing)
I learned how attackers use invisible `<iframe>` layers to trick users into clicking buttons they cannot see.
* **SOC Observation:** This is prevented by checking for the `X-Frame-Options` or `Content-Security-Policy (CSP)` headers in the web server's responses.

## 🛠️ Tools & Methodology
* **Browser Inspector (F12):** Essential for viewing the DOM and identifying where unsanitized input is being rendered.
* **Burp Suite Repeater:** Used to test if the server "reflects" specific characters (like `< > " '`) without encoding them.
* **DOMPurify (Concept):** Researched how modern front-end frameworks use libraries to "sanitize" HTML before rendering.

## 🛡️ The "Blue Team" Defense Strategy
As a SOC Analyst, I would recommend these front-end "Hardening" steps:
1.  **Strict Content Security Policy (CSP):** Disallow inline scripts and only allow JS from trusted domains.
2.  **Input Validation + Output Encoding:** Ensure that `<` becomes `&lt;` so the browser treats it as text, not a command.
3.  **Secure Cookies:** Set `HttpOnly` (prevents JS from stealing cookies) and `Secure` (only sends over HTTPS) flags.

---
*Next Step: Progressing into Back End Component and Back End Vulnerabilities*
