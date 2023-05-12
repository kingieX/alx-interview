#!/usr/bin/python3
import sys
import signal
"""
A script that reads stdin line by line
"""

total_file_size = 0
status_code_counts = {}

def signal_handler(signal, frame):
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

line_count = 0
for line in sys.stdin:
    line = line.strip()

    if not line.startswith('"GET ') or len(line.split()) != 7:
        continue

    parts = line.split()
    status_code = parts[5]
    file_size = parts[6]


    total_file_size += int(file_size)
    status_code_counts[status_code] =status_code_counts.get(status_code, 0) + 1

    line_count += 1

    if line_count % 10 == 0:
        print_statistics()

print_statistics()

def print_statistics():
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_code_counts.keys()):
        if status_code_isdigit():
            count = status_code_counts[status_code]
            print(f"{status_code}: {count}")
