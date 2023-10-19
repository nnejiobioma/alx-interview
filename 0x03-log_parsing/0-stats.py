#!/usr/bin/env python3
import sys

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def parse_line(line):
    parts = line.split()
    if len(parts) != 10:
        return None
    try:
        file_size = int(parts[-1])
        status_code = int(parts[-2])
        return file_size, status_code
    except (ValueError, IndexError):
        return None

def print_metrics():
    print(f"Total file size: File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

try:
    for line in sys.stdin:
        line = line.strip()
        parsed = parse_line(line)
        if parsed:
            file_size, status_code = parsed
            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            line_count += 1
            if line_count % 10 == 0:
                print_metrics()
except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print_metrics()
