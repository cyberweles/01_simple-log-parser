# 01_scripts/log_generator.py
import random
from datetime import datetime, timedelta
import os

def generate_logs(filename, num_logs):
    """Generates sample Apache server logs."""
    ips = ["192.168.1.1", "10.0.0.5", "203.0.113.1", "172.16.254.1"]
    users = ["-", "janek", "marek", "anna"]
    methods = ["GET", "POST", "PUT", "DELETE"]
    endpoints = ["/", "/login", "/logout", "/admin", "/api/v1/data", "/images/logo.png"]
    statuses = [200, 200, 200, 200, 200, 401, 403, 404, 500, 503]
    
    # Ensure the logs directory exists
    logs_dir = os.path.dirname(filename)
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    with open(filename, 'w') as f:
        for _ in range(num_logs):
            ip = random.choice(ips)
            user = random.choice(users)
            timestamp = (datetime.now() - timedelta(minutes=random.randint(1, 60))).strftime("[%d/%b/%Y:%H:%M:%S +0100]")
            method = random.choice(methods)
            endpoint = random.choice(endpoints)
            status = random.choice(statuses)
            size = random.randint(100, 5000)
            log_line = f'{ip} {user} {user} {timestamp} "{method} {endpoint} HTTP/1.1" {status} {size} "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"\n'
            f.write(log_line)

if __name__ == "__main__":
    log_file = "00_logs/webserver.log"
    generate_logs(log_file, 100)
    print(f"Generated 100 sample logs in {log_file}")

