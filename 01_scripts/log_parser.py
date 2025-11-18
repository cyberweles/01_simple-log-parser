# 01_scripts/log_parser.py
import re
import os

def parse_logs(input_filename, output_filename):
    """Parses logs and searches for 4xx/5xx errors, saving the result."""
    
    # Regular expression (regex) to match standard Apache log format
    # Matches: IP, user1, user2, [timestamp], "Method Endpoint HTTP/Version", Status Code, Size
    log_pattern = re.compile(r'^(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<timestamp>.*?)\] "(?P<method>.*?)\s(?P<endpoint>.*?)\sHTTP/1\.\d" (?P<status>\d{3}) (?P<size>\d+) ".*?" ".*?"$')
    
    error_logs = []
    
    with open(input_filename, 'r') as f:
        for line in f:
            match = log_pattern.match(line)
            if match:
                data = match.groupdict()
                # We are interested in error statuses (e.g., 401, 403, 404, 500)
                if data['status'].startswith('4') or data['status'].startswith('5'):
                    error_logs.append(f"[{data['timestamp']}] ERROR {data['status']} from IP: {data['ip']} for {data['endpoint']}\n")

    # Ensure the results directory exists
    results_dir = os.path.dirname(output_filename)
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    with open(output_filename, 'w') as f:
        f.writelines(error_logs)
        
    print(f"Analysis complete. Found {len(error_logs)} error lines.")

if __name__ == "__main__":
    input_path = "00_logs/webserver.log"
    output_path = "02_results/error_summary.txt"
    
    if os.path.exists(input_path):
        parse_logs(input_path, output_path)
    else:
        print(f"Error: Log file not found at {input_path}")

