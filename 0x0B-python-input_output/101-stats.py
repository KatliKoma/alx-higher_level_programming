#!/usr/bin/python3
"""Script for reading from stdin and calculating metrics."""

def print_metrics(total_size, status_code_counts):
    """Prints the metrics for file size and status code occurrences."""
    print("File size: {}".format(total_size))
    for code in sorted(status_code_counts.keys()):
        print("{}: {}".format(code, status_code_counts[code]))

if __name__ == "__main__":
    import sys

    total_size = 0
    status_code_counts = {}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) > 2:
                size = parts[-1]
                status_code = parts[-2]

                # Update total size
                try:
                    total_size += int(size)
                except ValueError:
                    pass

                # Update status code count
                if status_code in valid_codes:
                    if status_code not in status_code_counts:
                        status_code_counts[status_code] = 0
                    status_code_counts[status_code] += 1

            line_count += 1
            if line_count % 10 == 0:
                print_metrics(total_size, status_code_counts)

    except KeyboardInterrupt:
        print_metrics(total_size, status_code_counts)
        raise

    # Print final metrics if not already printed after KeyboardInterrupt
    print_metrics(total_size, status_code_counts)

