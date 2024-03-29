#!/usr/bin/env python3

import sys
import signal

# Function to handle SIGINT (Ctrl+C)
def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)


# Register SIGINT handler
signal.signal(signal.SIGINT, signal_handler)


# Initialize variables to hold statistics
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


# Function to print statistics
def print_statistics():
    print("File size:", total_file_size)
    for status_code in sorted(status_code_counts.keys()):
        if status_code_counts[status_code] > 0:
            print(f"{status_code}: {status_code_counts[status_code]}")


# Main loop to read from stdin
for line in sys.stdin:
    line = line.strip()
    parts = line.split()
    if len(parts) == 7 and parts[2] == "GET" and parts[3].startswith("/projects/") and parts[4].startswith("HTTP/1.1"):
        try:
            status_code = int(parts[5])
            file_size = int(parts[6])
            total_file_size += file_size
            status_code_counts[status_code] += 1
            line_count += 1
            # Print statistics after every 10 lines
            if line_count % 10 == 0:
                print_statistics()
        except ValueError:
            pass  # Skip lines with invalid status code or file size
    else:
        pass  # Skip lines not in the expected format


# Print final statistics if the loop exits without interruption
print_statistics()
