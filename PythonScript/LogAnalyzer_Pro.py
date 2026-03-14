import os

def filter_logs_by_ip(input_file, target_ip, output_file):
    """
    Parses a log file and extracts all entries related to a specific IP address.
    
    Args:
        input_file (str): Path to the source log file.
        target_ip (str): The IP address to search for.
        output_file (str): Path where the filtered results will be saved.
    """
    try:
        # Check if the input file exists before attempting to open it
        if not os.path.exists(input_file):
            print(f"[!] Error: The file '{input_file}' was not found.")
            return

        match_count = 0
        
        # Using 'with' statements ensures files are properly closed after processing
        with open(input_file, 'r') as src, open(output_file, 'w') as report:
            
            # Writing a professional header for the output report
            report.write("==========================================\n")
            report.write(f"SOC ANALYSIS REPORT: IP INVESTIGATION\n")
            report.write(f"Target Identifier: {target_ip}\n")
            report.write("==========================================\n\n")

            # Iterating through the file line by line for memory efficiency
            for line_number, line in enumerate(src, 1):
                if target_ip in line:
                    # Log the matching line and its original position
                    report.write(f"Line {line_number}: {line}")
                    match_count += 1
            
            # Writing the final summary
            report.write(f"\nSummary: {match_count} occurrences found for {target_ip}.\n")
            report.write("End of Report.\n")

        print(f"[*] Success: {match_count} entries exported to '{output_file}'.")

    except Exception as e:
        # Catching unexpected errors (e.g., permission issues)
        print(f"[!] An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Standard entry point for the script
    # Change these variables to test with your own files
    LOG_TO_SCAN = "server_access.log"
    SUSPICIOUS_IP = "192.168.1.50"
    RESULT_FILE = "investigation_results.txt"

    print("--- LogAnalyzer Pro: Starting Analysis ---")
    filter_logs_by_ip(LOG_TO_SCAN, SUSPICIOUS_IP, RESULT_FILE)
