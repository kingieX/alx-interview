#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

# Initialize metrics
total_file_size = 0
status_code_counts = {}

# Define signal handler for keyboard interruption
def signal_handler(signal, frame):
    print_statistics()
    sys.exit(0)

# Register signal handler for keyboard interruption (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

# Read stdin line by line
line_count = 0
for i in range(10000):
    sleep(random.random())
    line = "{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    )
    line = line.strip()

    # Skip lines that don't match the expected format
    if not line.startswith('"GET ') or len(line.split()) != 7:
        continue

    # Parse the line to extract relevant information
    parts = line.split()
    status_code = parts[5]
    file_size = parts[6]

    # Update metrics
    total_file_size += int(file_size)
    status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1

    line_count += 1

    # Print statistics after every 10 lines
    if line_count % 10 == 0:
        print_statistics()

# Print final statistics
print_statistics()

def print_statistics():
    print(f"Total file size: {total_file_size}")
    for status_code in sorted(status_code_counts.keys()):
        if status_code.isdigit():
            count = status_code_counts[status_code]
            print(f"{status_code}: {count}")
