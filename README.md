# Simple Log Analyzer

A minimal introductory project for learning log parsing and basic security automation.  
The script analyzes Apache-style webserver logs and extracts HTTP error responses (4xx/5xx), providing a simple summary useful in early SOC workflows.

## Project Structure

01_simple-log-parser/
├── 00_logs/ # Raw webserver logs
├── 01_scripts/ # Generator + parser scripts
├── 02_results/ # Output reports
├── README.md
└── structure_tree.txt


## Scripts

- **log_generator.py** — creates sample demonstration logs  
- **log_parser.py** — parses logs using regex and extracts error events  

## How to Run

python3 01_scripts/log_generator.py
python3 01_scripts/log_parser.py


## Skills Demonstrated

- Log parsing fundamentals  
- Regex pattern extraction  
- Automation using Python  
- Intro SOC-style error identification  

---

## Author

**cyberweles**  
GitHub: https://github.com/cyberweles

---

## License

MIT License
