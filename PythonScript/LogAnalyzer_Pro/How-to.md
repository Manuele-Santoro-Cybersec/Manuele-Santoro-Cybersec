LogAnalyzer Pro - Documentation
Purpose:
This script was developed to assist SOC analysts in the initial triage of large log files. Instead of manually searching through thousands of entries, this tool automates the extraction of specific indicators of compromise (IoC), such as suspicious IP addresses.

Why I built it this way:

Memory Efficiency: The script reads the file line-by-line using a generator-like approach. This is crucial for security analysts because real-world log files can be several gigabytes in size; loading them all at once would crash the system.

Error Handling: I implemented os.path.exists and try-except blocks to ensure the script doesn't just crash if a file is missing or permissions are restricted.

Professional Reporting: The output isn't just a list of lines; it includes a structured header and a summary, making it ready for escalation to Tier 2 teams.

How to run it:

Place your log file in the same directory as the script (or provide the full path).

Update the LOG_TO_SCAN and SUSPICIOUS_IP variables in the if __name__ == "__main__": block.

Run the command: python LogAnalyzer_Pro.py

Check investigation_results.txt for the final report.
