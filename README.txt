# README.txt
This app creates a streaming Splunk command which enriches your logs with email addresses from hunter.io when provided a domain as a field. 

### TA for HunterIO
Apache 2.0

### Installation
1) Install TA
2) Open hunterio_ta/bin/hunterio.py in your favorite text editor
3) Add your hunter.io API Key
4) Restart Splunk

### Usage
1) Alias or create a domain field in Splunk called hunter_domain
2) Pipe the results of your search to | hunterio
3) The command will return a hunter_addresses
4a) Consider making your own lookup tables to save on reran researches

### Help
see: https://www.hunter.io
see: http://www.oldlogsnewtricks.com

### Contribute
see: https://github.com/dpwtheitguy/hunterio_ta

### Author
daniel . p . wilson@live.com

### Known Issues/Todo
1) Error checking
2) Needs a Splunk GUI
3) Provide Sample searches

### History
1.2.2021 - dwilson, initial version
