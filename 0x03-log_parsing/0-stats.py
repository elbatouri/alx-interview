#!/usr/bin/python3

import sys

def print_msg(status_counts, total_file_size):
    """
    Prints statistics.

    Args:
        status_counts (dict): Dictionary containing status code counts.
        total_file_size (int): Total size of files.

    Returns:
        None
    """
    print(f"File size: {total_file_size}")
    for code, count in sorted(status_counts.items()):
        if count != 0:
            print(f"{code}: {count}")

status_counts = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}
total_file_size = 0
counter = 0

try:
    for line in sys.stdin:
        parsed_line = line.split()[::-1]  # Trim and reverse
        if len(parsed_line) > 2:
            counter += 1
            if counter <= 10:
                total_file_size += int(parsed_line[0])  # file size
                status_code = parsed_line[1]  # status code
                if status_code in status_counts:
                    status_counts[status_code] += 1
            if counter == 10:
                print_msg(status_counts, total_file_size)
                counter = 0

finally:
    print_msg(status_counts, total_file_size)
